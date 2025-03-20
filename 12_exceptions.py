### Exceptions ###
try:
    print(5 + "5")
except Exception as e:
    print(e)
    print("Something went wrong")
finally:#no es obligatorio
    print("This will always run")

print("Program continues")