import asyncio
import os
from dotenv import load_dotenv
from urllib.parse import unquote, urlencode, quote
from playwright.async_api import async_playwright
from rich.console import Console

load_dotenv()
console = Console()
BASE_URL = "https://www.yelp.com"
SCRAPERAPI_KEY = os.getenv('SCRAPERAPI_KEY')  # Replace with your ScraperAPI key
SCRAPERAPI_ENDPOINT = "https://api.scraperapi.com/?api_key=" + SCRAPERAPI_KEY  # ScraperAPI endpoint

class SolarScraper:
    def __init__(self):
        self.browser = None
        self.context = None
        self.page = None

    def ensure_str(self, url):
        if not url:
            return ""
        if isinstance(url, bytes):
            return url.decode('utf-8')
        return str(url)

    async def get_scraperapi_url(self, url):
        return f"{SCRAPERAPI_ENDPOINT}&url={quote(url)}&render=true"

    async def initialize_browser(self, business_type, business_location):
        base_url = "https://www.yelp.com/search?"
        
        # Define parameters for the query string
        params = {
            'find_desc': business_type,
            'find_loc': business_location
        }

        # Encode the parameters into a query string
        query_string = urlencode(params)

        # Construct the full URL
        search_url = base_url + query_string
        self.original_url = search_url
        try:
            pw = await async_playwright().start()
            proxy_url = await self.get_scraperapi_url(self.ensure_str(search_url))
            self.page_url = proxy_url
            self.browser = await pw.chromium.launch(headless=False)
            self.context = await self.browser.new_context()
            self.page = await self.context.new_page()
            await self.page.goto(self.ensure_str(proxy_url), timeout = 600000)
            await self.page.wait_for_load_state('domcontentloaded')
            console.log(f"Page successfully loaded: {proxy_url}")
        except Exception as e:
            console.log(f"Error during browser initialization or navigation: {e}")
            raise

    async def extract_data_from_page(self):
        company_names = []
        company_urls = []
        try:
            company_elements = await self.page.query_selector_all("a.y-css-12ly5yx")
            if not company_elements:
                raise Exception("No company_elements found")
            
            for element in company_elements:
                try:
                    company_name = await element.text_content()
                    print(company_name)
                    if company_name:
                        company_names.append(unquote(company_name))
                    else:
                        print("company_name is None or empty")
                        continue
                except Exception as e:
                    print(f"Error getting company_name: {e}")
                    continue

                try:
                    href = await element.get_attribute("href")
                    if href:
                        full_url = BASE_URL + href
                        company_urls.append(full_url)
                    else:
                        print("href is None or empty")
                        company_urls.append("")
                except Exception as e:
                    print(f"Error getting href: {e}")
                    company_urls.append("")

            return company_names, company_urls

        except Exception as e:
            print(f"Error during data extraction: {e}")
            return company_names, company_urls

    async def get_info_from_page(self):
        try:
            company_names, company_urls = await self.extract_data_from_page()
        except:
            company_names, company_urls = []
        
        company_data = list(zip(company_names, company_urls))
        print(f"len(company_data)-f{len(company_data)}")
        # Wait until the page is fully loaded
        await self.page.wait_for_load_state("load")

        businesses_info = []
        for element in company_data:
            company_name = element[0]
            url = element[1]
            print("***********************************************")
            print(f"company_data-{element}")
            print("***********************************************")
            self.count = self.count + 1
            proxy_url = await self.get_scraperapi_url(self.ensure_str(url))
            # Wait until the page is fully loaded
            await self.page.wait_for_load_state("load")
            await self.page.goto(proxy_url, timeout = 600000)


            # Locate all the sections containing business information
            business_website = ""
            business_phone = ""
            business_address = ""
            business_owner = ""
            try:
                # Extract business website
                business_website_tag = await self.page.query_selector('p:has-text("Business website")')

                if business_website_tag:
                    # Find the next <p> sibling that contains the company name
                    business_website_tag = await business_website_tag.evaluate_handle('(p) => p.nextElementSibling')

                    if business_website_tag:
                        business_website = await business_website_tag.inner_text()
                    else:
                        business_website = ""
                else:
                    business_website = ""
            except:
                business_website = ""

            
            # Extract Phone Number
            try:
                phone_number_tag = await self.page.query_selector('p:has-text("Phone number")')
                if phone_number_tag:
                    phone_number_value_tag = await phone_number_tag.evaluate_handle('(p) => p.nextElementSibling')
                    if phone_number_value_tag:
                        business_phone = await phone_number_value_tag.inner_text()
                    else:
                        business_phone = ""
                else:
                    business_phone = ""
            except:
                business_phone = ""


            # Extract Address
            try:
                address_direction_tag = await self.page.query_selector('p:has-text("Get Directions")')
                if address_direction_tag:
                    address_tag = await address_direction_tag.evaluate_handle('(p) => p.nextElementSibling')
                    if address_tag:
                        business_address = await address_tag.inner_text()
                    else:
                        business_address = ""
                else:
                    business_address = ""
            except:
                business_address = ""


            try:
                # Extract Business Owner
                content = await self.page.content()
                # Search for the string "About the Business"
                if "About the Business" in content:
                    owner_tag = await self.page.query_selector('p.y-css-w3ea6v')
                    if owner_tag:
                        print("Found onwer_tag")
                        # Do something with the element, for example, get its text content
                        business_owner = await owner_tag.inner_html()
                        if len(business_owner) < 4 or len(business_owner) > 20:
                            business_owner = ""
                        print(business_owner)
                    else:
                        business_owner = "" 
                else: 
                    business_owner = ""
            except:
                business_owner = ""

            company_number = self.count

            business_info = {
                "Number": company_number,
                "Name": company_name,
                "Website": business_website,
                "Phone": business_phone,
                "Address": business_address,
                "Owner": business_owner
            }
            businesses_info.append(business_info)

            print(f"Number of Businesses - {company_number}")
            print(f"Business-{business_info}")

        company_info = []
        company_name = []
        for element in businesses_info:
            if element["Name"] not in company_name:
                company_info.append(element)
                company_name.append(element["Name"])

        print(company_info)
        return company_info
    
    async def scrape(self, business_type, business_location):
        try:
            business_type = business_type
            business_location = business_location
            self.count = 0
            await self.initialize_browser(business_type, business_location)
            businesses_info = []
            page_number = 6
            while True:
                # Perform your data extraction here before moving to the next page
                businesses_info_one_page = await self.get_info_from_page()
                print(self.page_url)
                print("sss")
                await self.page.goto(self.page_url, timeout = 600000)
                print("sss")

                businesses_name = []
                for element in businesses_info:
                    businesses_name.append(element["Name"])

                for element in businesses_info_one_page:
                    if element["Name"] not in businesses_name:
                        businesses_info.append(element) 

                count = 1               
                for element in businesses_info:
                    element["Number"] = count
                    count = count + 1

                print(businesses_info)
            
                with open('output.txt', 'w', encoding = 'utf-8') as file:
                    for element in businesses_info:
                        file.write(f"{element}\n")  # Write each number followed by a newline

                # Wait for the "Next Page" button to be available
                next_button = await self.page.wait_for_selector('button.pagination-button__09f24__kbFYf.y-css-1ewzev', timeout = 12000000)

                # If the "Next Page" button is not found, break the loop
                if not next_button:
                    print("No more pages.")
                    break

                is_disabled = await next_button.get_properties('disabled')
                is_disabled_value = await is_disabled.json_value()
                if is_disabled_value:
                    print("Next page button is disabled or deactivated. Stopping.")
                    break

                page_number = page_number + 1
                # Wait for the new page content to load by waiting for a specific element that indicates new content is loaded
                next_page_url = f"{self.original_url}&start={page_number * 10}"
                proxy_url = await self.get_scraperapi_url(self.ensure_str(next_page_url))
                self.page_url = proxy_url

                await self.page.goto(self.ensure_str(self.page_url), timeout = 60000)
                await self.page.wait_for_selector('a.y-css-12ly5yx')

            await self.get_info_from_page()
        except Exception as e:
            console.log(f"Scraping failed: {e}")
        finally:
            if self.browser:
                await self.browser.close()

async def main():
    solarscraper = SolarScraper()
    business_type = "plumbing"
    business_location = "Ville-Marie, Montreal, QC, Canada"
    await solarscraper.scrape(business_type, business_location)

if __name__ == "__main__":
    import asyncio

    # Get the event loop and run the 'main' function until it's done
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())