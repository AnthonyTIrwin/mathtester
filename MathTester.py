import random
import csv
import datetime


# Function that starts the math assesment.   
def teststart():
  counter = 0

  while counter < questsize:

    testvaraone = rannumone()
    testvaratwo = rannumtwo()
    score = 0
 
  
    print("What's " + str(testvaratwo) + " plus " + str(testvaraone))
  
    answer = int(input("Answer: "))
  
    if answer == testvaraone + testvaratwo:
      print("Good Job!")
    score += 1
    counter += 1
    print("You have a score of " + str(score))
    wannasave = input("Do you want to save your score?").lower()
    if wannasave == "y":
      saveit(score)
    else: 
      print("Fine, then don't save it!")
  else:
      print("How shameful, try again!!")
      counter += 1

# Random Number Generator Functions

def rannumone():
  return int(random.randint(1,1000))

def rannumtwo():
  return int(random.randint(1, 1000))



# Saving the score and the name to .csv

def saveit(score):
  with open('scorecard.csv', 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    timewrite = 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    spamwriter.writerow([namez] + [score] + [timewrite])
   

    # Start Menu where user is asked to put in their name and ask whether or not they want to take the math challenge.  

namez = input(" Please enter your name:")

print("Welcome " + namez + " would you like to test your computational skills?")

wannaplay = input("Y/N?").lower()
if wannaplay == "y":
  questsize = int(input("How many questions do you want to answer?"))
  print(namez + "Lets Begin.")
  teststart()
else:
  print("Please feel free to start when you're ready")







    
