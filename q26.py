def degree(a, b, res = 0):
    if res == 0:
        res = a
        b -= 1
        
    if b == 0:
        return res
    
    res = a*res
    b -= 1
    
    return degree(a,b,res)
        
    
print(degree(int(input('Введите A:')), int(input('Введите B:'))))
