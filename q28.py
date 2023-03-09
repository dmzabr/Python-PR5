def sum(a, b):
    if b == 0:
        return a
    
    a += 1
    b -= 1
    
    return sum(a,b)
        
    
print(sum(int(input('Введите A:')), int(input('Введите B:'))))
