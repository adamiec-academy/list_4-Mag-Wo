def min_max(data):
    
    min_value = data[0]
    max_value = data[0]
    
    for value in data:
        if value > max_value:
            max_value = value
        elif value < min_value:
            min_value = value
            
    return min_value, max_value
