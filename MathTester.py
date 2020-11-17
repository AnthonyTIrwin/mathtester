import random
import csv
import datetime

# function that creates random numbers from 1 to 1000 and asks user math problem.

def teststart():

  testvaraone = rannumone()
  testvaratwo = rannumtwo()
  score = 0
  
  print("What's " + str(testvaratwo) + " plus " + str(testvaraone))
  
  answer = int(input("Answer: "))
  
  if answer == testvaraone + testvaratwo:
    print("Good Job!")
    score += 1
    print("You have a score of " + str(score))
    wannasave = input("Do you want to save your score?").lower()
    if wannasave == "y":
      saveit(score)
    else: 
      print("Fine, then don't save it!")
  else:
      print("How shameful, try again!!")
# Random Number Generators
def rannumone():
  return int(random.randint(1,1000))

def rannumtwo():
  return int(random.randint(1, 1000))



# Saving the score and the name to .csv on a new line

def saveit(score):
  with open('scorecard.csv', 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    timewrite = 'Time: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    spamwriter.writerow([namez] + [score] + [timewrite])
   

    # Start Menu where user is asked to put in their name and ask whether or not they want to take the math challenge.  

namez = input(" Please enter your name:")

print("Welcome " + namez + " would you like to test your computational skills?")

wannaplay = input("Y/N?").lower()
if wannaplay == "y":
  print(namez + " lets Begin!")
  teststart()
else:
  print("Please feel free to start when you're ready")






    
