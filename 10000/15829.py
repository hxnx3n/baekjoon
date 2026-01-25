L = int(input())
s = input().strip()
mod = 1234567891
hash_value = 0
for i in range(L):
    hash_value = (hash_value + (ord(s[i]) - 96) * pow(31, i, mod)) % mod
print(hash_value)
