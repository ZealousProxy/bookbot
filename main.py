import sys

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		from stats import get_num_words,character_count,sorter

		path = sys.argv[1]
		num_words = get_num_words(path)
		char_count = character_count()
		sorted_chars = sorter(char_count)


		print ("============ BOOKBOT ============")
		print (f"Analyzing book found at {path}...")
		print ("----------- Word Count ----------")
		print (f"Found {num_words} total words")
		print ("--------- Character Count -------")


		for char_dict in sorted_chars:
			char = char_dict["char"]
			count = char_dict["count"]
			if char.isalpha():  # Only print alphabetical characters
				print (f"{char}: {count}")

		print ("============= END ===============")

main()	
