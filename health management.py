def getdate():
    import datetime
    return datetime.datetime.now()


def log():

    a = int(input("In whose file do you wan't to log : 1.Devansh 2.Adi 3.Dhruv \n"))
    if a==1 :
        b=int(input("What do you wan't to log : 1.Diet 2.Exercise \n"))
        if b==1:
            c=input("Enter the Diet here \n")
            d= open("Devansh Diet.txt","a")
            d.writelines("["+str(getdate())+"]"+" : "+c+".\n")
            print("Data has been logged")
            d.close()
        elif b==2:
            e = input("Enter the Exercise here \n")
            f= open("Devansh Exercise.txt", "a")
            f.writelines("["+str(getdate())+"]"+" : "+e+".\n")
            f.close()
            print("Data has been logged")
    elif a==2:
        g=int(input("What do you wan't to log : 1.Diet 2.Exercise \n"))
        if g==1:
            h = input("Enter the Diet here \n")
            i = open("Adi Diet.txt", "")
            i.writelines("["+str(getdate())+"]"+" : "+h+".\n")
            i.close()
            print("Data has been logged")
        elif g==2:
            j = input("Enter the Exercise here \n")
            k = open("Adi Exercise.txt", "a")
            k.writelines("["+str(getdate())+"]"+" : "+j+".\n")
            k.close()
            print("Data has been logged")
    elif a==3:
        l = int(input("What do you wan't to log : 1.Diet 2.Exercise \n"))
        if l == 1:
            m = input("Enter the Diet here \n")
            n = open("Dhruv Diet.txt", "a")
            n.writelines("["+str(getdate())+"]"+" : "+m+".\n")
            n.close()
            print("Data has been logged")
        elif l == 2:
            o = input("Enter the Exercise here \n")
            p = open("Dhruv Exercise.txt", "a")
            p.writelines("["+str(getdate())+"]"+" : "+o+".\n")
            p.close()
            print("Data has been logged")



def retrive():


    a = int(input("whose file do you wan't to retrive : 1.Devansh 2.Adi 3.Dhruv \n"))
    if a==1 :
        b=int(input("What do you wan't to retrive : 1.Diet 2.Exercise \n"))
        if b==1:
            d= open("Devansh Diet.txt")
            print( d.read())
            d.close()
        elif b==2:

            f= open("Devansh Exercise.txt")
            print(f.read())
            f.close()

    elif a==2:
        g=int(input("What do you wan't to retrive : 1.Diet 2.Exercise \n"))
        if g==1:

            i = open("Adi Diet.txt")
            print( i.read())
            i.close()
        elif g==2:

            k = open("Adi Exercise.txt")
            print(k.read())
            k.close()

    elif a==3:
        l = int(input("What do you wan't to retrive : 1.Diet 2.Exercise \n"))
        if l == 1:

            n = open("Dhruv Diet.txt")
            print(n.read())
            n.close()
        elif l == 2:

            p = open("Dhruv Exercise.txt")
            print( p.read())
            p.close()




while(1):
    x= int(input("Press 1 for log or 2 for retrive \n"))
    if x==1:
        log()
    elif x==2:
        retrive()
    else:
        print("Syntax Error")

    y=int(input("Do you want to log or retrive more data : 1.Yes  2.No\n"))
    if y==1:
        continue
    else:
        break
