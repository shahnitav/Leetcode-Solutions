'''
CodeWars - https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.
Split the IP Address in Octets and see there are 4
Check each octet for leading zeros and if the value is between 0 and 255
else return False
'''

import re

def is_valid_IP(strng):
    octets = strng.split('.')
    if len(octets) != 4 or bool(re.search('\s', strng)):
        return False
    else:
        for x in octets:
            try:
                x_int = int(x)
            except:
                return False
            if len(x)>1 and x[0] == '0':
                return False
            else:
                if x_int < 0 or x_int > 255:
                    return False
    return True

if __name__ == '__main__':
    print("12.34.56 .1", is_valid_IP("12.34.56 .1"))
    print("123.045.067.089", is_valid_IP("123.045.067.089"))
    print("127.1.1.0", is_valid_IP("127.1.1.0"))