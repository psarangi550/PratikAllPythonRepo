import re #impiorting re module
pattern=re.compile(r"(0|\+91|91)?[6-9]\d{9}")
with open("input.txt") as f:
    content=f.read()
    matcher=pattern.finditer(content)
    for match in matcher:
        print(match.group(0))