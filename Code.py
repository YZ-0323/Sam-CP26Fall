k = int(input())
s = input()

for i in range(len(s)):
    shift = 3 * (i + 1) + k
    code = (ord(s[i]) - ord('A') - shift) % 26 + ord('A')
    print(chr(code), end='')