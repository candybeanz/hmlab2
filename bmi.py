"""
he=input("enter h ")
we=input("enter w ")


def calculate_bmi(h, w):
    print("height is "+h)
    print("weight is "+w)
    cal=

bmi =calculate_bmi(he, we)

def cal_bmi(w,h):
    print(f'height is {h}')
    print(f'weight is {w}')
    cal=w/h**2
    return cal

returned_cal=cal_bmi(w=20,h=30)
print(f'Bmi is: {round(returned_cal,2)}')
"""

W=float(input("Input weight: "))
H=float(input("Input height: "))

def cal_bmi(w,h):
    print("Height is "+ str(h))
    print("Weight is "+ str(w))
    cal=w/(h**2)
    if cal<18.5:
        print("under weight")
    elif cal>=18.5 and cal<=25.0:
        print("normal weight")
    else:
        print("over weight")
    return cal
bmi=cal_bmi(W,H)
print(f"bmi is {bmi}")