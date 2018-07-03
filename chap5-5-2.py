x = 10
y = 5
z = 0
def culc():
    global z
    z = x + y
    print(z)

culc()
print(z)