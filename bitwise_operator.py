# Bitwise operator is used to comapre binary number
# it operaters are binnary level

# Bitwise operator are & (AND)
#                      | (OR)
#                      ^ (XOR)
# AND(&)  x y z
#         0 0 0
#         1 0 0
#         0 1 0
#         1 1 1   in and(&) if any one is zero then zero
# 
# OR(|)   x y z
#         0 0 0
#         1 0 1
#         0 1 1
#         1 1 1  in or(|) if any one is one then one
#
# XOR(^). x y z
#         0 0 0
#         1 0 1
#         0 1 1
#         1 1 0 in xor(^) if both bits are same then zero
#                         if both bits are different then 1

print(6&3) #    8 4 2 1
           # 6= 0 1 1 0
           # 3= 0 0 1 1
           # &= 0 0 1 0
           #        2 output

print(6|3) # 6= 0 1 1 0
           # 3= 0 0 1 1
           # |= 0 1 1 1
           #      4 2 1 = 7 output

print(6^3) # 6= 0 1 1 0
           # 3= 0 0 1 1
           # ^= 0 1 0 1
           #      4   1 = 5 output

# operator precedence follows the table

# if same opder precedence comes then evaluate from left or right
# ==>>>
print(5+4-7+3) # see add and sub have same order precedence we use left to right

# 9-7= 2+3=5
