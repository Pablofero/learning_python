import math
#
res = .2
scale = 20
r = 20
#
r*=math.pi
iter = 0
while iter<r:
    if math.sin(iter)>0:
        i = 1
        for j in range(scale):
            print(" ",end="")
        while i<(scale*math.sin(iter)):
            print("*",end="")
            i += 1;
        print(" ")
    else:
        i = scale*math.sin(iter)
        for j in range(scale-abs(int(i))):
            print(" ",end="")
        while i<0:
            print("*",end="")
            i+=1;
        print(" ")
    iter+=res
