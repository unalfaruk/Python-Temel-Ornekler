x=1
y=1
while (y<=10):
    print(x,"*",y," = ", x*y)
    y=y+1
    if (y>=10):
        x=x+1
        y=1
        if(x>=10):
            break
