import re

def sort_words(input):
  # Separate words by spaces using the .split() funciton on the input
  words = input.split()
  # Append a .lower() copy to the front of the original words
  words = [w.lower() + w for w in words]
  # Alphabetize the funciton by using the .sort() function on words
  words.sort()
  # BELOW, we remove the .lower() half of each string by copying the string, starting at
  # the halfway point (length//2) and going to the end of the string (empty)
  words = [w[len(w)//2:] for w in words]
  return ' '.join(words)

# line 8 is very powerful, creating an array of strings, words,
# calling each string of letters w in the words array, and concatonating it with the lower
# in front of the original

# commands used in solution video for reference
if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))  # apple banana ORANGE
    print(sort_words('ape barn bahn AUTObannnn zebra Snuggles pear toothache WyaTT LAsTofUS')) 
    # ***my test*** (on the line ABOVE))
