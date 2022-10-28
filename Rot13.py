#==================================================
# Problem 0

# Reminder:  For the first 128 characters, ASCII and UTF-8 are the same and interchangeable.

# Write a function, encode_table(), that should print out
# each letter from a-z, along with its UTF-8 value, use one line per character.
# Each line should look like this:
#     a: 97
# The function does not need to return anything.

def encode_table(a):
    print(a, end = ""+ ':')
    print(ord(a))


print(('=' * 10) + "Problem 0" + ('=' * 10))
encode_table('h')
# End Problem 0
#==================================================

#==================================================
# Problem 1

# There is a cipher (https://en.wikipedia.org/wiki/Cipher) called rot13
# The following shows how to "encrypt" something in rot13:

# a b c d e f g h i j k l m n o p q r s t u v w x y z
# n o p q r s t u v w x y z a b c d e f g h i j k l m

# 'hello' in rot13 becomes 'uryyb'

# Look at the Unicode values from encode_table()
# what can you tell about a letter and its rot13 equivalent?
# print your answer as a string below

print(('=' * 10) + "Problem 1" + ('=' * 10))
answer = 'The letters are all shifted up 13 places from the uft-8 encoding. And when it gets to n, the 13th letter of the alphabet, it circles back and subtracts 13 instead.'
print(answer)

# End Problem 1
#==================================================

#==================================================
# Problem 2

# Write a function that takes a single character string
# as a parameter and returns its rot13 equivalent.
# If the character is not a lowercase letter then
# return the original character.
# for example rot13char("b") would return "o"

def rot13char(c):
    i = 0
    if c >= 'a' and c < 'n':
        i = ord(c) + 13
    elif c >= 'n' and c <= 'z':
        i = ord(c) - 13
    else:
        i = ord(c)
    c = chr(i)
    return c

print(('=' * 10) + "Problem 2" + ('=' * 10))
print( 'b: ' + rot13char('b') )
print( 'q: ' + rot13char('q') )
print( 'B: ' + rot13char('B') )
print( 'Q: ' + rot13char('Q') )
print( '?: ' + rot13char('?') )
print( '$: ' + rot13char('$') )

# End Problem 2
#==================================================


#==================================================
# Problem 3

# Write a function that prints out all the characters
# from 'a' to 'z' along with their rot13 equivalents.
# Like problem 0, each letter should be on its own line.
# A line of this string might look like:
#       h <-> u

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def rot13_table(s):
  y = 0
  i = 0
  phrase = ''
  while y < len(s):
    if s[y] >= 'a' and s[y] < 'n':
        i = ord(s[y]) + 13
    elif s[y] >= 'n' and s[y] <= 'z':
        i = ord(s[y]) - 13
    phrase = chr(i)
    print (s[y] + '<->' + phrase)
    y = y + 1

print(('=' * 10) + "Problem 3" + ('=' * 10))
rot13_table(alphabet)

# End Problem 3
#==================================================

#==================================================
# Problem 4
# Write a function that will take a string consisting of
# lowercase letters only and will return its rot13 equivalent.

# For example, rot13("skywalker") would return "fxljnyxre"

def rot13(s):
  y = 0
  i = 0
  phrase = ''
  while y < len(s):
    if s[y] >= 'a' and s[y] < 'n' or s[y] >= 'A' and s[y] < 'N':
        i = ord(s[y]) + 13
    elif s[y] >= 'n' and s[y] <= 'z' or s[y] >= 'N' and s[y] <= 'Z':
        i = ord(s[y]) - 13
    else:
        i = ord(s[y])
    phrase += chr(i)
    y = y + 1
  return phrase

print(('=' * 10) + "Problem 4" + ('=' * 10))
tester = 'skywalker'
rotted = rot13(tester)
print( tester + ' -> ' + rotted )

# What happens when you call rot13 on a string that was created by rot13?
# print out your answer as a string
answer = 'The string would revert to its original state.'
print(answer)

# End Problem 4
#==================================================

#==================================================
# Problem 5

# Go back to problem 2, create a new version below such
# that it now works with both upper and lower case letters.
def rot13char_anycase(c):
    i = 0
    if c >= 'a' and c < 'n' or c >= 'A' and c < 'N':
        i = ord(c) + 13
    elif c >= 'n' and c <= 'z' or c >= 'N' and c <= 'Z':
        i = ord(c) - 13
    else:
        i = ord(c)
    c = chr(i)
    return c

# Test your function here

print(('=' * 10) + "Problem 5" + ('=' * 10))
print( 'b: ' + rot13char_anycase('b') )
print( 'q: ' + rot13char_anycase('q') )
print( 'B: ' + rot13char_anycase('B') )
print( 'Q: ' + rot13char_anycase('Q') )
print( '?: ' + rot13char_anycase('?') )
print( '$: ' + rot13char_anycase('$') )

# End Problem 5
#==================================================

#==================================================
# Problem 6

# Look back to problem 4, create a new version below
# that can take a string with any characters in it,
# but will only modify letters, upper or lowercase,
# leaving spaces, numbers and punctuation unchanged.
#
# Hint: If you've gotten to this point, most of the
# work has already been done.

def rot13_full(s):
  y = 0
  i = 0
  phrase = ''
  while y < len(s):
    if s[y] >= 'a' and s[y] < 'n' or s[y] >= 'A' and s[y] < 'N':
        i = ord(s[y]) + 13
    elif s[y] >= 'n' and s[y] <= 'z' or s[y] >= 'N' and s[y] <= 'Z':
        i = ord(s[y]) - 13
    else:
        i = ord(s[y])
    phrase += chr(i)
    y = y + 1
  return phrase

print(('=' * 10) + "Problem 6" + ('=' * 10))
print(rot13_full("Nerf Ares, gel sync pyrex. Terra hey!"))
# Test your function here


# End Problem 6
#==================================================
