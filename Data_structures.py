#List of data structure,mutable[changable],indexed,ordered
cars=["toyota","nissan","subaru"]
cars[2]="marcedese"

print(cars)
print(f"i love {cars[2]}")


#tuple

fruits=("mangoes","oranges","watermelon","pineapples")

print(fruits)
print(f"i love eating {fruits[2]}")

#sets, unordered,non index
comp=("hp","dell","lenovo")
print(comp)

#dictionaries
employee={"name":"daniel","age":"55","salary":"45000"}

print(employee)
print(f"the name of employee is {employee['name']}")

number=10

if number>=10:
    print("1")
if number<10:
    print("2")
else:
    print("3")