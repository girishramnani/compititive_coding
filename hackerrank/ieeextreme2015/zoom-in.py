columns = int(input())
rows = int(input())
storage = dict()
for i in range(int(input())):
    small_char = input()
    character =[input()[:columns] for j in range(rows)]
    storage[small_char] = character

for i in range(int(input())):
    word = input()
    output = [[] for _ in range(rows)]
    for ro in range(rows):
        for char in word:
            output[ro].append(storage[char][ro])
    for line in output:
        print("".join(line))
