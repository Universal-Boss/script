import json
import requests
from pprint import pprint

query = input("Enter your query here: ")
print("""
What do you want to see 
'content' to see ful content of search,
'page' to see discription, summary and related suggestions for your search,
'search' to see the list of related suggestion and thier their summary
""")
init = input("=> ").lower()

if init == "content":
    url = "https://wikipenapi.herokuapp.com/content/?q="
    result = json.loads(requests.get(url + query).text)

    result_content = result["page"]["content"]
    result_tittle = result["details"]["tittle"]
    print(f"**************** For tittle '{result_tittle}' content is ****************")
    print(result_content)

if init == "page":
    url = "https://wikipenapi.herokuapp.com/page/?q="
    result = json.loads(requests.get(url + query).text)

    result_details = result["details"]
    result_details_page_found = result_details["page found"]
    result_details_tittle = result_details["tittle"]
    result_details_url = result_details["url"]
    result_details_search = result_details["search"]

    if result_details_page_found == True:
        page_exists = f"exist with tittle '{result_details_tittle}'"
    else:
        page_exists = "does not exist"

    result_page = result["page"]
    result_page_summary = result_page["summary"]

    result_suggestion = result["suggestions"]
    other_suggestion_list = result_suggestion["other suggestions"]

    print(f"""
You search is '{result_details_search}', and a page {page_exists} at url '{result_details_url}' on internet.
""")

    pprint(result_page_summary)
    print("A few related suggestions for your search are:")
    for i in other_suggestion_list:
            print(i)

if init == "search":
    url = "https://wikipenapi.herokuapp.com/search/?q="
    result = json.loads(requests.get(url + query).text)

    result_search_related_suggestions = result["search related suggestions"]  # this return list
    for index, value in enumerate(result_search_related_suggestions):
        print(index, value)

    print("=" * 100)

    new = input("Do you want summary of the above contents('yes' or 'no'): ").lower()
    if new == "yes":
        num = int(input("Enter for how many suugestion you want to see summary: "))
        count = 0
        rel_list = []
        while count < num:
            index_rel = int(input("Enter the corresponding index of the related suggestion: "))
            rel_list.append(index_rel)
            count +=1
        print("=" * 100)

        for i in rel_list:
            query = result_search_related_suggestions[i]
            url = "https://wikipenapi.herokuapp.com/page/?q="
            result = json.loads(requests.get(url + query).text)
            result_page_summary = result["page"]["summary"]
            result_details_search = result["details"]["search"]
            pprint(f"*********** For search '{result_details_search}' is ***********")
            pprint(result_page_summary)
            print("=" * 100)

