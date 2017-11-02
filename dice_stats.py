run = 1
print("""Enter a dice roll in the form of XdY(+N), where X is number of dice,
      Y is number of faces and N is an optional flat value to add""")
print("To quit, enter 'q'")

while(run == 1):
  print("Enter a dice roll:")
  command = input()

  if(command == "q"):
    run = 0
    break
  
  # split the string
  split_command = command.split("d")
  split_command2 = split_command[1].split("+")
  
  if(len(split_command2) > 1): add = int(split_command2[1])
  else: add = 0

  num_dice = int(split_command[0])
  num_faces = int(split_command2[0])
  

  #calculate min roll
  print("Min: ", num_dice + add)
  
  #calculate average
  avg = num_dice * (num_faces + 1) / 2 + add
  print("Average:", avg)

  #calculate max
  print("Max: ", num_dice * num_faces + add)
