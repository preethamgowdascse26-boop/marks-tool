def pass_count(marks, pass_mark):
	return len([mark for mark in marks if mark >= pass_mark])
