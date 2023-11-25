from math import exp,sin,fabs 
file = open('input.txt', "r") 
l = open("output.txt", "w") 
a = file.read().split(" ") 
b = list(map(float,a)) 
 
def calc(n, p): 
    h= (1/n)-exp(n)*sin(p) 
    y= h/fabs(h+1) 
    return [h, y, n, p] 
f = calc(b[0],b[1]) 
l.write(""+str(f[0])+" "+str(f[1])+" "+str(f[2])+" "+str(f[3])) 
file.close() 
l.close()