# Copy solution from use_classes_create_employee file.
# Change the class that your previously created in such a way that calling print(empl) will give the same result as
# calling empl.print_info().

class Employee:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  # def empl(self):
  #   return self.firstname, self.lastname

empl = Employee("John", "Doe")
print(empl.firstname)