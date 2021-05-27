import requests
from bs4 import BeautifulSoup

# soup = BeautifulSoup(
#     requests.get("https://medium.com/featurepreneur").content,
#     "html.parser")
    
# print(soup.prettify)
with open('medium-articles-list.html','r') as html_file:
    content =html_file.read()

    soup=BeautifulSoup(content,'lxml')
    # print(soup)

count =0

section=soup.find_all('h3',class_="post-title")

for sc in section:
    head=sc.get_text()
    # print(head)
    print(f'''
    Title: {head.replace(' ','')}
    ''')
    count=count+1
    print()


print("Total Number of Articles : ", count)



    





