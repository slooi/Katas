def rot13(message):
	"""
		INPUT: 
			message - string
		RETURN string - ciphered with Rot13
		NOTES:
			- number/special chars should bbe returned as they are
			- Only latin alphabet should be shifted
			- Remember the capitals
		BRAIN DUMP:
			- isAlphanumeric
			- ord/chr +13
			- wrap around
			- inspect each letter
		QUESITONS:
		 	- should we wrap?
	"""
	
	# iter through each character
	encoded_message =""
	for letter in message:
		ord13_letter = ord(letter)+13


		if ord(letter)>=ord("A") and ord(letter)<=ord("Z"):
			if ord13_letter > ord("Z"):
				ord13_letter = ord("A")+(ord13_letter-ord("Z"))-1
		elif ord(letter)>=ord("a") and ord(letter)<=ord("z"):
			if ord13_letter > ord("z"):
				ord13_letter = ord("a")+(ord13_letter-ord("z"))-1
		else:
			ord13_letter = ord(letter)
		
		encoded_message+= chr(ord13_letter)

	return encoded_message

print(rot13("abc"))
print("2")
print(rot13("z"))
print("3")
print(rot13(".asd"))