import math

# One method that takes an integer and returns the location numeral in abbreviated form. that is, you pass in 9 and it returns "ad"

# One method that takes a location numeral and returns its value as an integer. that is, you pass in "ad" and it returns 9

# One method that takes a location numeral and returns it in abbreviated form. that is, you pass in "abbc" and it returns "ad"

def get_abbreviation(n):
    powers = []
    while n > 0:
        x = math.log(n,2)
        if x % 1 == 0:
            powers.append(str(int(x)))
            break
        else:
            x = math.floor(x)
            powers.append(str(x))
            n -= 2 ** x
            if n == 2:
                powers.append('1')
                break
            if n == 1:
                powers.append('0')
                break
    for numb, i in enumerate(powers):
        powers[numb] = chr(ord('a') + (int(i)))
    powers.sort()
    return ''.join(powers)

challenge_1 = get_abbreviation(23)
print(challenge_1)

def get_number(n):
    x = 0
    for i in list(n):
        x += 2 ** (ord(i) - 97)
    return x

challenge_2 = get_number('z')
print(challenge_2)

def get_abbreviated_form(n):
    return(get_abbreviation(get_number(n)))

challenge_3 = get_abbreviated_form('abbc')
print(challenge_3)