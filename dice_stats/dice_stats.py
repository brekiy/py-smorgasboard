import re

run = 1
print("""Enter a dice roll in the form of XdY(+N)("D"),
where X is number of dice, Y is number of faces,
N is an optional flat value to add and "D" means drop the lowest""")
print("To quit, enter 'q'")

while(run == 1):
  print("Enter a dice roll:")
  command = input()

  if(command == "q"):
    run = 0
    break
  
  # split the string
  # get the digits for X, then digits for Y, then +N (optional) then D (optional)
  match = re.match('(\d+)d(\d+)\+?(\d+)?(D)?', command)
  num_dice = int(match.group(1))
  num_faces = int(match.group(2))
  if match.group(3): flat = int(match.group(3))
  else: flat = 0
  if match.group(4): drop = 1
  else: drop = 0
  print(num_dice)
  print(num_faces)
  print(flat)
  print(drop)
  
  #calculate min roll
  print("Min: ", (num_dice - drop) + flat)
  
  #calculate average
  if(drop == 0): avg = num_dice * (num_faces + 1) / 2 + flat
  else: 
    t_1 = (num_faces+1)*(num_dice/2)*(num_faces**num_dice)
    t_2 = 0
    for i in range(1,num_faces+1):
      t_2 += i*((num_faces-i+1)**(num_dice) - (num_faces-i)**(num_dice))
    avg = (t_1 - t_2) / (num_faces**num_dice)
  
  print("Average:", avg)

  #calculate max
  print("Max: ", (num_dice - drop) * num_faces + flat)
