class BankAccount:
    def __init__(self, initialBalance = 0.0):
        self.initialBalance = initialBalance
    
    def deposit(self, amount):
        self.initialBalance += amount
        return amount
    
    def withdraw(self, amount):
        if self.initialBalance >= amount:
            self.initialBalance -= amount
            return amount
        else:
            self.initialBalance -= 10
            return "You were charged $10 overdraft"
    
    def addInterest(self, rate):
        rate = self.initialBalance / (rate * 100)
        self.initialBalance += rate
        return rate
        
        
    def getBalance(self):
        return self.initialBalance

class Student:
    def __init__(self, studentID, name, address, program,):
        self.studentID = studentID
        self.name = name
        self.address = address
        self.program = program
        self.current_courses = []
        self.completed_courses = {}
    
    def get_description(self):
        return "Student ID: " + self.studentID + "\n" + "Student name: " + self.name + "\n" + "Address: " + self.address + "\n" + "Program: " + self.program
    
    def add_course(self, course_id):
        self.current_courses.append(course_id)
        return self.current_courses
    
    def drop_course(self, course_id):
        if course_id not in self.current_courses:
            raise ValueError("Course not found")
        self.current_courses.remove(course_id)
        return self.current_courses
    
    def course_completed(self, course_id, marks_obtained):
        self.completed_courses[course_id] = marks_obtained
        return self.completed_courses

def main():
    
    harrysAccount = BankAccount(1000.0)
    harrysAccount.deposit(500)
    harrysAccount.withdraw(2000)
    harrysAccount.addInterest(1.0)
    print(harrysAccount.getBalance())
    
    print()
    print()
    
    john = Student("1001", "John", "150 Crosbie", "Programmer Analyst")
    print(john.get_description())
    print(john.add_course("1002"))
    print(john.course_completed("1003", "50"))
    
    
if __name__ == "__main__":
    main()