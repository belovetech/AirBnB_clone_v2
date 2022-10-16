#!/usr/bin/python3

obj = {
    "name": "Abeeb",
    "Age": 12
}

print(obj)

if "Age" in obj.keys():
    del obj["Age"]

print(obj)