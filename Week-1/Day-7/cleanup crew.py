try:

    num1 = 10
    num2 = 0
    result = num1 / num2
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Calculation failed.")
finally:
    print("Execution Complete")
    