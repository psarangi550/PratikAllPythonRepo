text_to_search="""
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""
import re
pattern=re.compile(r"M(r|s|rs)+[\W\s]*[\W\s]*[a-zA-Z0-9]*")
matcher=pattern.finditer(text_to_search,re.V)
for match in matcher:
    print(match)