n = 10
odd_number = 1

"""
while odd_number <= n:
    print odd_number
    odd_number = odd_number + 2
"""

odd_numbers = []

while odd_number <= n:
    odd_numbers.append(odd_number)
    odd_number += 2
print odd_numbers
