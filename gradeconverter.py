#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

done = False

while done != True:
  try:
    score = float(input('Enter score here:'))
  except:
    print('enter numbers only')
    continue
          
  if score > 1.0 or score <0:
    print('score is out of range')
    continue
  elif score >= 0.9:
    letter_score = 'A'
  elif score >= 0.8:
    letter_score = 'B'
  elif score >= 0.7:
    letter_score = 'C'
  elif score >= 0.6:
    letter_score = 'D'
  elif score < 0.6:
    letter_score = 'F'
  
  print(letter_score)
  done = True
  