import json 

with open("data.json","r")as file:
    data=json.load(file)

data["username"] = "bharat"
data["skills"].append("flask")

with open("data.json",'w') as file:
    json.dump(data,file,indent=4)


import json
student = {
    "name": "Narasimha",
    "age": 22,
    "course":"python"
}
json_data = json.dumps(student)
print(json_data)

student = json.loads(json_data)
print(student)
print(type(student))