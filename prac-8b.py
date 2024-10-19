def distributive_law(a, b, c): 
    # Calculate both sides of the distributive law 
    left_side = a * (b + c)            # Left side: a * (b + c) 
    right_side = (a * b) + (a * c)     # Right side: (a * b) + (a * c) 
    return left_side, right_side 
# Test values 
a = 3 
b = 4 
c = 5 
# Check Distributive Law 
left_result, right_result = distributive_law(a, b, c) 
print(f"Distributive Law: a * (b + c) = {left_result}, (a * b) + (a * c) = {right_result}") 
# Verify if both sides are equal 
if left_result == right_result: 
    print("The Distributive Law holds true.") 
else: 
    print("The Distributive Law does not hold true.")
