def unique_in_order(iterable):
	# iterable - string, Array<any>
	# RETURNS string|number[]

	previous_val = None
	new_arr = []
	for i, val in enumerate(iterable):
		if i == 0:
			new_arr.append(val)
		else:
			if not val == previous_val:
				new_arr.append(val)
		previous_val = val
	return new_arr
unique_in_order('AAAABBBCCDAABBB')
unique_in_order('ABBCcAD')         
unique_in_order([1,2,2,3,3])      