import json
def parseIt(orig_quant=100,trgt_quant=23,json_path='data.json'):
    def parser(jData):
        for i in jData.keys():
            if i == 'quantity':
                jData[i] = jData[i] * trgt_quant/orig_quant
                #print(jData[i])
            elif type(jData[i]) is dict:
                parser(jData[i])
            elif type(jData[i]) is list:
                for each in jData[i]:
                    parser(each)
    with open(json_path) as jsonFile:
        json_data = json.load(jsonFile)
        parser(json_data)
        json.dump(json_data,open('result.json',mode='w'))
        print("result loaded in 'result.json' file")
                    
if __name__ == "__main__":
    parseIt()
                