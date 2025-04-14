#Give letter grade according to marks to a student

m=float(input("Enter marks: "))
new_m=int(m)

if new_m>=0:
    if new_m>=90:
        print("A+")
    elif new_m>=80:
        print("A")
    elif new_m>=70:
        print("B+")
    elif new_m>=60:
        print("B")
    elif new_m>=50:
        print("C")
    elif new_m>=40:
        print("D")
    
    else:
        print("F")
else:
    print("Input Valid Marks")