import datetime

current = datetime.datetime.now()

print("=== My Daily Mood Advisor ===")

name = input("Enter your name: ")
mood = input("How are you feeling today? (happy/sad/stressed/tired): ").lower()
energy = int(input("Enter your energy level (1-10): "))

print()

if energy >= 7:
    print("You have plenty of energy today!")
else:
    print("You should take things a little slower today.")

print()

if energy >= 5:
    print("Your energy level is good.")
else:
    print("Your energy level is low.")

print()

if mood == "happy":
    advice = "Keep smiling and spread your positive energy!"
elif mood == "sad":
    advice = "Talk to someone you trust and remember tomorrow is a new day."
elif mood == "stressed":
    advice = "Take a short break, breathe deeply, and organize your tasks."
elif mood == "tired":
    advice = "Get some rest and stay hydrated."
else:
    advice = "Stay positive and make today a great day."

print("Current Date:", current.strftime("%B %d, %Y"))
print("Current Time:", current.strftime("%I:%M:%S %p"))

print("\n===== Daily Mood Report =====")
print("Name:", name)
print("Mood:", mood)
print("Energy Level:", energy)
print("Advice:", advice)