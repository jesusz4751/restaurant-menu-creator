import json
import sys

# Open appropriate json files
with open("data/default_restaurants.json", "r", encoding="utf-8") as file:
  default_res = json.load(file)
with open("data/user_restaurants.json", "r", encoding="utf-8") as file:
  user_res = json.load(file)
print("Hello, and welcome to the restaurant menu program! This program allows you to view restaurants as well as update your own restaurant menu.")
acc_selection = input("To start, please indicate if you are a restaurant owner (r) or a customer (c): ").lower().strip()
valid_ans = ["r","c"]
# Make sure user inputs valid answer
while acc_selection not in valid_ans:
  acc_selection = input("Please enter a valid response: ").lower().strip()
# Start of restaurant code
if acc_selection == "r":
  print(f"You currently have {len(user_res['restaurants'])} custom restaurants." )
  if len(user_res["restaurants"]) > 0:
    user_selection = input("Would you like to add (a), modify (m), or delete (d) an existing restaurant: ").lower().strip()
    valid_ans = ["a", "m", "d"]
    while user_selection not in valid_ans:
      user_selection = input("Please enter a valid response: ").lower().strip()
  # If there are no restaurants, automatically create a new one
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
        # Repeat until valid input is entered
        if del_res < 0 or del_res >= len(user_res["restaurants"]):
          try:
            del_res = int(input("Please select a valid restaurant: ")) - 1
          except ValueError:
            print("Invalid number")
        else:
          break
      # Save result on json file
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
  # User has selected either add or modify restaurant
  while True:
    # If there is more than one item in restaurant, give options to user
    if len(restaurant["items"]) > 0:
      user_selection = input("Would you like to view the menu (v), add (a), or delete (d) an item from the restaurant? ").lower().strip()
      valid_ans = ["v","a","d"]
      while user_selection not in valid_ans:
        user_selection = input("Please enter a valid input ").lower().strip()
    # If there are no items, default to add item
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
    # Print every item in the menu
    elif user_selection == "v":
      for i, item in enumerate(restaurant["items"]):
        print(f"{i+1}. Name: {item['name']}, Calories: {item['calories']}, Price: ${item['price']:.2f}")
    else:
      for i, item in enumerate(restaurant["items"]):
        print(f"{i+1}. {item['name']}")
      try:
        del_res = int(input("Please select an item to remove: ")) - 1
      except ValueError:
        print("Invalid number")
        del_res = -1
      while True:
        # Ensure valid input
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
    user_selection = input("Would you like to make another restaurant change? (y/n) ").lower().strip()
    valid_ans = ["y","n"]
    while user_selection not in valid_ans:
      user_selection = input("please enter a valid response: ").lower().strip()
    if user_selection == "n":
      with open("data/user_restaurants.json", "w") as file:
        json.dump(user_res,file,indent=2)
      sys.exit("Thank you for using the progam, we hope to see you again soon!")
else: # Start of customer code
  restaurant_arr = default_res["restaurants"] + user_res["restaurants"]
  print("Here are all the restaurants available: ")
  for i, restaurant in enumerate(restaurant_arr):
    print(f"{i+1}. {restaurant['name']}")
  while True:
    # Ensure valid input
    try:
      user_selection = int(input("please select a restaurant to view: "))-1
      if user_selection < 0 or user_selection >= len(restaurant_arr):
        print("Invalid restaurant")
        continue
      restaurant = restaurant_arr[user_selection]
      if len(restaurant["items"]) == 0:
        print("This restaurant has no items, please select another one.")
        continue
      break
    except ValueError:
      print("Invalid number")
      continue
  while True:
    print(f"Current restaurant: {restaurant['name']}")
    user_selection = input("Would you like to view the menu (v), create a plate (c), or exit (e)? ").lower().strip()
    valid_ans = ["v", "c", "e"]
    while user_selection not in valid_ans:
      user_selection = input("Please select a valid answer").lower().strip()
    # View menu
    if user_selection == "v":
      for i, item in enumerate(restaurant["items"]):
        print(f"{i+1}. Name: {item['name']}, Calories: {item['calories']}, Price: ${item['price']:.2f}")
    # Create plate
    elif user_selection == "c":
      plate = []
      while True:
        print("Here are all of the available dishes: ")
        for i, item in enumerate(restaurant["items"]):
          print(f"{i+1}. Name: {item['name']}, Calories: {item['calories']}, Price: ${item['price']:.2f}")
        try:
          user_selection = int(input("Please select a food item to add to your plate: "))-1
          if user_selection < 0 or user_selection >= len(restaurant['items']):
            print("Invalid number")
            continue
        except ValueError:
          print("Invalid number")
          continue
        plate.append(restaurant["items"][user_selection])
        user_selection = input("Would you like to add another item to your plate? (y/n) ").lower().strip()
        valid_ans = ["y", "n"]
        while user_selection not in valid_ans:
          user_selection = input("Please select a valid option. ").lower().strip()
        if user_selection == "n":
          break
      # Print out results of plate to user
      print("Here are the items on your plate:")
      total_cost = 0.0
      total_calories = 0
      for i, item in enumerate(plate):
        print(f"{i+1}. {item['name']}")
        total_cost += item['price']
        total_calories += item['calories']
      print(f"Your total cost is ${total_cost:.2f} with {total_calories} calories.")
    # Exit program
    else:
      sys.exit("Thank you for using the progam, we hope to see you again soon!")