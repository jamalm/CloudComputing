word = input("Enter a Palindrome: \n")

if str(word.lower()) == str(word.lower())[::-1]:
  print("True")

else:
  print("False")
