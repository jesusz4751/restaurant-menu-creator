import json
import sys

with open("data/default_restaurants.json", "r") as file:
  default_res = json.load(file)
with open("data/user_restaurants.json", "r") as file:
  user_res = json.load(file)
print("Hello, and welcome to the restaurant menu program! This program allows you to view restaurants as well as update your own restaurant menu.")
acc_selection = input("To start, please indicate if you are a restaurant owner (r) or a customer (c): ").lower()
valid_ans = ["r","c"]
while acc_selection not in valid_ans:
  acc_selection = input("Please enter a valid response: ").lower()
if acc_selection == "r":
  print(f"You currently have {len(user_res['restaurants'])} custom restaurants." )
  if len(user_res["restaurants"]) > 0:
    user_selection = input("Would you like to add (a), modify (m), or delete (d) an existing restaurant: ").lower()
    valid_ans = ["a", "m", "d"]
    while user_selection not in valid_ans:
      user_selection = input("Please enter a valid response: ").lower()
  else:
    user_selection = "a"
  if user_selection == "a":
    restaurant = {}
    restaurant["name"] = input("Enter a restaurant name: ")
    restaurant["items"] = []
  else:
    print("Here are all the currently created restaurants:")
    for i, res in enumerate(user_res["restaurants"]):
      print(f"{i+1}. {res['name']}")
    # User selects delete
    if user_selection == "d":
      try:
        del_res = int(input("Please enter a restaurant number to delete: ")) - 1
      except ValueError:
        print("Invalid number")
        del_res = -1
      while True:
        if del_res < 0 or del_res >= len(user_res["restaurants"]):
          try:
            del_res = int(input("Please select a valid restaurant: ")) - 1
          except ValueError:
            print("Invalid number")
        else:
          break
      user_res["restaurants"].pop(del_res)
      with open("data/user_restaurants.json", "w") as file:
        json.dump(user_res,file,indent=2)
      sys.exit("Thank you for using the progam, we hope to see you again soon!")
    # User selects modify
    else:
      try:
        mod_res = int(input("Please enter a restaurant number to modify: ")) - 1
      except ValueError:
        print("Invalid number")
        mod_res = -1
      while True:
        if mod_res < 0 or mod_res >= len(user_res["restaurants"]):
          try:
            mod_res = int(input("Please select a valid restaurant: ")) - 1
          except ValueError:
            print("Invalid number")
        else:
          break
      restaurant = user_res["restaurants"][mod_res]
  while True:
    if len(restaurant["items"]) > 0:
      user_selection = input("Would you like to add (a) or delete (d) an item from the restaurant? ").lower()
      valid_ans = ["a","d"]
      while user_selection not in valid_ans:
        user_selection = input("Please enter a valid input ").lower()
    else:
      user_selection = "a"
    if user_selection == "a":
      item_name = input("What is the name of the food item? ")
      while True:
        try:
          item_price = float(input("How much does this cost? "))
          break
        except ValueError:
          print("Invalid number")
          continue
      while True:
        try:
          item_calories = int(input("How many calories does this have? "))
          break
        except ValueError:
          print("Invalid number")
          continue
      restaurant["items"].append({"name": item_name, "price": item_price, "calories": item_calories})
    else:
      for i, item in enumerate(restaurant["items"]):
        print(f"{i+1}. {item['name']}")
      try:
        del_res = int(input("Please select an item to remove: ")) - 1
      except ValueError:
        print("Invalid number")
        del_res = -1
      while True:
        if del_res < 0 or del_res >= len(restaurant["items"]):
          try:
            del_res = int(input("Please select a valid item: ")) - 1
          except ValueError:
            print("Invalid number")
        else:
          break
      restaurant["items"].pop(del_res)
    # Create an array of all restaurant names
    names = [r["name"] for r in user_res["restaurants"]]
    # If restaurant already created, modify it
    if restaurant["name"] in names:
        idx = names.index(restaurant["name"])
        user_res["restaurants"][idx] = restaurant
    # If not, add to array as new restaurant
    else:
        user_res["restaurants"].append(restaurant)
    user_selection = input("Would you like to make another restaurant change? (y/n) ").lower()
    valid_ans = ["y","n"]
    while user_selection not in valid_ans:
      user_selection = input("please enter a valid response: ").lower()
    if user_selection == "n":
      with open("data/user_restaurants.json", "w") as file:
        json.dump(user_res,file,indent=2)
      sys.exit("Thank you for using the progam, we hope to see you again soon!")
else:
  # Future work
  print("customer")