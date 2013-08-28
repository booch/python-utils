'''
Helper functions to display things in a more human way.

by Craig Buchek
'''


import re


def bytes(byte_count, precision=1):  # @ReservedAssignment
    '''
        Convert a number of bytes into a human-friendly string, with 'precision' digits after the decimal point.
    '''
    return number(byte_count, precision=precision, suffixes=[' byte', ' bytes', ' kB', ' MB', ' GB', ' TB', ' PB', ' EB', ' ZB', ' YB'])


def number(number, precision=3, suffixes=['', '', ' k', ' M', ' G', ' T', ' P', ' E', ' Z', ' Y']):
    '''
        Convert a number into a human-friendly string, with 'precision' digits after the decimal point.
    '''
    # Make sure it's really a number, so we can do math with it.
    number = float(number)
    # If the number is less than 1000, subtract 3 from precision, because 3 digits of precision fall before the decimal point.
    if number < 1000:
        precision = precision - 3
    # Treat 1 ('1', '1.0', '1.00', etc.) as a special case, for pluralization reasons. 
    if re.match(r'1(\.0+)?$', '%.*f' % (precision, number)):
        return '%.*f%s' % (precision, number, suffixes[0])
    thousand_powers = 0
    while number >= 1000:
        number = number / 1000.0
        thousand_powers += 1
    return '%.*f%s' % (precision, number, suffixes[thousand_powers + 1]) 
