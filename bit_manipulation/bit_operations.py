"""
Type: Bit Manipulation
"""

def get_bit(num, i):
	'''
	Return the bit at position i.
	1. Create mask with 1 at pos i.
	2. & the mask and input val, should only have a 1 at pos i if num is 1 at pos i.
	3. Convert bool to int.
	'''
	return int((num & (1 << i)) != 0)

def set_bit(num, i):
	'''
	Set bit at position i to 1.
	1. Create mask with 1 at pos i.
	2. | the mask and input val.
	'''
	return num | (1 << i)


def clear_bit(num, i):
	'''
	Set bit at position i to 0.
	1. Create mask with 1 at pos i.
	2. Invert mask to get 0 at pos i.
	3. & the mask and input val.
	'''
	return num & ~(1 << i)

def clear_left_bits(num, i):
	'''
	Set all bits from the left-most bit up to and including i to 0.
	1. Create mask with 1 at i.
	2. Subtract 1 from the mask to get all 1's up to i-1.
	3. & the mask and input val.
	'''
	return num & ((1 << i) - 1)

def clear_right_bits(num, i):
	'''
	Set all bits from i up to and including the right-most bit to 0.
	1. Create a mask of all 1's.
	2. Shift the mask to i+1.
	3. & the mask and input val.
	'''
	return num & (-1 << (i + 1))

def update_bit(num, i, update=True):
	'''
	Set bit at i to update val.
	1. Create a mask with update val at i.
	2. Clear bit at i for input val.
	3. | the mask and input val.
	'''
	return (num & ~(1 << i)) | (int(update) << i)


