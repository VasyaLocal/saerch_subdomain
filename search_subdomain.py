import requests


url = input("Enter url website:")
print("[+]Search subdomains:" + url)

def subdomain_search(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

with open("subdomain.txt", "r") as subdomainlist:
    for line in subdomainlist:
        subdomainlist = line.strip()
        subdomain = subdomainlist + "." + url
        response = subdomain_search(subdomain)
        if response:
            print("Descovered subdomain-->" + subdomain)
open("savesubdomain.txt", "w+")
