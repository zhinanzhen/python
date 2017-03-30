class Employee:
	empCount=0
	
	def __init__(self, name, salary):
		self.name = name
		self.salary=salary
		Employee.empCount += 1
	
	def displayCount(self):
		print('total employee %d' % Employee.empCount)
	
	def displayEmployee(self):
		print('name:',self.name,';','salary:',self.salary)
		
emp1 = Employee('xu',1000)
emp1.displayEmployee()
emp1.name='xu2222'
emp1.displayEmployee()

emp2 = Employee('yue',2000)
emp2.displayEmployee()

print('total count:',Employee.empCount)

print("hasattr:",hasattr(emp1,'name'))
print("hasattr:",hasattr(emp1,'age'))

print(getattr(emp1,'name'))

print("set:",setattr(emp1,'name','xuxiangnan'))
getattr(emp1,'name')

print("del",delattr(emp1,'name'))

print('=========================')
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)