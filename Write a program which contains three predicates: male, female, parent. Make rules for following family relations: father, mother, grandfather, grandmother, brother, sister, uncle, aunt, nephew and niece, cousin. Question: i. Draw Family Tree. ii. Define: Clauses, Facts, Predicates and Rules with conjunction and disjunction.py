# Facts about individuals 
male = {'John', 'Robert', 'Michael', 'Kevin'} 
female = {'Mary', 'Patricia', 'Jennifer', 'Linda'} 
parents = { 
    'John': ['Michael', 'Sarah'],   # John is the father of Michael and Sarah 
    'Mary': ['Michael', 'Sarah'],    # Mary is the mother of Michael and Sarah 
    'Robert': ['Kevin'],              # Robert is the father of Kevin 
    'Patricia': ['Kevin']             # Patricia is the mother of Kevin 
} 
def is_father(father, child): 
    return father in male and child in parents.get(father, []) 
def is_mother(mother, child): 
    return mother in female and child in parents.get(mother, []) 
def is_grandfather(grandfather, grandchild): 
    return grandfather in male and any(is_father(parent, grandchild) or is_mother(parent, grandchild) 
for parent in parents.get(grandfather, [])) 
def is_grandmother(grandmother, grandchild): 
    return grandmother in female and any(is_father(parent, grandchild) or is_mother(parent, 
grandchild) for parent in parents.get(grandmother, [])) 
def is_brother(sibling1, sibling2): 
    return sibling1 in male and sibling2 in parents.get(sibling1, parents[sibling2]) 
def is_sister(sibling1, sibling2): 
    return sibling1 in female and sibling2 in parents.get(sibling1, parents[sibling2]) 
def is_uncle(uncle, nephew): 
    return uncle in male and (any(is_brother(uncle, parent) for parent in parents.get(nephew, [])) or 
any(is_sister(uncle, parent) for parent in parents.get(nephew, []))) 
def is_aunt(aunt, niece): 
    return aunt in female and (any(is_brother(aunt, parent) for parent in parents.get(niece, [])) or 
any(is_sister(aunt, parent) for parent in parents.get(niece, []))) 
def is_cousin(cousin1, cousin2): 
    return any(parent1 != parent2 and (parent1 in parents.get(cousin2, []) or parent2 in 
parents.get(cousin1, [])) 
               for parent1 in parents.get(cousin1, []) 
               for parent2 in parents.get(cousin2, [])) 
# Example Queries 
print("Is John the father of Michael?", is_father('John', 'Michael')) 
print("Is Mary the mother of Sarah?", is_mother('Mary', 'Sarah')) 
print("Is Robert a grandfather of Michael?", is_grandfather('Robert', 'Michael')) 
print("Is Patricia an aunt of Kevin?", is_aunt('Patricia', 'Kevin')) 
