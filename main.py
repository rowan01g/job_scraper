from bs4 import BeautifulSoup
import requests 
import re 

#job = input("What Jobs do you want to look for?")
url = "https://www.gradcracker.com/search/science/graduate-jobs"

try:
    response = requests.options(url)
    if response.ok:
        print("Success - API is accessible.")
    else:
        print(f"Failure - API is accessible but something is not right. Response code : {response.status_code}")
except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
    print(f"Failure - Unable to establish connection: {e}.")
except Exception as e:
    print(f"Failure - Unknown error occurred: {e}.")






#page = requests.get(url).text

#doc = BeautifulSoup(page, "html.parser")

#page_text = doc.find(class_= "tw-relative tw-z-0 tw-inline-flex tw-rounded-md tw-shadow-sm")
#print(page_text)