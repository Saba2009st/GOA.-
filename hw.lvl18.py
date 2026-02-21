#1
number = int(input("შემოიტანეთ რიცხვი ფაქტორიალის გამოსათვლელად: "))
factorial = 1

for i in range(1, number + 1):
    factorial += i

print(f"{number}-ის ფაქტორიალი არის: {factorial}")



#2
num = 10
remainder = num % 3 

print(f"10 გაყოფილი 3-ზე, ნაშთია: {remainder}") 

if num % 2 == 0:
    print("რიცხვი ლუწია")
else:
    print("რიცხვი კენტია")




#3
print(f"{num}-ის გამყოფებია:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
