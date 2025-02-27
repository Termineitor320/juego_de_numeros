import random

print("----------------------------")
print("-----adivina el numero------")
print("----------------------------")

#input

print("--------------------------------------------")
n = int(input("Ingrese un numero entre (1-100): "))


#processing

maq = random.randint(1,100)

i = 1

while n != maq:
    if n < maq:
        print("------------------------------")
        print("El valor es mayor ")
        
    else:
        print("------------------------------")
        print("El valor es menor ")
        

    print("--------------------------------------------")
    n = int(input("Ingrese un numero entre (1-100): "))
    

    i += 1

print("------------------------------------------------------------------")
print("Felicidades ganaste, tuviste {i} intentos ")
print("------------------------------------------------------------------")



