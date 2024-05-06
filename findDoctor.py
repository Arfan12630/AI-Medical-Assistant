from bs4 import BeautifulSoup
import requests
url = "https://www.yelp.ca/search?find_desc=Bamiyan+Kabab&find_loc=Toronto%2C+ON"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")
divs = doc.find_all('a', class_='css-19v1rkv')
document = []
for div in divs[2:]:
    newDiv = div.text
    document.append(newDiv)
new_list =  [item for item in document if "Bamiyan Kabob" in item]
print(new_list) 
 # Since we got the test
 # now we can format
# formattedName = headingText.replace(" ", "-").lower()
# print(formattedName)