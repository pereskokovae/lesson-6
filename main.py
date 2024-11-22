PASSWORD = input("Введите пароль: ")


def main():
	score = 0


	def is_very_long(PASSWORD):
		symbol = len(PASSWORD)
		is_very_long = symbol > 8
		return is_very_long
	def has_digit(PASSWORD):
		return any(letter.isdigit() for letter in PASSWORD)
		return has_digit
	def has_letters(PASSWORD):
		return any(letter.isalpha() for letter in PASSWORD)
		return has_letters
	def has_upper_letters(PASSWORD):
		return any(letter.isupper() for letter in PASSWORD)
		return has_upper_letters
	def has_lower_letters(PASSWORD):
		return any(letter.islower() for letter in PASSWORD)
		return has_lower_letters
	def has_symbols(PASSWORD):
		return any(not letter.isdigit() and not letter.isalpha() for letter in PASSWORD)
		return has_symbols


	rating_functions = [
		is_very_long(PASSWORD),
		has_digit(PASSWORD),
		has_letters(PASSWORD),
		has_upper_letters(PASSWORD),
		has_lower_letters(PASSWORD),
		has_symbols(PASSWORD)
]


	for code_counting in rating_functions:
		if code_counting:
			score = score + 2


	print(f"Рейтинг пароля: {score}")
		

if __name__ == "__main__":
	main()
