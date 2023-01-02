def min_max(data):
    
    min = data[0]
    max = data[0]
    
    for value in data:
        if value > max:
            max = value
        elif value < min:
            min = value
            
    return min, max
