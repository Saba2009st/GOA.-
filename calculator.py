# მომხმარებელს შემოატანინეთ პირველი რიცხვი
num1 = float(input("შეიყვანე პირველი რიცხვი: "))

# მომხმარებელს შემოატანინეთ მოქმედება
operation = input("აირჩიე მოქმედება (+, -, *, /): ")

# მომხმარებელს შემოატანინეთ მეორე რიცხვი
num2 = float(input("შეიყვანე მეორე რიცხვი: "))

# მოქმედებების შემოწმება
if operation == "+":
    result = num1 + num2
    print("პასუხი:", result)

elif operation == "-":
    result = num1 - num2
    print("პასუხი:", result)

elif operation == "*":
    result = num1 * num2
    print("პასუხი:", result)

elif operation == "/":
    if num2 == 0:
        print("0-ზე გაყოფა არ შეიძლება!")
    else:
        result = num1 / num2
        print("პასუხი:", result)

else:
    print("არასწორი მოქმედება აირჩიე")