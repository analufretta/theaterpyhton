##Theater Python Program --> Program to purchase tickets from the montthly programm

#libraries
import datetime
import os

#variables
performances = ["Lost in repetition", "The poetics of surviving"]
ticket = 35.50 #ticket price
name = input("Type your name to start the program: ")

os.system("clear")

print("Hello, {0}, welcome to Theater Python!\n".format(name))

#Performance selection loop
while True:
  print("Which performance would you would like to purchase?\n")
  for x in range(len(performances)): #loop to print the whole varible performances
    print("{0}. {1}".format(x + 1, performances[x])) #Formating
  else:
    perf_question = int(input("\nType the option number you would like to purchase: "))

  if perf_question > len(performances) or perf_question < 1:
    print ("\nInvalid option. Try again.\n")
    input("Press any key to continue...")
    os.system("clear")
    continue
  else:
    print("\nYou chose to buy tickets for '{0}'".format(performances[perf_question-1]))

  while True:
    qtd = int(input("\nHow many tickets would you like to purchase?: ")) #quantity of tickets
    if qtd <= 5:
      print("\nThe total price is €", (qtd * ticket))
      break #Finish loop
    else:
      print("\nInvalid number. You can only buy a maximum of 5 tickets. Try again.")
  break

# date = ["Fri, 28 March", "Sat, 29 March", "Sun, 30 March"]

# #Date selection loop
# while True:
#   print("\nSelect the date fo your purchase\n")
#   print("1. ", date[0])
#   print("2. ", date[1])
#   print("3. ", date[2])

#   date_option = input("\nType the option number you would like to purchase: ")

#   if date_option == '1':
#     date_option = date[0]
#     break #Exit loop if input is valid

#   elif date_option == '2':
#     date_option = date[1]
#     break #Exit loop if input is valid

#   elif date_option == '3':
#     date_option = date[2]
#     break #Exit loop if input is valid

#   else:
#     print("\nInvalid option. Try again.\n")