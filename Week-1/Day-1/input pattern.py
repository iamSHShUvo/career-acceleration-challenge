#standard input (not safe)
# age = input ("Age: ")

# academy standard input (safe)

raw_val = input ('Enter Principal: ')
try:
    principal = float (raw_val) 
    print (f"Accepted: ${principal:,.2f}") #F-string formatting
except ValueError:
    print ('Error: Invalid Number')