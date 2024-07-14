import re
#using regular expression (REG-EX): creates a DESCRIPTION of an expression to compare to
def is_palindrome(words):
  #define variables
  # return booleans (True or False, can return boolean expressions themselves!)
  # get rid of punctuation and whitespace

  # first, take the words input and 'find all' alphabetic symbols and then make all of them lowercase
  forwards = ''.join(re.findall(r'[a-z]+', words.lower()))

  # second, take the string, forwards, and reverse the order of the chars
  # (first-->last, second-->second last, ...)
  backwards = forwards[::-1]
  return forwards == backwards # if true, then 'return True' (and vice versa)


# commands used in solution video for reference
if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
    print(is_palindrome("This is not a plaindrome, lol 12345"))   # false, my test case***
