import re #importing the re module
url="""
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""
#here we want to fetcvh only google.com/coreyms.com like that
pattern=re.compile("https?://(www.)?(\w+)(\.\w)*")
matcher=pattern.finditer(url)
print(pattern.sub(r"\2\3",url))
# for match in matcher:
#     print(match)