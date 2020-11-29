import json

## Simple serialization
# data = {
#     "president": {
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgeusian"
#     }
# }

# with open("data_file.json", "w") as write_file:
#     json.dump(data, write_file)
# #  continue using this serialized JSON data in your program,
# # you could write it to a native Python str object.
# json_string = json.dumps(data)
# print(json_string)

## Simple deserialization example
with open("demo.json","r") as read_file:
    data = json.load(read_file)
    print(data)
    print(type(data))


