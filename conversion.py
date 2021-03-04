#user defined function
def Fah_To_Cel(Tf):
 #return the value in celcius
  return (5/9)*(Tf-32)

#output statmeent for user input
print("Enter Temperature in Fahrenheit: ", end="")

#input statment user input and initilize to fah variable
fah = float(input())

#call to function and value return in celcius to cel variable
cel = Fah_To_Cel(fah)

#output statement to print temperature in celcius
print("\nEquivalent Temperature in Celsius = {:.2f}".format(cel))