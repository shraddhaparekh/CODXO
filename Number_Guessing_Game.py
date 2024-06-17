import randam 
number_to_guess = random.randint(1,100)

attempts = 0

print("welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")

while True:
  user_guess = int(input("Enter your guess:"))
  attempts += 1

if user_guess == number_to_guess:
  print("Congratulations! You guessed the number in {attempts} attempts.")
  break
elif user_guess < number_to_guess:
  print("Too low! try again.")
else:
  print("Too high!try again.")
