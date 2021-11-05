x = input("input number of floors: ")
y = 1 
z = 0 

def calc(x,y,z):
    for x in range(x):
        x = x - 1
        y = y + 2 
        z = y + z 
    return z+1

print(calc(int(x),y,z))