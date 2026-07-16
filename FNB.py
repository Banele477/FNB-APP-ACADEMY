# 1. Ask the user for the kilometers and convert it to a float
kilometers = float(input("Enter the number of kilometers you want to drive: "))

# 2. Ask for the petrol price per liter and convert it to a float
petrol_price = float(input("Enter the current petrol price per liter (e.g., 22.45): R"))

# 3. Calculate the liters needed (1 liter for every 10 km)
liters_needed = kilometers / 10

# 4. Calculate the total cost
total_cost = liters_needed * petrol_price

# 5. Round the final cost to 2 decimal places
final_cost = round(total_cost, 2)

# Print the final result
print("----------------------------------------")
print(f"Liters of fuel needed: {liters_needed} L")
print(f"The total cost of your trip will be: R{final_cost}")
print("----------------------------------------")
