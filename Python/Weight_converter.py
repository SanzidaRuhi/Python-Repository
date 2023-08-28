weight=float(input("enter the wight: "))
unit=input("enter unit in lbs(L) or kgs(K): ")
if unit.upper()=='L':
    convert=weight*.45
    print(f"you are {convert} kilos")
else:
    convert=weight/.45
    print(f"you are {convert} pounds")