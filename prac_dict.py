#creating a dictionaries
myClothes = {"type" : "skirt", "length" : "mini", "size" : 30}
print(myClothes)
print()

#accessing dictionary element
user_access = input("type a key: ")
cloth = myClothes.get(user_access)
print(f"The value of {user_access} is {cloth}")
print()

#Adding new key-value pairs
user_key = input("Add a key: ")
user_value = input("Add a value: ")
myClothes.update({user_key: user_value})
print(myClothes)
print()

#Removing elements
user_remove = input("What would you like to remove? ")
myClothes.pop(user_remove)
print(myClothes)
print()

#Dictionary length
dict_len = len(myClothes)
print(f"The length of the dictionary is = {dict_len}")
print()

#Update the value of an existing key
user_update = input("What would you like to change? ")
change_value = input("Enter a change value: ")
myClothes[user_update] = change_value
print(myClothes)
print()

#Iterate through a dictionary
for x, y in myClothes.items():
    print(x, ":", y)
print()

#Nested Dictionaries
footwear = { 
    "Sneakers" : {
        "brand": "Nike",
        "size": 2
    },
    "Sandals" : {
        "brand" : "Adidas",
        "size" : 5
    },
    "Boots" : {
        "brand" : "Dr. Martens",
        "size" : 3
    }
} 
print(footwear)
user_shoe = input("Which shoe would you like to view? ")
user_choice = input("What would you like to see about the shoe? ")
print(footwear[user_shoe][user_choice])