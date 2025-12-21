try:

    user_number = int(input("Enter a positive number: "))

    if user_number < 0 :

        raise ValueError("No negatives")
    
    print(f"Processing number: {user_number}")

except ValueError as e:
    print(f"Error Caught: {e}")