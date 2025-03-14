import random
import datetime

# ASCII Art Title
ascii_title = """
  ____       _   _                  _       
 |  _ \ _ __| |_| |_ _   _ _ __ ___| |_ ___ 
 | |_) | '__| __| __| | | | '__/ _ \ __/ _ \\
 |  __/| |  | |_| |_| |_| | | |  __/ ||  __/
 |_|   |_|   \__|\__|\__,_|_|  \___|\__\___|
"""
print(ascii_title)

# Display Current Date & Time
now = datetime.datetime.now()
print(f"📅 Current Date & Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# User Input
name = input("Enter your name: ")
print(f"Hello, {name}! 🎉 Welcome to Python!")

# Fun Fact About Python
fun_facts = [
    "🐍 Python was created by Guido van Rossum and released in 1991.",
    "🎭 Python is named after 'Monty Python', not the snake!",
    "🌍 Python is one of the most popular programming languages in the world.",
    "🚀 NASA, Google, Netflix, and even AI projects use Python!"
]

print(f"💡 Fun Fact: {random.choice(fun_facts)}")

# End Message
print("\n✅ This is a new Python file with extra features! 🚀")
