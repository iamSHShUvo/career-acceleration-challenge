user = {"id":1}

try:
    print (user ["email"])
except KeyError:
    print ("No email found")

email = user.get ("email", "No email found")

print (f"Safe access result: {email}")