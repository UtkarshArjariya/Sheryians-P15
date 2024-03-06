# Day 6 notes

# Logical operator revision

print(34 or "Hello" or 34 or 44 or "kl")
print(34 and "Hello" and 34 and 44 and "kl")


'''''
Decimal to binary conversion  (You can do this in your notebook)
19//2 -> 9 -> 1 (Here, 9 is quotient and 1 is remainder)
9//2 -> 4 -> 1
4//2 -> 2 -> 0
2//2 -> 1 -> 0
1//2 -> 0 -> 1

So, 19 = 10011 (This is binary representation of 19)

Binary to decimal conversion of 1100001
1*2^6 + 1*2^5 + 0*2^4 + 0*2^3 + 0*2^2 + 0*2^1 + 1*2^0 = 64 + 32 + 1 = 97
                        or
 1     1       0       0       0       0       1 
 *     *       *       *       *       *       *
2^6   2^5     2^4     2^3     2^2     2^1     2^0
64  +  32  +   0   +   0   +   0   +   0   +   1   = 97

So, 1100001 = 97

101011011 - binary to decimal conversion
1*2^8 + 0*2^7 + 1*2^6 + 0*2^5 + 1*2^4 + 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0 = 256 + 64 + 16 + 8 + 2 + 1 = 347
                        or
 1     0       1       0       1       1       0       1       1
 *     *       *       *       *       *       *       *       *
2^8   2^7     2^6     2^5     2^4     2^3     2^2     2^1     2^0
256 +  0   +  64   +   0   +  16   +   8   +   0   +   2   +   1   = 347

So, 101011011 = 347
'''''

# Bitwise operators or compliment operators or tilt operators
# ~, &, |, ^, <<, >>

# i) ~ (Compliment operator) - It is used to convert 1 to 0 and 0 to 1 example -9 = +8
print(~-9) # 8

# ii) & (And operator) - It is used to convert 1 to 1 and 0 to 0
print(4 & 7) # 4

# iii) | (Or operator) - It is used to convert 1 to 1 and 0 to 1
print(4 | 7) # 7

# iv) ^ (XOR operator) - It is used to convert 1 to 0 and 0 to 1
print(4 ^ 7) # 3

# v) << (Left shift operator) - It is used to shift the bits to the left side
print(12 << 2) # 48, shift n bits to the left side, then the number will be multiplied by 2^n
'''''
12<<2
1100.00<<2
110000.00
48

In left side shift, the resultant always increases
'''''

# vi) >> (Right shift operator) - It is used to shift the bits to the right side
print(12 >> 2) # 3, shift n bits to the right side, then the number will be divided by 2^n
'''''
12>>2
1100.00>>2
0011.00
3

In right side shift, the resultant always decreases
''''' 
