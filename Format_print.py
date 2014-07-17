__author__ = 'ND'
width = int(raw_input('Please input width'))
prince_width = 10
item_width = width - prince_width
header_format = '%-*s%*s'
print_format = '%-*s%*.2f'

print '=' * width
print header_format % (item_width,'Item',prince_width, 'Price')

print '-' * width
print print_format % (item_width,'Apple',prince_width,1.2)
print header_format
print prince_width
print '-' * width