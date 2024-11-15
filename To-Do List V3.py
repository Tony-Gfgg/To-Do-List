to_do_list = []
listingtype = 0
while True:
 action = input("Insert action: ")
 if action == "view":
  if len(to_do_list) == 0:
   print("No items in list!")
  else:
   if listingtype == 0:
    for item in to_do_list:
     print("- ", item)
   elif listingtype == 1:
    counter = 1
    for item in to_do_list:
     print(counter, " - ", item)
     counter += 1
 elif action == "add":
  addeditem = input("What to add: ")
  to_do_list.append(addeditem)
 elif action == "remove":
  removeindex = int(input("Removed item index: ")) - 1
  to_do_list.pop(removeindex)
 elif action == "edit":
  editindex = int(input("Item to edit index: ")) - 1
  newtextinput = input("Text to replace item: ")
  to_do_list[editindex] = newtextinput
 elif action == "reset":
  to_do_list = []
 elif action == "settings":
  listingtype = int(input("Listing type: "))
 else:
  print("Unknown Action!")