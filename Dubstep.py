def song_decoder(song):
	# INPUT - string - WUB'ed song
	# RETURN - string - decoded
	# ASSUMPTIONS: no WUBs in original string

	# GATCHA:
	"""
		- song is len of 1,2,3
	"""


	if len(song)<3:
		return song

	decoded_song = ""
	against_str = "WUB"
	i = 0
	while i < len(song):
		if song[i:i+3] == against_str:
			# Only add one space between words, prevent spaces from happening at beginning of string
			if not decoded_song == "" and not decoded_song[-1] == " ":
				decoded_song+=" "
			i+=3
		else:
			decoded_song += song[i]
			i+=1

	# Removes trailing white space that occurred from decoding process
	if decoded_song[-1] == " ":
		return decoded_song[0:-1]
	else:
		return decoded_song
	# may be 0
	# after last word number could be 0


	# wub before first word of song
	# after last word
	# at least one between pair of words
	# boy glues together all words including wub
	# one string

print(song_decoder("AWUBBWUBC"))