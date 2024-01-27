print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1 + name2
lower_case = name.lower()
numberT1 = lower_case.count("t")
numberT2 = lower_case.count("r")
numberT3 = lower_case.count("u")
numberT4 = lower_case.count("e")
numberT5 = lower_case.count("l")
numberT6 = lower_case.count("o")
numberT7 = lower_case.count("v")
numberT8 = lower_case.count("e")
totalT = numberT1 + numberT2 + numberT3 + numberT4
totalL = numberT5 + numberT6 + numberT7 + numberT8
totalA = int(str(totalT) + str(totalL))
if totalA <= 10 or totalA > 90:
  print(f"Your score is {totalA}, you go together like coke and mentos.")
elif totalA >= 40 and totalA <=50:
  print(f"Your score is {totalA}, you are alright together.")
else:
  print(f"Your score is {totalA}.")
