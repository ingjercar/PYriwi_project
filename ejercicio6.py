print("Binevenido al sistema")
print("_________________________________________")
print("Este sistema ")


for i in range (1, 101):
    
    if i % 3 == 0 and not i % 5 == 0:
        print("Fizz")
    elif i % 5 == 0 and i % 3 == 0:
             print("FizzBuzz")
    elif i % 5 == 0 and not i % 3 == 0:
        print("Buzz")
    else:
        print(i)
    

print("_________________________________________")
print("Fin del sistema")
