import requests
from bs4 import BeautifulSoup


soup = BeautifulSoup(
    requests.get("https://medium.com/featurepreneur").content,
    "html.parser")
    
count=0
section=soup.find_all('div',class_='postMetaInline postMetaInline-authorLockup ui-captionStrong u-flex1 u-noWrapWithEllipsis')

for sec in section:
    headline= sec.get_text()
    print(headline)
    count=count+1

print()
print("Number of Articles : ",count)


