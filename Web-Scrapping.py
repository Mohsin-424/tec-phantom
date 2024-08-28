import requests
import bs4
import requests


result = requests.get('https://mohsin-424.github.io/ee/')
print(type(result))
print(result)
sop = bs4.BeautifulSoup(result.text , "lxml")
print(sop)

site_para = sop.select('p')
print(site_para)

site_para[0].get_text()
