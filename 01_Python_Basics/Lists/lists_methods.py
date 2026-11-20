nums = [1, 2, 3]

nums.append(4)  # add one element at the end
print(nums)

nums.insert(2, 10)  # insert element at idx
print(nums)

nums.sort()     # arranges in increasing order
print(nums)

nums.sort(reverse=True)     # arranges in decreasing order
print(nums)

nums.reverse()      # reveres order
print(nums)

# Through Linear Search
x = 10
idx = 0

for val in nums:
    if (val == x):
        print(f"{x} found at index {idx}")
        break
    idx += 1

# Tuples () are immutable in Python

tup = (1, 2, 3, 4, 5)

print(tup)
print(type(tup))

print(tup[2])

for val in tup:
    print(val)

tup = (1, 2, 2, 3, 2, 4)

print(f"2 is at index {tup.index(2)} and appears {tup.count(2)} times")