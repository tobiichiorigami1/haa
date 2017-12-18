import requests
from bs4 import BeautifulSoup
def getHTMLTEXT(url,headers):
    r=requests.get(url,headers)
    try:
        print(r.raise_for_status())
        r.encoding = r.apparent_encoding
        html=r.text
        return html
    except:
        return ""
def main():
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"}
    url="http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E9%95%BF%E6%B2%99%2B%E6%A0%AA%E6%B4%B2%2B%E6%B9%98%E6%BD%AD&kw=java&sm=0&isfilter=1&p=1"
    html=getHTMLTEXT(url,headers)
    print(html[:100])
main()
