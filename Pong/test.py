a = float(input(">>>"))
x = 8
z = 0
while x <= 50:
    y = round((5 + (x ** a)), 3)
    d = round(y - z, 3)
    z = y
    print(f"{x} || {y} || +{d}")
    x += 1
    
