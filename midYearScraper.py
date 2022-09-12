import requests as req
from bs4 import BeautifulSoup as bs
from residencyList import residency_number
from residencyCredentials import payload, header

for x in residency_number:
    print(x)
#print(residency_number)

html_doc = "https://www.accp.com/resandfel/profile.aspx?mode=view&rid=7205"

res = req.get(html_doc, data = payload, headers = header, allow_redirects=True)
print(res)
print("--")

soup = bs(res.content,'html.parser')
#print(soup.text)

Content = soup.find(id="tblOther")
print(Content.text)
#print(Content)
#for element in Content:
 #   print(element.string)
#print(soup.prettify())

