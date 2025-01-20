def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_counter():
	text = get_book_text("books/frankenstein.txt")
	lowercase_text = text.lower()
	lowered_dictionary = {}
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	alphabet_list = []
	
	for j in range(len(alphabet)):
		alphabet_list.append(alphabet[j])

	for i in range(len(lowercase_text)):
		if lowercase_text[i] not in lowered_dictionary and lowercase_text[i] in alphabet_list:
			lowered_dictionary[lowercase_text[i]] = 1
		elif lowercase_text[i] in lowered_dictionary:
			lowered_dictionary[lowercase_text[i]] += 1

	for key in lowered_dictionary:
		print(f"The '{key}' character was found {lowered_dictionary[key]} times")
	


word_counter()