import math


def is_triangular(x):
    n = math.sqrt(8 * x + 1)
    if n - int(n):
        return False
    else:
        return True


d = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7,
    "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20,
    "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26
}

fptr = open("E:\Python\p042_words.txt")
words_list = fptr.read().split('","')
count = 0
i = 0
while i < len(words_list):
    sum = 0
    for j in words_list[i]:
        sum += d.get(j,0)
    if is_triangular(sum):
        count += 1
    i += 1
print(count)

"""

d = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six"
}

phone = input("Phone : ")
s = ""
for i in phone:
    s += d[int(i)]
    s += " "

print(s)

"""
