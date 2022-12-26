class Employee:
  def __init__(self, name, role, vacation_days):
    self.name = name
    self.role = role
    self.vacation_days = vacation_days
    self.taken_days = 0
  
  def request_leave(self, days):
    if self.vacation_days - self.taken_days >= days:
      self.taken_days += days
      return True
    else:
      return False
  
  def check_vacation_days(self):
    return self.vacation_days - self.taken_days

class Administrator:
  def __init__(self, name):
    self.name = name
  
  def approve_leave(self, employee, days):
    if employee.request_leave(days):
      print(f"{self.name} has approved {employee.name}'s request for {days} vacation days.")
    else:
      print(f"{self.name} has denied {employee.name}'s request for {days} vacation days.")

def run_leave_system():
  employees = [Employee("Alice", "Manager", 10), Employee("Richard", "Developer", 15)]
  admin = Administrator("Dushime")
  
  while True:
    print("Leave Management System")
    print("Enter 1 to request vacation days")
    print("Enter 2 to check remaining vacation days")
    print("Enter 3 to exit")
    choice = int(input())
    
    if choice == 1:
      print("Enter employee name:")
      name = input()
      employee = None
      for e in employees:
        if e.name == name:
          employee = e
          break
      if employee:
        print("Enter number of vacation days:")
        days = int(input())
        admin.approve_leave(employee, days)
      else:
        print("Employee not found.")
    elif choice == 2:
      print("Enter employee name:")
      name = input()
      employee = None
      for e in employees:
        if e.name == name:
          employee = e
          break
      if employee:
        remaining_days = employee.check_vacation_days()
        print(f"{employee.name} has {remaining_days} vacation days remaining.")
      else:
        print("Employee not found.")
    elif choice == 3:
      break
    else:
      print("Invalid input.")

run_leave_system()
