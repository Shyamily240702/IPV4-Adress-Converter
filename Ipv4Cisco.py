import ipaddress


def in_range(n):
    if n >= 0 and n <= 255:
        return True
    return False


def has_leading_zero(n):
    if len(n) > 1:
        if n[0] == "0":
            return True

    return False


def isValid(s):


    s = s.split(".")
    if len(s) != 4:
         return 0
         for n in s:

           if has_leading_zero(n):
              return 0
              if len(n) == 0:
               return 0
    try:
        n = int(n)

        if not in_range(n):
            return 0
    except:
        return 0
    return 1


def hexadecimal(ip):
    parts = ip.split('.')


    hexNumber = format(int(parts[0]), '02X') \
            + format(int(parts[1]), '02X') \
            + format(int(parts[2]), '02X') \
            + format(int(parts[3]), '02X')
    return hexNumber


def binary(ip):
    parts = ip.split('.')


    binaryNumber = format(int(parts[0]), '08b') \
               + format(int(parts[1]), '08b') \
               + format(int(parts[2]), '08b') \
               + format(int(parts[3]), '08b')
    return binaryNumber


def octal(ip):
    parts = ip.split('.')


    octalNumber = format(int(parts[0]), '03o') \
              + format(int(parts[1]), '03o') \
              + format(int(parts[2]), '03o') \
              + format(int(parts[3]), '03o')
    return octalNumber


def decimal(ip):
    parts = ip.split('.')


    decimalNumber = format(int(parts[0]), '03d') \
                + format(int(parts[1]), '03d') \
                + format(int(parts[2]), '03d') \
                + format(int(parts[3]), '03d')
    return decimalNumber


def conversions(ip):
    a = decimal(ip)


    b = binary(ip)
    c = octal(ip)
    d = hexadecimal(ip)
    return a, b, c, d

if __name__ == "__main__":
    print("Input 10 ipv4 addresses")
    list = []
    finalLine = []
    n = 10
for i in range(0, n):
    ip = input()
    if ((isValid(ip)) == True):
        list.append(ip)
    elif ((isValid(ip)) == False):
        ip = format(ipaddress.ip_address((ip)))
        list.append(ip)

textfile = open("conversion.txt", "w")

for element in list:
    textfile.write(element + "\n")
textfile.close()

with open('conversion.txt') as f:
    lines = f.readlines()

for line in lines:
    linePart = line.split("\n")
    finalLine.append(linePart[0])
f.close()

print(f"The first IP address in Decimal, Binary, Octal and hexadecimal format is {conversions(finalLine[0])} \n")
print(f"The second IP address in Decimal, Binary, Octal and hexadecimal format is {conversions(finalLine[1])} \n")
print(f"The third IP address in Decimal, Binary, Octal and hexadecimal format is {conversions(finalLine[2])} \n")
print(f"The fourth IP address in Decimal, Binary, Octal and hexadecimal format is {conversions(finalLine[3])} \n")
print(f"The fifth IP address in Decimal, Binary, Octal and hexadecimal format is {conversions(finalLine[4])} \n")
print(f"The sixth IP address in Decimal, Binary, Octal and hexadecimal format is {conversions(finalLine[5])} \n")
print(f"The seventh IP address in Decimal, Binary, Octal and hexadecimal format is {conversions(finalLine[6])} \n")
print(f"The eighth IP address in Decimal, Binary, Octal and hexadecimal format is {conversions(finalLine[7])} \n")
print(f"The ninth IP address in Decimal, Binary, Octal and hexadecimal format is {conversions(finalLine[8])} \n")
print(f"The tenth IP address in Decimal, Binary, Octal and hexadecimal format is {conversions(finalLine[9])} \n")


