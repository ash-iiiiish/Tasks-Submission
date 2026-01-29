# ---- Task 1: math_utils imports ----
import math_utils
from math_utils import square

print("Math Utils:")
print(math_utils.add(10, 5))
print(math_utils.subtract(10, 5))
print(square(6))

print("\n------------------\n")

# ---- Task 2: string_utils ----
import string_utils

text = "hello world from python"

print("String Utils:")
print(string_utils.capitalize_words(text))
print(string_utils.reverse_string(text))
print(string_utils.word_count(text))

print("\n------------------\n")

# ---- Task 4: shop_package imports ----
import shop_package.discount as disc
from shop_package.billing import calculate_total
from shop_package import flat_discount, apply_tax

print("Shop Package:")
print(disc.apply_discount(1000, 10))
print(flat_discount(500))
print(calculate_total([100, 200, 300]))
print(apply_tax(1000))
