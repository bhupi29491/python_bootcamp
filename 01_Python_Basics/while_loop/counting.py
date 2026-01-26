current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print("=================================")

# consider a loop that counts from 1 to 10 but prints only the odd numbers in that range
curr_number = 0
while curr_number < 10:
    curr_number += 1
    if curr_number % 2 == 0:
        continue

    print(curr_number)