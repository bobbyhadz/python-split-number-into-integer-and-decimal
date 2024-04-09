# Split a Float into Integer and Decimal parts in Python

import math

my_num = 1.3588

result = math.modf(my_num)
print(result)  # 👉️ (0.3588, 1.0)

print(result[0])  # 👉️ 0.3588
print(result[1])  # 👉️ 1.0