class Person():
	def __init__(self, name):
		self.name = name
	        print "(Initializing {})". self.name
	def sayHi(self):
		print ('Hello, how are you', self.name)

p = Person('Duythien')
p.sayHi()
