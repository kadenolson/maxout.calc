# 1RM Calculator
import streamlit as st



print("ADVANCED ONE-REP-MAX CALCULATOR")
print("-------------------------------")

while True:
    try:
        reps = float(input("REPS: "))
        break
    except ValueError:
        print("Invalid input. Try again")

print("------------------------------------------")

while True:
    try:
        lifter_type = int(input("How many reps can you typically do at 90% of your max: "))
        break
    except ValueError:
        print("Invalid input. Try again")

print("------------------------------------------")

while True:
    try:
        weight = float(input("Weight: "))
        break
    except ValueError:
        print("Invalid input. Try again")

print("------------------------------------------")

while True:
    try:
        rpe = float(input("RPE (whole number or decimal): "))
        break
    except ValueError:
        print("Invalid input. Try again")


unit = input("Enter the unit of weight: ")
x = int(lifter_type * 10)
max_eq = round((1 + (1/x) * reps) * weight,1)
print("------------------------------------------")
print(f"Estimated 1RM: {max_eq} {unit}")


