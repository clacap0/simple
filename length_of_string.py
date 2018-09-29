
def length_o_string(a_string):
	the_counting = 0
	for i in a_string:
		if i == " ":
			pass
		else:
			the_counting += 1
	return the_counting

i_wanna_count = input("I will count how many characters are in your string, excluding spaces: ")
print (length_o_string(i_wanna_count))