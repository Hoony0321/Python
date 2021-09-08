import json

tempList = [1,2,3,4,5,6]

jsonObj = json.dumps(tempList)

jsonReturn = json.loads(jsonObj)

print(type(jsonReturn))

if 1 in jsonReturn:
    