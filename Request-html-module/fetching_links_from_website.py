from requests_html import HTMLSession
html=HTMLSession()
resp=html.get("https://coreyms.com/")
print(resp.html.links)#set of links if we try to fetch the links
# for link in resp.html.links:
#     print(link)
#for absolute link can be written as
# for link in resp.html.absolute_links:
#     print(link)
