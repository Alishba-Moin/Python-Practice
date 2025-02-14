class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def diplayInfo(self):
        print(f" Name: {self.name}\n Salary: {self.salary} \n Company: {self.company}")

Programmer1 = Programmer("Alishba", 1200000)
Programmer1.diplayInfo()
Programmer2 = Programmer("Daniyal", 1000000)
Programmer2.diplayInfo()
Programmer3 = Programmer("Mishal", 1500000)
Programmer3.diplayInfo()
Programmer4 = Programmer("Zimal", 900000)
Programmer4.diplayInfo()