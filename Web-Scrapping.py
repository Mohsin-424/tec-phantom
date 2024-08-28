import requests
import bs4
import requests


# result = requests.get('https://mohsin-424.github.io/ee/')
result = requests.get('https://creativecommons.org/')
print(type(result))
print(result)
sop = bs4.BeautifulSoup(result.text , "lxml")
print(sop)

# site_para = sop.select('p')
# site_para = sop.select('div')
# site_para = sop.select('.description')
# site_para = sop.select('.skip-to-content')
site_para = sop.select('footer')
print(site_para)

# site_para[1].get_text()



# # Web Scrapping in Python 
# import requests
# import bs4
# # Send a GET request to the website URL
# result = requests.get('https://creativecommons.org/')
# # Check if the request was successful
# if result.status_code == 200:
#     # Parse the response text using BeautifulSoup
#     sop = bs4.BeautifulSoup(result.text, "lxml")
#     # Select specific elements using CSS selectors
#     site_title = sop.select_one('h1.site-title').get_text()
#     site_description = sop.select_one('p.site-description').get_text()
#     license_types = sop.select('div.license-type-icon')
#     # Extract license type information
#     licenses = []
#     for license_type in license_types:
#         license_name = license_type.select_one('h3').get_text()
#         license_description = license_type.select_one('p').get_text()
#         licenses.append({'name': license_name, 'description': license_description})

#     # Print the scraped data
#     print("Site Title:", site_title)
#     print("Site Description:", site_description)
#     print("License Types:")
#     for license in licenses:
#         print(f"Name: {license['name']}")
#         print(f"Description: {license['description']}")
# else:
#     print(f"Failed to fetch the website. Status code: {result.status_code}")

