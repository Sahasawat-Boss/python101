import random
import datetime

# Randomized Greetings
greetings = ["Hello", "Hi", "Hey", "Greetings", "Salutations"]
selected_greeting = random.choice(greetings)

# Console Log Equivalent
print(f"{selected_greeting}, Python! 👋")
print(f"{selected_greeting}, GitHub! 🚀")

# User Input
name = input("Enter your name: ")
print(f"{selected_greeting}, {name}! 🎉")

# Display Current Date & Time
now = datetime.datetime.now()
print(f"Current Date & Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Simple Math Quiz
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
answer = num1 + num2
user_answer = int(input(f"Quick Math: What is {num1} + {num2}? "))

if user_answer == answer:
    print("✅ Correct! You're a math genius!")
else:
    print(f"❌ Oops! The correct answer was {answer}.")

# Fun Fact About Python
fun_facts = [
    "Python was created by Guido van Rossum and released in 1991.",
    "Python is named after 'Monty Python', not the snake! 🐍",
    "Python is one of the most popular programming languages in the world.",
    "Python is used by NASA, Google, Netflix, and even AI projects!"
]

print(f"💡 Fun Fact: {random.choice(fun_facts)}")
