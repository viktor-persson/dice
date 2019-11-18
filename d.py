import random
print("Välkommen till tärningssimulatorn")

ans = input("vill du slå en tärning ")
result = random.randint(1, 6)
while ans == "ja":
    result = random.randint(1, 6)
    print(result)
    ans = input("vill du slå en tärning ")
else:
     print("ok")


