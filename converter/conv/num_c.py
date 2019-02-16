# Arabian to Roman convert method

def arabian_to_roman(value):
    if not 0 < value < 4000:
        return 'Number must be 0<x<4000.'

    ints = (1000,900,500,400,100,90,50,40,10,9,5,4,1)
    nums = ('M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I')
    result = []

    for i in range(len(ints)):
        count = int(value / ints[i])
        result.append(nums[i] * count)
        value -= ints[i] * count

    return ''.join(result)

# Roman to Arabian convert method

def roman_to_arabian(input):
    input = input.upper()
    roman_numeral_map = (
        ('M', 1000, 3),
        ('CM', 900, 1),
        ('D', 500, 1),
        ('CD', 400, 1),
        ('C', 100, 3),
        ('XC', 90, 1),
        ('L', 50, 1),
        ('XL', 40, 1),
        ('X', 10, 3),
        ('IX', 9, 1),
        ('V', 5, 1),
        ('IV', 4, 1),
        ('I', 1, 3))

    (result, index) = (0, 0)
    for (numeral, value, maxcount) in roman_numeral_map:
        count = 0
        while input[index:index + len(numeral)] == numeral:
            count += 1
            if count > maxcount:
                return 'Invalid roman numeral'
            global result
            result += value
            index += len(numeral)

    if index < len(input):
        return 'Invalid roman numeral'

    if result == 0:
        return 'Failed'
    else:
        return result