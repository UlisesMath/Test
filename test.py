import requests

headerDict = {"Authorization":"d1db3681-2d3bfab0-285745fe-785281a8"}

r = requests.get('https://fortniteapi.io/v1/lookup?username=G2 Jelty.', headers=headerDict)
#print(r)

jr = r.json()

print(jr["account_id"])

url = 'https://fortniteapi.io/v1/stats?account=' + jr["account_id"]

r2 = requests.get(url, headers=headerDict)

r2j = r2.json()

print(r2j['global_stats']['solo']['kd'])
