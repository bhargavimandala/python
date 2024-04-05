### get pull requests information on a repo using python ###
### first need to install request module using pip - pip install request ###
import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
#print(response.json())
full_details = response.json()
for i in range(len(full_details)):
    print(full_details[i]["user"]["login"])