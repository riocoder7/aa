def associative_law_addition(a, b, c): 
    # (a + b) + c == a + (b + c) 
    left_side = (a + b) + c 
    right_side = a + (b + c) 
    return left_side, right_side 
def associative_law_multiplication(a, b, c): 
    # (a * b) * c == a * (b * c) 
    left_side = (a * b) * c 
    right_side = a * (b * c) 
    return left_side, right_side 
# Test values 
a = 2 
b = 3 
c = 4 
# Check Associative Law for Addition 
add_left, add_right = associative_law_addition(a, b, c) 
print(f"Addition: (a + b) + c = {add_left}, a + (b + c) = {add_right}") 
# Check Associative Law for Multiplication 
mul_left, mul_right = associative_law_multiplication(a, b, c) 
print(f"Multiplication: (a * b) * c = {mul_left}, a * (b * c) = {mul_right}")
