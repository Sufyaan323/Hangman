#Variable values
name = "Munasar"
lives = 3
guessed = []
correct = []
deny = False
x = 0
print("-"*len(name), end="")

#Check if lives is more than 0
while lives > 0:
  x = 0
  y = 0
  count = 0
  
  deny = False

  #Replace "-" with their correctly guessed letters counterpart
  while y < len(name):
    z = 0
    accept = True
    while z < len(correct):
      if name[y].lower() == correct[z].lower():
        print(correct[z], end="")
        accept = False
        count += 1
    
      z+=1

      if z == len(correct) and accept == True:
        print("-", end="")


    y+=1

  #check if the answer is found
  if count == len(name):
    print("\n***Congragulation, you have guessed the word correctly***")
    break


  #Get the user's guess
  print("\nPlease enter a letter: ")
  letter = str(input())
  
  #Only accept the input if it is 1 letter
  if len(letter) == 1 and letter.isalpha() == True:

    #check if the guess is correct and do not allow the user to guess the same letter again
    if letter.lower() in name.lower():
      while x < len(correct):
        if correct[x] == letter:
          deny = True
          print("The letter has already been guessed correctly")
          break
        x+= 1

      #Append the guessed letter to the "correct" list if it has not been guessed already
      if deny == False:
        correct.append(letter)
        print("\nWell done, continue!!!")

    #check if the guess is not correct and do not allow the user to guess the same letter again
    if letter.lower() not in name.lower():
      while x < len(guessed):
        if guessed[x] == letter:
          deny = True
          print("The letter has already been used")
          break
        x+= 1

      #Append the guessed letter to the "guessed" list if it has not been guessed already  and lose 1 life
      if deny == False:
        lives-=1
        print("\nYou have lost one life.")
        guessed.append(letter)

  #Deny the input if it is more or less than 1 letter and is not in the alphabet
  else:
    print("Please only enter 1 letter")

  #End the game if the user has no lives
  if lives == 0:
      print("Game over.")