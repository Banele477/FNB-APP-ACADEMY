#collect two numbers the user 
try:
    num1 = float(input("Enter the first number: ").strip())
    num2 = float(input("Enter the second number: ").strip())
except ValueError:
    print("invalid input! Please eneter number only.")
    exit()

#Perform basic calculations (Addition, Subtraction, Multiplication)
add_res =round(num1 + num2, 2)
sub_res =round(num1 - num2, 2)
mul_res =round(num1 * num2, 2)

#Handle division operation and safely check for division by zero
if num2 == 0:
    div_res = "Error (Div by 0)"
    loor_res= "Error (Div by 0)"
    mod_res ="Error (Div By 0)"

else:
    div_res = round(num1 / num2, 2)
    loor_res = round(num1 // num2, 2)
    mod_res = round(num1 % num2, 2)

#Display all results in s format table usingf-strings
print("\n --- Calculation Results --- ")
print(f"Addition: {add_res}")
print(f"Subtraction: {sub_res}")
print(f"Multiplication: {mul_res}")
print(f"Division: {div_res}")
print(f"Floor Division: {loor_res}")
print(f"Modulus: {mod_res}")