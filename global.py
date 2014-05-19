
a_string = "This is globlas "
def foo():
	globals a_string = "test"
	print locals()

foo()
print a_string
