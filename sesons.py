sesons=("Winter","Spring","Summer","Fall")
mon=int(input("Enter a number of a month:"))

def seson(mon):
    if mon==12 or mon <=2:
         return sesons[0]
    elif 3<= mon <=5:
        return sesons[1]
    elif 6<= mon <=9:
        return sesons[2]
    else:
        return sesons[3]




print(seson(mon))