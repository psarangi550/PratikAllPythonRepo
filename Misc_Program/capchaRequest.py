import requests
import json
client_key="6LcdsUYcAAAAANOCLx9y_ueHZtScqL2_GZByF1Vz"
server_key="6LcdsUYcAAAAACda8x2QWtP6bEXbkWMwnr63N76A"
data={
        "secret":server_key,
        "response":client_key
    }
resp=requests.post("https://www.google.com/recaptcha/api/siteverify",data=data)
my_dict=resp.json()
print(my_dict)