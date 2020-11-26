import os
import jsonParser
import requests
from time import sleep 
fp = open("trainingSet/trainingDataset.text","a")
# requests setup
requests.urllib3.disable_warnings()
client =  requests.session()
client.verify = False

apikey = '7d8b77586ddb8f5f75dab26184107087e82d72b142e45597407b773a54ea0d96'
def find(hash):
    get_hash_report(apikey,hash)

def get_hash_report(apikey,filehash):
	url = 'https://www.virustotal.com/vtapi/v2/file/report'
	params = {"apikey" : apikey, "resource" : filehash }
	r = client.get(url,params=params)
	if r.status_code == 200:
		response = r.json()
		parse_hash_report(response,filehash) 
def parse_hash_report(response,filehash):
	code = response['response_code']
	if code == 0:
		return 0
	else:
		return 1
