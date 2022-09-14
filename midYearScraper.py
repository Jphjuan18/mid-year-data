
import requests as req
from bs4 import BeautifulSoup as bs
from residencyList import residency_number, fellowship_number
from residencyCredentials import payload, header
import pandas as pd
import time
import random

html_doc = f"https://www.accp.com/resandfel/profile.aspx?mode=view&rid={9550}" # Residency: 4514 Fellowship: 9550


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

residency_dict = dict(zip(h4_text, span_text))
    
df = pd.DataFrame.from_dict([residency_dict], orient = "columns")

#for r_number in residency_number: #for residency
for r_number in fellowship_number: #for fellowships
    print(r_number)

    num = random.randrange(0,10)
    time.sleep(num)
    

    html_doc = f"https://www.accp.com/resandfel/profile.aspx?mode=view&rid={r_number}"

    res = req.get(html_doc, data = payload, headers = header, allow_redirects=True)
    #print(res)
    #print("--")

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

    residency_dict = dict(zip(h4_text, span_text))
          
    #print('$$$$$$$$$$$$$$$$$$$$$')           
    df.loc[len(df.index)] = residency_dict.values()        
        
print(df)

#df.to_csv("midYearFellowship.csv") 
df.to_csv("midYearFellowship.csv") 
        # Rerun loop for second iteration

