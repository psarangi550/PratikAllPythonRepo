import re #importing re module
import urllib.request
list_of_sites=['https://jntuh.ac.in/contact-us#',
            'https://www.osmania.ac.in/aboutus-contactus.php',
            'https://cgu-odisha.ac.in/contact/',
            'https://www.driems.ac.in/driems-degree/contactus.php',]
pattern=re.compile(r"[a-zA-Z0-9.]+@[a-zA-Z0-9-]+[.]ac[.]in")
for site in list_of_sites:
    resp=urllib.request.urlopen(site)
    text=resp.read()
    stext=str(text)
    matcher=pattern.finditer(stext)
    set_matcher=set(matcher)
    for match in set_matcher:
        print(match.group(0))

