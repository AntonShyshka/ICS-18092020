class SuperStr(str):
	def is_repeatance(self, sub_string):
		if(not isinstance(sub_string,str)):
			return False
		if(self == '' or sub_string == ''):
			return False
		elif(len(sub_string)< len(self)):
			sub_string = sub_string*2
			if(sub_string in self):
				return True
			else:
				return False
		elif(self.count(sub_string) == float(len(self))/len(sub_string)):
			return True

	def is_palindrom(self):
		self = self.lower()
		if(self == ''):
			return True
		elif(self == self[::-1]):
			return True
		return False
	

s = SuperStr('123123123123')
print( s.is_repeatance('123') == True)
print( s.is_repeatance('123123') == True)
print( s.is_repeatance('123123123123') == True)
print( s.is_repeatance('12312') == False)
print( s.is_repeatance(123) == False)

print("\n\n-----")
print( s.is_palindrom() == False)
print( s == '123123123123')
print( int(s) == 123123123123)
print( s + 'qwe' == '123123123123qwe')
p = SuperStr('123_321')
print( p.is_palindrom() == True)