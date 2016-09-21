input = raw_input('Input:')
print "Output: "+input

class MyException(Exception):
	def _init_(self,data):
		self.data = data
	def _str_(self):
		return self.data

try:
	intInput = raw_input("Input Int:")
	print "Int Input: "+str(1+long(intInput))
	raise Exception, "Nothing Wrong but Exception Test"
except Exception, info:
	print info
except ValueError:
	print("Bad Input!\r\n")

try:
	raise MyException, "Advance Info"
except MyException, advInfo:
	print advInfo

		