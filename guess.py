import math
name = input("Hi, what is your Name? ")
print(f"Hello, {name}!Let's play a game!")
print("Think of random numbers from 1 to 100, and I'll try to guess it!")
playMore = "yes"
while playMore.lower() != "no":
guessChoice = "no"
isSmaller = "no"
isLarger = "no"
low = 1
high = 100
count = 0
while guessChoice.lower() != "yes":
mid = int(math.ceil((low + high-1)/2))
guessChoice = input(f"Is it {mid}?(yes/no)")
if guessChoice.lower() == "no":
isLarger = input(f"Is the number larger than {mid}?(yes/no)")
if isLarger.lower() == "yes":
low = mid+1
elif isLarger.lower() == "no":
high = mid - 1
count += 1
print(f"Yeey! I got it in {count} tries!")
playMore = input("Do you want to play more? ")
print("Bye-bye")