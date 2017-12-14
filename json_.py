#https://docs.python.org/3.3/library/json.html
#https://www.youtube.com/watch?v=pTT7HMqDnJw

import json

jsonfilename = "aboutme.json"

d = {}
d["name"]="Dmitriy"
d["LastName"]="Vlasov"
d["weigth"]=75
d["language"]="python"
d["isMale"]=True


with open(jsonfilename,"w",encoding="utf-8") as f:
	json.dump(d,f)

with open(jsonfilename,"r",encoding="utf-8") as f:
	d1= {}
	d1 = json.load(f)


print(d)
print(d1)

s2 = json.dumps(d1) #можно конвертнуть в строку
print(type(s2))

weird_json = '{"x": 1, "x": 2, "x": 3}'
print(json.loads(weird_json))




