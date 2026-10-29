class Grade:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        elif self.score >= 60:
            return 'D'
        else:
            return 'F'

class GradeCalculator:
    def __init__(self):
        self.grades = []

    def add_grade(self, name, score):
        grade = Grade(name, score)
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0
        total_score = sum(grade.score for grade in self.grades)
        return total_score / len(self.grades)

    def get_letter_grades(self):
        return {grade.name: grade.get_grade() for grade in self.grades}

class GradeCalculatorApp:
    def __init__(self):
        self.calculator = GradeCalculator()

    def run(self):
        while True:
            print("\nGrade Calculator Menu:")
            print("1. Add Grade")
            print("2. Calculate Average")
            print("3. Get Letter Grades")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter student's name: ")
                score = float(input("Enter student's score: "))
                self.calculator.add_grade(name, score)
                print(f"Added grade for {name}.")
            elif choice == '2':
                average = self.calculator.calculate_average()
                print(f"The average score is: {average:.2f}")
            elif choice == '3':
                letter_grades = self.calculator.get_letter_grades()
                for name, letter in letter_grades.items():
                    print(f"{name}: {letter}")
            elif choice == '4':
                print("Exiting the Grade Calculator.")
                break
            else:
                print("Invalid choice. Please try again.")
                
