i=1
count=0
start=True

while start:
    c=0
    for j in range (1, (i+1)):
        a = i%j
        if (a==0):
            c = c+1

    if (c==2):
        count=count+1
        print i,
        if count==(10):
            print
        elif count==20:
            print
        elif count==30:
            print
        elif count==40:
           print 
    if count==50:
        start=False
    i=i+1
