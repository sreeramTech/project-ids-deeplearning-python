import os
import jsonParser
import requests
from time import sleep 
not_threat = []
fp = open("trainingSet/trainingDataset.text","a")
'''pcap_command = 'python3 fatt/fatt.py -r fatt/testbed.pcap -j'
fatt = os.system(pcap_command)
if fatt == 1:
	print("command didn't execute successfully")
	exit(1)
sleep(10)'''
# requests setup
requests.urllib3.disable_warnings()
client =  requests.session()
client.verify = False

apikey = '7d8b77586ddb8f5f75dab26184107087e82d72b142e45597407b773a54ea0d96'

def get_hash_report(apikey,filehash,hashes):
	h = hashes
	url = 'https://www.virustotal.com/vtapi/v2/file/report'
	params = {"apikey" : apikey, "resource" : filehash }
	r = client.get(url,params=params) 

	
	if  r.status_code ==   204:
		print("Rate-limit reached waitig for 60sec secondes\n")
		sleep(60)
		get_hash_report(apikey,filehash,hashes)
	elif r.status_code != 200:
		print("Program terminated due to unforeseen error\n")
		exit(1)
	elif r.status_code == 200:
		response = r.json()
		parse_hash_report(response,filehash,h) 
def parse_hash_report(response,filehash,hashes):
	code = response['response_code']
	if code == 0:
		not_threat.append(hashes[filehash])
	else:
		fp.write(filehash)
		print(hashes[filehash])

hashes = jsonParser.jsonParser('fatt.log')
for  hash in hashes:
	get_hash_report(apikey,hash,hashes)







