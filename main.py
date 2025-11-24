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
    for res in user_res["restaurants"]:
      print(res)
    if user_selection == "d":
      del_res = input("Please select a restaurant to delete: ")
      while del_res not in user_res["restaurants"]:
        del_res = input("Please select a valid restaurant: ")
      user_res["restaurants"].pop(del_res)
      # ADD CODE FOR SAVING TO JSON FILE
      sys.exit("Thank you for using the progam, we hope to see you again soon!")
else:
  print("customer")