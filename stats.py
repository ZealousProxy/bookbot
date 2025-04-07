import sys

path = sys.argv[1]

def get_book_text(path_to_file):
	file_contents = ""
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents
	pass


def get_num_words(path):
	book_text = ""
	book_text = get_book_text(path)
	return(len(book_text.split()))
	pass


def character_count():
	char_counts = {}
	book_text_cc = ""
	book_text_cc = get_book_text(path).lower()
	for character in book_text_cc:
		if character in char_counts:
			char_counts[character]+=1
		else:
			char_counts[character]=1
	return(char_counts)
	pass


def sorter(char_counts):
	chars_list = []
	for char, count in char_counts.items():
		chars_list.append({"char":char, "count":count})

	def sort_on(dict):
		return dict["count"]

		chars_list.sort(reverse=True, key=sort_on)
	return (chars_list)
	pass
