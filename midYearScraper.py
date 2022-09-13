
import requests as req
from bs4 import BeautifulSoup as bs
from residencyList import residency_number
from residencyCredentials import payload, header
import pandas as pd

#for x in residency_number:
#   sh root@45.79.52.207print(x)
#print(residency_number)

html_doc = "https://www.accp.com/resandfel/profile.aspx?mode=view&rid=7205"

res = req.get(html_doc, data = payload, headers = header, allow_redirects=True)
print(res)
print("--")

soup = bs(res.content,'html.parser')
#print(soup.text)

Content = soup.find(id="tblOther")

Content_header = soup.find(id="ctl00_master_body_lblHeader")
header_text = Content_header.text

Content_h4 = Content.find_all("h4")
h4_text = []
for i in Content_h4:
    h4_text.append(i.text)

Content_span = Content.find_all("span")
span_text = []
for i in Content_span:
    span_text.append(i.text)
 
print(header_text)
#for i in range(0,len(Content_h4)):
    #print(h4_text[i])
    #print(span_text[i])
    #print('---')

residency_dict = dict(zip(h4_text, span_text))
#print(residency_dict)

#for key, value in residency_dict.items():
#        print(key, ' : ', value)

print('$$$$$$$$$$$$$$$$$$$$$')

df = pd.DataFrame.from_dict([residency_dict], orient = "columns")
print(df)
#print(df.info())

#print(df['Type of Program'])
#print(df['Region'])
#print(df['Institution'])

#print('$$$$$$$$$$$$$$$$$$$$$')
df2 = pd.DataFrame.from_dict([residency_dict], orient = "columns")
df2.append(span_text)
print(df2)
#print(df.info())





