def dirReduc(arr):
	"""
	INPUTS:
		arr - string[] - 
	RETURN:
		string[]
	"""

	# iter through arr
	# [i] and [i+1]
	# If reduce i-1 <= MAKE sure not too go into negative
	#	=> maybe use [i-1] [i]
	#		=> no still encounter same problem
	# REMEMBER TO DO ANOTHER CHECK AFTER ANY REDUCTION OCCURS!!!!
	# ASSUMPTION: CAPITAL LETTERS ONLY, only has four directions NORTH, SOUTH, etc...
	dir_dict = {
		"NORTH": "SOUTH",
		"SOUTH": "NORTH",
		"EAST": "WEST",
		"WEST": "EAST"
	}

	length = len(arr)-1
	i=0
	while i < length:
		dir1 = arr[i]
		dir2 = arr[i+1]
		if dir_dict[dir1] == dir2:
			arr.pop(i+1)
			arr.pop(i)
			length-=2
			if i>0:
				i-=1
			# don't go into negative i's

			# check reduced_dir and see if it's reducable

		else:
			i+=1
	return arr

print(dirReduc(["NORTH","NORTH","SOUTH","SOUTH","EAST","WEST"]))