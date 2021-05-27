import requests
from bs4 import BeautifulSoup

# soup=BeautifulSoup(requests.get('https://medium.com/featurepreneur').content,
# 'lxml')

soup = BeautifulSoup(
    requests.get("https://medium.com/featurepreneur/latest").content,
    "html.parser")
    
# print(soup.prettify)

count =0

section=soup.find_all('div',class_="section-inner sectionLayout--insetColumn")

for sc in section:
    head=sc.get_text()
    print(head)
    count=count+1
    print(" ")

print("Number of Articles : ", count)



    





