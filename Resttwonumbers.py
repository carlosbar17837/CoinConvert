num1 = input ("Ingrese un Numero")   #We create var num1 and its value will be the input 
num1 = float(num1)                   # we convert this string input into a float var

num2 = input ("Ingrese el Numero que desea restar")         
num2 = float(num2)

rest = num1 - num2            #We create a var that will be saving our result 
rest = str(rest)              # We convert this float valut to a string value so we will be able to concatenate 
print ("El resultado es " + rest) # we take our string value to make the answer availble 