stringToCheck = 'blauualb'

def isStringPalindrome(stringToCheck):
  stringReversed = reverseString(stringToCheck)
  if stringToCheck == stringReversed:
    return 'true'
  else:
    return 'false'

def reverseString(stringToCheck):
  stringReversed = ''
  length = len(stringToCheck)
  while length:
    length -= 1
    stringReversed += stringToCheck[length]
  return stringReversed

isStringPalindrome(stringToCheck)