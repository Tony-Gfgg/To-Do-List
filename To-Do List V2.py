list = []
while True:
 action = input("Insert action: ")
 if action == "view":
  if len(list) == 0:
   print("No items in list!")
  else:
   for item in list:
    print("- ", item)
 elif action == "add":
  addeditem = input("What to add: ")
  list.append(addeditem)
 elif action == "remove":
  removeindex = int(input("Removed item index: ")) - 1
  list.pop(removeindex)
 elif action == "edit":
  editindex = int(input("Item to edit index: ")) - 1
  newtextinput = input("Text to replace item: ")
  list[editindex] = newtextinput
 elif action == "reset":
  list = []
 else:
  print("Unknown Action!")