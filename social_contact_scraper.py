from playwright.sync_api import sync_playwright
import re
import ast

def parse_each_line_to_dict(line):
    # Define a function to safely parse a string into a dictionary
    try:
        # Convert the string representation of a dictionary to an actual dictionary
        return ast.literal_eval(line.strip())
    except ValueError as e:
        print(f"An error occurred while parsing line to dict: {e}")
        return None

def get_social_media_urls(page_content, pattern_list):
    for url in re.compile(pattern_list[1]).findall(page_content):
        if url == None:
            return {pattern_list[0]: ''}
        return {pattern_list[0]: url}


def get_gmail_url(page_content):
    for url in re.compile(r'mailto:%20([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})').findall(page_content):
        if url == None:
            return {'Mail': ''}
        return {'Mail': url}

def get_facebook_url(page_content):
    facebook_urls = re.compile(r'https:\/\/www\.facebook\.com\/[A-Za-z0-9._-]+').findall(page_content)
    for facebook_url in facebook_urls:
        if facebook_url == None:
            return {'Facebook' : ''}
        elif not facebook_url.endswith('/tr'):
            return {'Facebook': facebook_url}

def scrape(page_content):
    medias = []
    social_media_patterns = [
        ['Youtube', r'https?://(?:www\.)?youtube\.com/@[^/\s"\']+/?'],
        ['Instagram', r'https?://(?:www\.)?instagram\.com/[^/\s"\']+/?'],
        ['Twitter', r'https?://(?:www\.)?twitter\.com/[^/\s"\']+/?'],
        ['Linkedin', r'https?://(?:www\.)?linkedin\.com/[^\s"\']*'],
        ['Reddit', r'https?://(?:www\.)?reddit\.com/[^/\s"\']+/?'],
        ['Tiktok', r'https?://(?:www\.)?tiktok\.com/[^/\s"\']+/?'],
    ]

    # Extract social media URLs
    for media_pattern in social_media_patterns:
        social_media_url = get_social_media_urls(page_content, media_pattern)
        medias.append(social_media_url if social_media_url is not None else {media_pattern[0] : ''})

    gmail_url = get_gmail_url(page_content)
    medias.append(gmail_url if gmail_url is not None else {"Mail": ''})

    facebook_url = get_facebook_url(page_content)
    medias.append(facebook_url if facebook_url is not None else {"Facebook": ''})
    return medias


def main():
    with sync_playwright() as p:
        # Launch a browser instance
        browser = p.chromium.launch(headless=True)
        # Open a new browser page
        page = browser.new_page()

        # Open the original file in read mode and the result file in write mode
        with open('output.txt', 'r') as infile, open('result.txt', 'w') as outfile:
            for line in infile:
                # Parse the line to a dictionary
                line_dict = parse_each_line_to_dict(line)
                if line_dict is not None:
                    # Fetch the website from the dictionary
                    website = line_dict.get('Website', 'No website found')

                    # Navigate to the target URL (e.g., a web page where social media links are located)
                    try:
                        page.goto("https://" + website)  # Replace with your target page URL
                        # Get the content of the page
                        content = page.content()
                        New_dict = scrape(content)
                        for new_dict in New_dict:
                            line_dict.update(new_dict)
                    except Exception as e:
                        line_dict.update({'Youtube': '', 'Instagram': '', 'Twitter': '', 'Linkedin': '', 'Reddit': '', 'Tiktok': '', 'Facebook' : '', 'Mail' : ''})
                        print(f"An error occurred: {e}")
                    print(line_dict)
                    outfile.write(f"{str(line_dict)}\n")
                    
        # Close the browser instance
        outfile.close()
        browser.close()

if __name__ == "__main__":
    main()