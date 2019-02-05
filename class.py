class Mathematics:

	def __init__(self, list):
		self.list = []

	def multiplication(self):
		list_1 = [i * 3 for i in self.list]
		return list_1

	def subtraction(self):
                list_2 = [i - 5 for i in self.list] 
                return list_2

	def division(self):
		a = input("Input any number except 0")
		try:
			a = int(a)
                	list_3 = [i / a for i in self.list] 
                	return list_3
		except ZeroDivisionError:
			print("Division by Zero!")
		except ValueError:
			print("Inappropriate Data")


action = Mathematics([])
action.list.append(50)
action.list.append(100)
action.list.append(150)
action.list.append(200)

print(action.multiplication())
print(action.subtraction())
print(action.division())






