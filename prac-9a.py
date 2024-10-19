facts = { 
    'Sachin': 'batsman', 
    'batsman': 'cricketer' 
} 
# Function to derive the final fact from the initial fact 
def derive_fact(starting_subject, target_predicate): 
    current_subject = starting_subject 
    while current_subject in facts: 
        current_subject = facts[current_subject] 
        if current_subject == target_predicate: 
            return f"{starting_subject} is {target_predicate}" 
    return "Cannot derive the fact" 
# Define the starting subject and the target predicate 
starting_subject = 'Sachin' 
target_predicate = 'cricketer' 
# Derive and print the fact 
result = derive_fact(starting_subject, target_predicate) 
print(result)
