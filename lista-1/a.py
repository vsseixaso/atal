# https://codeforces.com/problemset/problem/908/A

s = input()

checklist = ['a', 'e', 'i', 'o', 'u', '1', '3', '5', '7', '9']

count = 0
for c in s:
    if c in checklist:
        count += 1

print(count)