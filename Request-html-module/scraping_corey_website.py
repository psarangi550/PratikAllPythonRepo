import requests_html #importing the request_html module
import csv #importing the csv module
from requests_html import HTMLSession #importing the HTML Session Class Using the request_html module
#creating the Object of HtmlSession Class as to hit httpRequest
html=HTMLSession()
#accessign the site by putting the get request
resp=html.get("https://coreyms.com/")
html_content=resp.html
# print(html_content)#object of HTML Class
articles=resp.html.find("article")
# print(article.html)
csv_file=open("Corey_web_1_scrapping.csv","w",newline="")
csv_writer=csv.writer(csv_file)
csv_writer.writerow(["HeadLine","Summary","Youtube_link"])
for article in articles:
    headline = article.find(".entry-title .entry-title-link", first=True).text
    print(headline)
    summary = article.find(".entry-content p", first=True).text
    print(summary)
    try:
        yt_video_link = article.find("iframe", first=True).attrs.get("src")
        # print(yt_video_link)
        yt_video_link = yt_video_link.split("/")[4]
        yt_video_link = yt_video_link.split("?")[0]
        # print(yt_video_link)
        yt_video_link = f"https://www.youtube.com/watch?v={yt_video_link}"
        print(yt_video_link)
        print()
        print()
    except:
        yt_video_link=None
    csv_writer.writerow([headline, summary, yt_video_link ])
csv_file.close()
