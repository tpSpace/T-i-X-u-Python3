import random
a=["","","","","","","","",""]

def draw(x):
    
    """
    012
    345
    678
    """
    if x==1:
        a[4]="*"
        return a
    elif x==2:
        a[0]="*"
        a[8]="*"
    elif x==3:
        a[0]="*"
        a[4]="*"
        a[8]="*"
        return a
    elif x==4:
        a[0]="*"
        a[2]="*"
        a[6]="*"
        a[8]="*"
    elif x==5:
        a[0]="*"
        a[2]="*"
        a[6]="*"
        a[8]="*"
        a[4]="*"
    elif x==6:
        a[0]="*"
        a[2]="*"
        a[6]="*"
        a[8]="*"
        a[1]="*"
        a[7]="*"
    return a
y="y"

while y=="y":
    
    print("Tai press 1 Xiu press 0")
    b=int(input(":"))

    sum=0
    a=[" "," "," "," "," "," "," "," "," "]
    k=random.randrange(1,7,1)
    draw(k)
    sum+=k
    print("+-------+")
    print("|",a[0],a[1],a[2],"|")
    print("|",a[3],a[4],a[5],"|")
    print("|",a[6],a[7],a[8],"|")
    print("+-------+")
    
    a=[" "," "," "," "," "," "," "," "," "]
    k=0
    k=random.randrange(1,7,1)
    draw(k)
    sum+=k
    print("+-------+")
    print("|",a[0],a[1],a[2],"|")
    print("|",a[3],a[4],a[5],"|")
    print("|",a[6],a[7],a[8],"|")
    print("+-------+")
    
    a=[" "," "," "," "," "," "," "," "," "]
    k=0
    k=random.randrange(1,7,1)
    draw(k)
    sum+=k
    print("+-------+")
    print("|",a[0],a[1],a[2],"|")
    print("|",a[3],a[4],a[5],"|")
    print("|",a[6],a[7],a[8],"|")
    print("+-------+")
    
    if sum>=4 and sum<=10 and b==0:
        print("You win")
        print("want to play more ? y/n ")
        y=inpuy(":")
    elif sum>=11 and sum<=17 and b==1:
        print("You win")
        print("want to play more ? y/n ")
        y=input(":")
    else:
        print("You lost")
        print("want to play more ? y/n ")
        y=input(":")
print("Good Night")
    



