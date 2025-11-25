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
  print(f"You currently have {len(user_res["restaurants"])} custom restaurants." )
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
  else:
    print("Here are all the currently created restaurants:")
    for i, res in enumerate(user_res["restaurants"]):
      print(f"{i+1}. {res["name"]}")
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
      print(restaurant["name"])
else:
  print("customer")