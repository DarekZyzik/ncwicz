# Create class Employee which takes name and last_name upon object creation.
# Calling empl.print_info() where empl is an Employee instance, should display string in format:
# '<name>, <last_name>'.

class Employee:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def print_info(self):
    print(self.firstname, self.lastname)

empl = Employee("John", "Doe")
empl.print_info()