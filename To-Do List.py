list = []
while True:
 action = input("Insert action: ")
 if action == "view":
  print(list)
 elif action == "add":
  addeditem = input("What to add: ")
  list.append(addeditem)
 elif action == "remove":
  removeindex = int(input("Removed item index: ")) - 1
  list.pop(removeindex)