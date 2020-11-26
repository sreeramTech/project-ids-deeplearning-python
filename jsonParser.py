import json
def jsonParser(filename):
        json_list = []
        raw_hash = {}
        keys = ['clientHeaderHash','serverHeaderHash','ja3','ja3s','hassh','hasshServer']
        with open(filename) as f:
                for jsonObj in f:
                        jsonDict = json.loads(jsonObj)
                        json_list.append(jsonDict)

       
        
        for j in json_list:
            properties = []
            source_ip = j['sourceIp']
            properties.append(source_ip) 
            source_port = j['sourcePort']
            properties.append(source_port) 
            
            prop = ['userAgent']
            for k in j[j['protocol']].keys():
                if k in prop:
                    properties.append(j[j['protocol']][k])
                if k in keys:
                    h = j[j['protocol']][k]
                    raw_hash[h] = properties 
            

            



        #hash = list(hash_set)
        return raw_hash


