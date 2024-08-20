thisdict = {
            "name":"Mohsin",
            "age":20,
            "city":"Karachi",
            "hobbies":["reading","playing cricket"],
            "address": {
                "street":"2nd Street",
                "city":"Karachi",
                "country":"Pakistan"
                       },
            "family": [
                {"name":"Father", "age":45},
                {"name":"Mother", "age":40},
                {"name":"Brother", "age":35},
                {"name":"Sister", "age":30}
                ]
            }

# print(thisdict)
# print(thisdict['address'])

# print(thisdict['hobbies'])

# Changing values on dictionary

# thisdict['first name '] = 'Muhammad Mohsin'
# print(thisdict)
# print(len(thisdict))
# print((thisdict.keys()))
# print((thisdict.values()))
# x = thisdict.get('name')
# x = thisdict.get('hobbies')
# # thisdict.update({'name':"test name"})
# print(x)

# print((thisdict.items()))
# print((thisdict.values()))
# print((thisdict.keys()))


# Nested Dictionary 
dict = {
    "dict1": {"name":"Muhammad Mohsin" , 
              "age":30
    },
    "dict2": {"hobbies":["reading","playing cricket"] ,
              
               
              "gender": "Male"
    },
    "dict3": {"family":  [
                {"name":"Father", "age":45},
                {"name":"Mother", "age":40},
                {"name":"Brother", "age":35},
                {"name":"Sister", "age":30}
                ] ,
              
               
              "caste": "Rajput"
    },

}

# print(dict)
# print(dict["dict1"])
# dict["dict1"]['name'] = 'Ashutsh Khan'
# print(dict["dict1"])
print(dict.copy())

# Primitive types vs non-primitive types

list_var = [1, 2, 3, 4, 5]
print(list_var)


