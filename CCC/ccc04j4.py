shift = input()
s = input()

s = ''.join(c for c in s if c.isalpha())

for i in range(len(s)):
    code = (ord(s[i])-ord('A')+ord(shift[i%len(shift)])-ord('A'))%26+ord('A')
    print(chr(code), end='')