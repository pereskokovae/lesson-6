import urwid


def is_very_long(password):
	symbol = len(str(password))
	is_very_long = symbol > 8
	return is_very_long
def has_digit(password):
	return any(letter.isdigit() for letter in password)
def has_letters(password):
	return any(letter.isalpha() for letter in password)
def has_upper_letters(password):
	return any(letter.isupper() for letter in password)
def has_lower_letters(password):
	return any(letter.islower() for letter in password)
def has_symbols(password):
	return any(not letter.isdigit() and not letter.isalpha() for letter in password)


def on_ask_change(edit, password):
	score = 0
	rating_functions = [
		is_very_long(password),
		has_digit(password),
		has_letters(password),
		has_upper_letters(password),
		has_lower_letters(password),
		has_symbols(password)
	]
	for code_counting in rating_functions:
		if code_counting == True:
			score = score + 2
	reply.set_text("Рейтинг пароля: " + str(score))


if __name__ == "__main__":
	ask = urwid.Edit("Введите пароль: ", mask='*')
	reply = urwid.Text("")
	menu = urwid.Pile([ask, reply])
	menu = urwid.Filler(menu, valign='top')
	urwid.connect_signal(ask, 'change', on_ask_change)
	urwid.MainLoop(menu).run()
