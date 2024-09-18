def int_to_roman(num):
    # List of tuples mapping integer values to Roman numerals
    val = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    roman_numerical = ""

    for v, r in val:
        while num>= v:
            roman_numerical += r
            num -= v

    return roman_numerical

num = int(input())
print(int_to_roman(num))