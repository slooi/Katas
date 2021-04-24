def scramble2(s1, s2):
	s2_set = set(s2)
	for letter in s2_set:
		if s1.count(letter) < s2.count(letter):
			return False
	return True


def scramble(s1, s2):
    # returns true if a portion of str1 can be rearrannged to match s2	
	# Else false
	#  case letters will be used (a-z). No punctuation or digits will be included.
	#
	
	letter_dict = {}
	

	i=0
	for letter in s1:
		if letter not in letter_dict:
			letter_dict[letter] = 1
		else:
			letter_dict[letter] += 1
	

	# letter_set = set(s1)
	for letter in s2:
		if letter not in letter_dict:
			return False
		elif letter_dict[letter] > 0:
			letter_dict[letter]-=1
		else:
			return False
	return True
print(scramble("aasldkjqwoeiquwioeuqwoieuasdlaskdjalskjdzxcmzxncbmnbvmxbvajdkaldjlqwkjelkeklrtjoiugqwertyuiolkjhgfdsaszxcvbnmdoigudfbnmn","zxmcznxcbmvbaslkdjalskdjkfhghqwpeoiewuoreriutyasdaskdjasjkdhqweuiqweyuiqwekdhakjhaskjdhaksjdhaqweretkjdhakjsdhzxcmnzbxcmnbvmnaskhdkasdquweyiuqweyiqwueyiuayiuaydiruasyudasa"))
print(scramble("aasldkjqwoeiqpuwioeuqwoieuasdlaskdjalskjdzxcmzxncbmnbvmxbvajdkaldjlqwkjelkeklrtjoiugqwertyuiolkjhgfdsaszxcvbnmdoigudfbnmn","zxmcznxcbmvbaslkdjalskdjkfhghqwpeoiewuoreriutyasdaskdjasjkdhqweuiqweyuiqwekdhakjhaskjdhaksjdhaqweretkjdhakjsdhzxcmnzbxcmnbvmnaskhdkasdquweyiuqweyiqwueyiuayiuaydiruasyudasa"))
