import json

# JSON string to dictionary
json_string = '{"name": "Alice", "age": 25, "city": "New York"}'
dictionary = json.loads(json_string)
print("Nimi: ", dictionary["name"])

# Dictionary to JSON string
ransukoira = {} # luodaan tyhjä sanakirja
ransukoira["nimi"] = "Ransu"
ransukoira["ika"] = 5
ransukoira["rotu"] = "Karvakuono"
ransukoira["kaverit"] = ["Eno-Elmeri", "Riku"] # lista
json_result = json.dumps(ransukoira, indent=4)
print(json_result)