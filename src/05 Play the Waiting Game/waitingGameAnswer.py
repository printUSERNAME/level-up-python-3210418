import time as t
import random as r
def waiting_game():
  #define your variables
  target = r.randint(2,4) #target number of seconds is randomly chosen each time

  #tell the user what is going on
  print(f'Your target time is {target} seconds.\n')

  input("Press ENTER to begin!\n") #start counting here
  start = t.perf_counter()

  input(f'Press ENTER after {target} seconds...\n') #take the difference between ENTERs
  elapsed = t.perf_counter() - start

  print(f'Elapsed time: {elapsed :.3f}') #round to the nearest millisecond
  if target == elapsed:
    print("Unbelieveable!!! Right on the money!!!$$$")
  elif target < elapsed:
    print(f'You were {elapsed-target :.3f} seconds too slow. Try being faster next time!')
  else:
    print(f'You were {target-elapsed :.3f} seconds too fast! Slow down buddy!')



  # commands used in solution video for reference
if __name__ == '__main__':
    waiting_game()
