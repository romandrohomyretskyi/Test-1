import math
file = open('input.txt', "r")
l = open("output.txt", "w")
a = file.read().split(" ")
b = list(map(float,a))
def abs(n):
    if n >= 0:
        return n
    else:
        return -n

def calc(n, p):
    h= (1/n)-math.exp(n)*math.sin(p)
    y= h/abs(h+1)
    return [h, y, n, p]
f = calc(b[0],b[1])
l.write(""+str(f[0])+" "+str(f[1])+" "+str(f[2])+" "+str(f[3]))
file.close()
l.close()