for a in range(1,350):
    t1 = (1000-a)
    t2 = (a**2)/(1000-a)
    if (t1+t2)%2 == 0 and (t1-t2)%2 == 0 :
        c = int((t1+t2)/2)
        b = int((t1-t2)/2)
        break

print(a,b,c)
print(a*b*c)