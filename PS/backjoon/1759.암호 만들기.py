import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

L, C = map(int, input().split())

alphabet = sorted(map(str, input().split()))
vowel = {'a','e','i','o','u'}

def backtracking(idx, password):
    if len(password) == L:
        vowel_count = 0
        consonant_count = 0
        for char in password:
            if char in vowel:
                vowel_count += 1
            else:
                consonant_count += 1
        if vowel_count >= 1 and consonant_count >= 2:
            print(password)
            return
    for i in range(idx+1, C):
        password = password + alphabet[i]
        backtracking(i, password)
        password = password[:-1]

for i in range(C - L + 1):
    backtracking(i, alphabet[i])