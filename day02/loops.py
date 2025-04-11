"""

In Jva:
    for(int i =o; i < 5; i++){

    }

"""
for i in range(1, 6):
    print(i)


print("Hello World")

print("-----------------------------")

s = "Selenium"

for i in s:
    print(i)

print("-----")

rever_string = ""

for each in s[::-1]:
    rever_string += each

print(rever_string)

print("-----------------------------")

for i in range(1, 6):
    for x in range(1, 6):
        print("Hello Selenium")

    print("-----------------------------")
"""
while True:
        print("Python Programming")
"""

score = int(input("Enter your score:\n"))

while score > 100 or score < 0:
    score = int(input("Please re-enter your score:\n"))

if score >= 0:
    print("Passed the exam")
else:
    print("Failed the exam")












