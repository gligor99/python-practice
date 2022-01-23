def square(x):
    return x * x

#Function for input name
def getName():
    name = str(input('Input your name: '))
    if name:
        print ("Hello " + str(name))
    else:
        print("Hello World") 
