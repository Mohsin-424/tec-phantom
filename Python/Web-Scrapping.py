import requests
import bs4




result = requests.get('https://mohsin-424.github.io/ee/')
# result = requests.get('https://www.zameen.com/')
# # result = requests.get('https://x.com/?mx=2')
# # # result = requests.get('https://creativecommons.org/')
# # # result = requests.get('https://sci-hub.se/')
# # # result = requests.get('https://moviesmod.monster/')
# # # result = requests.get('https://github.com/Mohsin-424')
# # result = requests.get('https://en.wikipedia.org/wiki/Elon_Musk')
# # # result = requests.get('https://medium.com/geekculture/web-scraping-with-python-a-complete-step-by-step-guide-code-5174e52340ea')

# print(type(result))
print(result)
sop = bs4.BeautifulSoup(result.text , "lxml")
sop = bs4.BeautifulSoup(result.text , "html.parser")
print(sop.findAll('div'))

site_para = sop.select('p')
# # site_para = sop.select('div')
# # site_para = sop.select('.description')
# # site_para = sop.select('.skip-to-content')
# # site_para = sop.select('footer')
# site_para = sop.select('header')
# site_para = type(sop.select('header'))
print(site_para)



# for item in sop.select('header'):
#     print(item.text)


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




# import csv
# # data to be saved
# data = [
# ['Jay', 'Dominic', 25],
# ['Justin', 'Seam', 30],
# ['Bob', 'Lans', 40]
# ]
# # open a file for writing
# with open('data.csv', mode='w', newline='') as file:
# # create a csv writer object
#             writer = csv.writer(file)
# # write the data to the file
# writer.writerows(data)





# ..................... Image Scraping ................................



# import requests
# from bs4 import BeautifulSoup

# # URL of the webpage
# url = "https://miro.medium.com/v2/resize:fit:786/format:webp/0*VvjoRJ5cfWtmATBt.jpg"

# # Send a GET request to the webpage
# response = requests.get(url)

# # Parse the HTML content of the webpage using BeautifulSoup
# soup = BeautifulSoup(response.text, "html.parser")

# # Find the image element in the HTML (e.g., using CSS selector or attribute)
# image_element = soup.select_one("img")

# # Extract the image URL from the image element
# image_url = image_element["src"]

# # Send a GET request to the image URL to download the image
# image_response = requests.get(image_url)

# # Save the downloaded image to a file
# with open("image.jpg", "wb") as file:
#     file.write(image_response.content)





# # res = requests.get("https://miro.medium.com/v2/resize:fit:786/format:webp/0*VvjoRJ5cfWtmATBt.jpg")
# res = requests.get("https://avatars.githubusercontent.com/u/129749023?v=4")
# res = requests.get("https://www.zameen.com/")


# soup = bs4.BeautifulSoup(res.text , "lxml")
# print(soup)
