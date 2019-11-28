import random
import time

dice_result = []

print("Välkommen till tärningssimulatorn")

def average(numbers):
    return sum(numbers)/len(numbers)

ans = input("Vill du slå en tärning ")
result = random.randint(1, 6)
while ans == "ja":
    result = random.randint(1, 6)
    time.sleep(0.1)
    print(result)
    dice_result.append(result)
    ans = input("Vill du slå en tärning ")
else:
    time.sleep(0.1)
    print(dice_result)
    print(average(dice_result))


