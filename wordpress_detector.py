import requests  

def check_url_exists(url):  
    try:  
        response = requests.get(url)  
        # A status code of 200 to 299 means the site exists and is reachable  
        if response.status_code == 200:  
            print(f"The URL '{url}' exists!")  
            return True  
        elif response.status_code == 404:  
            print(f"The URL '{url}' does not exist (404 Not Found).")  
            return False  
        else:  
            print(f"The URL '{url}' returned status code {response.status_code}.")  
            return False  
    except requests.exceptions.RequestException as e:  
        # This will catch all other exceptions (network errors, DNS problems, etc.)  
        print(f"An error occurred: {e}")  
        return False  

# Example usage  
url_to_check = input("Please enter the website URL: ")
if url_to_check[-1] == '/':
    websiteURL = url_to_check + "/wp-admin"
else:
    websiteURL = url_to_check + "wp-admin"
url_exists = check_url_exists(url_to_check + "/wp-admin")