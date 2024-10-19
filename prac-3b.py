import math 
increment = 0.1 
starting_point = [1, 1] 
points = [[1, 5], [6, 4], [5, 2], [2, 1]] 
def distance(x1, y1, x2, y2): 
    return math.pow(x2 - x1, 2) + math.pow (y2 - y1, 2) 
def sum_of_distances(x1, y1, points): 
    return sum(distance(x1, y1, px, py) for px, py in points) 
def new_distance(x1, y1, points): 
    return [x1, y1, sum_of_distances(x1, y1, points)] 
def new_points(minimum, *distances): 
    return next((d[:2] for d in distances if d[2] == minimum), None) 
min_distance = sum_of_distances(*starting_point, points) 
flag = True 
i = 1 
while flag: 
    d1 = new_distance(starting_point[0] + increment, starting_point[1], points) 
    d2 = new_distance(starting_point[0] - increment, starting_point[1], points) 
    d3 = new_distance(starting_point[0], starting_point[1] + increment, points) 
    d4 = new_distance(starting_point[0], starting_point[1] - increment, points) 
    print(i, round(starting_point[0], 2), round(starting_point[1], 2)) 
    minimum = min(d1[2], d2[2], d3[2], d4[2]) 
    if minimum < min_distance: 
        starting_point = new_points(minimum, d1, d2, d3, d4) 
        min_distance = minimum 
        i+= 1
    else: 
        flag = False
