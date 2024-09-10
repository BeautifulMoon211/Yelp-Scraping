from matplotlib.path import Path
import re
import os
from dotenv import load_dotenv
from operator import itemgetter

from urllib.parse import quote
from playwright.async_api import async_playwright
from rich.console import Console
import time
from urllib.parse import urlparse, parse_qs 

load_dotenv()
console = Console()

BASE_URL = "https://www.yelp.com"
SCRAPERAPI_KEY = os.getenv('SCRAPERAPI_KEY')  # Replace with your ScraperAPI key
SCRAPERAPI_ENDPOINT = "https://api.scraperapi.com/?api_key=" + SCRAPERAPI_KEY  # ScraperAPI endpoint

# websiteURL = input("Please enter the website URL: ")
websiteURL = "https://www.yelp.com/biz/exact-solar-newtown?osq=solar&override_cta=Request+pricing+%26+availability"

# map_URL = input("Please enter the map URL: ")
map_URL = "https://maps.googleapis.com/maps/api/staticmap?size=315x150&sensor=false&client=gme-yelp&language=en&scale=1&path=color%3A0x1F8EFF70%7Cweight%3A2%7Cfillcolor%3A0x1F8EFF40%7C45.320217%2C-74.108698%7C45.320217%2C-73.972597%7C45.473512%2C-73.533685%7C45.513923%2C-73.523972%7C45.695482%2C-73.523972%7C45.695482%2C-73.890733%7C45.444594%2C-74.108698%7C45.320217%2C-74.108698&signature=zY5GdtG1klTnHMytXWUAxW1DTPw="

# file_path = 'choosingCityInput_USA.txt'  # Replace this with the path to your file
file_path = 'choosingCityInput_Canada.txt'

parsed_data = []
parsed_xy = []

def is_point_in_polygon(point, polygon_vertices):  
    polygon_path = Path(polygon_vertices)
    return polygon_path.contains_point(point)

def get_bound_points(points_list):
    tx = 50
    ty = -60
    bx = 20
    by = - 130
    for point in points_list:
        if tx > point[0]:
            tx = point[0]
        if bx < point[0]:
            bx = point[0]
        if ty > point[1]:
            ty = point[1]
        if by < point[1]:
            by = point[1]
    return [tx, ty, bx, by]

def get_bound(arr, val, key1="x", key2="y"):
    l = len(arr)
    st, ed = 0, l
    while st < ed:
        md = int(st + (ed - st) / 2)
        ct = arr[md]
        if ct.get(key1) < val.get(key1) or ct.get(key1) == val.get(key1) and ct.get(key2) < val.get(key2):
            st = md + 1
        if ct.get(key1) > val.get(key1) or ct.get(key1) == val.get(key1) and ct.get(key2) >= val.get(key2):
            ed = md
    return st

parsed_sc = []

def final(points_list):
    # Reading file contents
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            # Strip off the beginning and ending brackets and quotes
            coordinates_str, location_str = line.split(' : ')
            # print(coordinates_str, location_str)

            coordinates_str = coordinates_str.strip('[]')
            location_str = location_str.strip('[]').replace('"', '')
            # Split coordinates and location into their respective components
            x, y = map(float, coordinates_str.split(', '))
            state, city = location_str.split(', ')

            # Append to the parsed_data list

            for i in parsed_sc:
                if {"state": state, "city": city} == i:
                    # print(state, city)
                    break
            else:
                parsed_sc.append({"state": state, "city": city})
                parsed_data.append({
                    "x": x,
                    "y": y,
                    "state": state,
                    "city": city
                })

            for i in parsed_xy:
                if {"x": x, "y": y} == i:
                    print({"x": x, "y": y, "state": state, "city": city})
                    break                    
            parsed_xy.append({"x": x, "y": y})

    print("parsed_sc:", parsed_sc)
    print("parsed_data:", parsed_data)
    with open('result_.txt', 'a') as output:
        output.write(str(parsed_data))

    tx, ty, bx, by = get_bound_points(points_list)
    print("Endpoints are ", tx, ty, bx, by)

    sorted_data = sorted(parsed_data, key=itemgetter("x", "y"))
    filtered_data = sorted_data[get_bound(sorted_data, {"x": tx, "y": ty}) : get_bound(sorted_data, {"x": bx, "y": by})]

    if not filtered_data:
        print("No result")
    else:
        sorted_data = sorted(filtered_data, key=itemgetter("y", "x"))
        filtered_data = sorted_data[get_bound(sorted_data, {"x": tx, "y": ty}, key1="y", key2="x") : get_bound(sorted_data, {"x": bx, "y": by}, key1="y", key2="x")]
        if not filtered_data:
            print("No result")
        else:
            cities_list = []
            print("filtered ", len(filtered_data), filtered_data)
            for data in filtered_data:
                point = list({data['x'], data['y']})
                if is_point_in_polygon(point, points_list):
                    cities_list.append(data['city'])
                    # cities_list.append(data['city'] + ', ' + data['state'])

            print("\n\nThese cities are in the blue box!!!\n The totla number of cities : ", len(cities_list), "\nCities are : ", cities_list)


class CityCoordinates:
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

    async def initialize_browser(self):
        try:
            pw = await async_playwright().start()
            proxy_url = await self.get_scraperapi_url(self.ensure_str(websiteURL))
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

    async def extract_coordinates(self):  
        img_selector = 'section[aria-label="Location & Hours"] img'  
        img_src = await self.page.get_attribute(img_selector, 'src')

        if img_src:  
            return parse_map(img_src)
    
    async def scrape(self):
        try:
            await self.initialize_browser()
            time.sleep(5)
            coordinates = await self.extract_coordinates()
            return coordinates
        except Exception as e:
            console.log(f"Scraping failed: {e}")
        finally:
            if self.browser:
                await self.browser.close()

def parse_map(mapURL):
    query = urlparse(mapURL).query
    params = parse_qs(query)  

    # Extract the 'path' parameter that contains the encoded coordinates string  
    path_params = params.get('path')  
    if path_params:  
        encoded_path = path_params[0]
        coordinates_str = re.findall(r'(\d+\.\d+,-\d+\.\d+)', encoded_path)  
        coordinates = [tuple(map(float, coord.split(','))) for coord in coordinates_str]  
        print('Coordinates: ', coordinates)
        return coordinates

async def main_websiteURL():
    cityCoordinates = CityCoordinates()
    coordinates = await cityCoordinates.scrape()
    final(coordinates)

def main_mapURL():
    coordinates = parse_map(map_URL)
    final(coordinates)

if __name__ == "__main__":
    main_mapURL()