from requests_html import HTML
with open("index.html") as f:
    content=f.read()
    html=HTML(html=content)
    # print(html.html)
    html.render()
    print(html.find("h2", first=True).html)

