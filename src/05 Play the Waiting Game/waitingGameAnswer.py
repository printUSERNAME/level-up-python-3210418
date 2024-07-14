import time as t
def waiting_game():
  #define your variables
  target = 7 #seconds, get close to guessing this number of seconds
  print("Your target time is " + target + " seconds. Good luck!")
  print("Press ENTER to begin!")
  #once ENTER is pressed, timer begins, timer stops after ENTER is pressed again
  #make a conditional where closer and further guesses ellicit different responses (print)
  #we can use the sleep funciton
  t.sleep(1)  #program sleeps for 1 second




  # commands used in solution video for reference
if __name__ == '__main__':
    waiting_game()
