def max(a, b):
    if a > b:
        return a
    else:
        return b

def max2(a, b, c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c

def length(list):
    counter = 0
    for x in list:
        counter += 1
    return counter

def wovel(a):
    vowel = ["a", "e", "i", "u", "o"]
    for letter in vowel:
        if letter == a:
            return True
    return False


def main():
    print("Hello World!")
    print(max(5, 6))
    print(max2(9, 8, 11))
    kecske = [1, 3, 4, 5, 6, 8, 7, 5, 3]
    lofasz = "picsa"
    print(length(lofasz))
    print(length(kecske))
    a = "h"
    print(wovel(a))


if __name__ == "__main__":
    main()
