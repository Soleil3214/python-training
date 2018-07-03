list_x = [10, 20, 30]
def irekae(a):
    temp = a[0]
    a[0] = a[1]
    a[1] = a[2]
    a[2] = temp
    print(a)

irekae(list_x)
print(list_x)