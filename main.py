from bs4 import BeautifulSoup
import requests 
import re 

#job = input("What Jobs do you want to look for?")
urls_dict = {
        "GRB" : "https://www.grb.uk.com/graduate-jobs?keywords=",
        "Civil Service" : "https://www.civilservicejobs.service.gov.uk/csr/index.cgi?SID=b3duZXI9NTA3MDAwMCZjb250ZXh0aWQ9MTEwMTgyOTg3Jm93bmVydHlwZT1mYWlyJnBhZ2VjbGFzcz1TZWFyY2gmcGFnZT0xJnBhZ2VhY3Rpb249c2VhcmNoY29udGV4dCZyZXFzaWc9MTczNDcyOTcxMy1jOGI3MzZhNTcwN2EwZDQ3MTdiYjE3MjRiZjRlY2FjZTg0YmRkODlj&sort=opening&submit_results_sort_form=Refresh+sort&reqsig=1734729713-c8b736a5707a0d4717bb1724bf4ecace84bdd89c",
        "Bright Network" : "https://www.brightnetwork.co.uk/graduate-jobs/pharmaceuticals-science/"
        }


urls_list = list(urls_dict.keys())
print(urls_list)

for index, url in enumerate(urls_list, start=1):
    print(f"{index}. {url}")

user_input = int(input("Please select a number corresponding to the website you would like to access: "))

if 0 <= user_input <= len(urls_list):
    selected_url_key = urls_list[user_input]
    url = urls_dict[selected_url_key]
    print(f"You have chosen {user_input}, {selected_url_key}")
    print(url)


def check_url_accessibility():
    """
    Checks whether the selected url is accessible for scraping
    """    
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





