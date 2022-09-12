import requests as req
from bs4 import BeautifulSoup as bs

payload = {"mode":"view","rid":"7205"}

header =  {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'ACCP_Modules_Bookstore_NEW_ShoppingCart=6%2bhpD%2bzoolSBF1%2fpX0BbTjfA1XM43QLuSenwF9en7W3R%2f1VS5dPObQ%3d%3d; sess_map=saytdbquxasztetyfetbeaqtwcrwtwaasaeuvvdvbdceezvqcefxeazwfzzarxvsfzxatsesufzrqsexfxbsbrfuacfsyxxcvsqustvqcyvttcecyfdswzsysevuzfxvbzqcbvqeqyrwurvyercaebywqzedddfv; _gid=GA1.2.713371975.1663010843; __utma=95587596.1196277446.1663010843.1663010844.1663010844.1; __utmc=95587596; __utmz=95587596.1663010844.1.1.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _sp_ses.6c31=*; ASP.NET_SessionId=ebjviad1rtqcp5fczvt1pw4m; cookieFooter=WwMkTPawge5kqzhCi91GSviITWb8UO8%2b9hR11%2bF7uNFwGULn2qcERw%3d%3d; _ga=GA1.2.1196277446.1663010843; __utmt=1; __utmb=95587596.7.10.1663010844; _ga_JRMCBWT0P2=GS1.1.1663010843.1.1.1663011687.0.0.0; _sp_id.6c31=568e178a19e8768d.1663010844.1.1663011717.1663010844.70f352bf-6e41-487b-8dde-88c5fa054d54',
'Host': 'www.accp.com',
'Referer': 'https://www.accp.com/resandfel/search.asp',
'sec-ch-ua': '"Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
}

html_doc = "https://www.accp.com/resandfel/profile.aspx?mode=view&rid=7205"
#html_doc = "https://accreditation.ashp.org/directory/#/program/residency/programInfo/63010"
#html_doc = "https://accreditation.ashp.org/api/ashp/rest/directoryInfo/filterSearch"

res = req.get(html_doc, data = payload, headers = header, allow_redirects=True)
#res = req.get(html_doc)
print(res)

print("--")
soup = bs(res.content,'html.parser')
#print(soup.text)

Content = soup.find(id="tblOther")
print(Content)
#for element in Content:
 #   print(element.string)
#print(soup.prettify())

