import random
import time
print("Välkommen till tärningssimulatorn")

ans = input("Vill du slå en tärning ")
result = random.randint(1, 6)
while ans == "ja":
    result = random.randint(1, 6)
    time.sleep(2)
    print(result)
    ans = input("Vill du slå en tärning ")
else:
    time.sleep(2)
    print("Ok")


