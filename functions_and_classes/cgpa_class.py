class Course:
    """Represents a course with a name, grade, and credit unit."""
    
    grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}

    def __init__(self, name: str, grade: str, credit: int):
        
        self.name = name
        self.grade = grade.upper()  # Convert grade to uppercase for consistency
        self.credit = credit
        self.grade_point = self.grade_points.get(self.grade, 0.0)  # Default to 0.0 for invalid grades

    def get_weighted_score(self):
        """Returns the weighted score (grade point * credit)."""
        return self.grade_point * self.credit


class Student:
    """Manages a student's courses and calculates CGPA."""
    
    def __init__(self, name: str):
        self.name = name
        self.courses = []  # List to store Course objects

    def add_course(self, course: Course):
        """Adds a course to the student's record."""
        self.courses.append(course)

    def calculate_cgpa(self):
        """Computes CGPA based on total grade points and total credits."""
        total_grade_points = sum(course.get_weighted_score() for course in self.courses)
        total_credits = sum(course.credit for course in self.courses)
        
        if total_credits == 0:
            return 0.0  # Avoid division by zero
        
        return round(total_grade_points / total_credits, 2)

    def display_courses(self):
        """Displays the courses taken by the student."""
        print(f"\nCourses taken by {self.name}:")
        for course in self.courses:
            print(f"- {course.name}: Grade {course.grade}, Credit {course.credit}")

    def display_cgpa(self):
        """Prints the CGPA of the student."""
        print(f"\n{self.name}'s CGPA: {self.calculate_cgpa()}")


# Example Usage
if __name__ == "__main__":
    student = Student("John Doe")

    # Adding courses
    student.add_course(Course("Mathematics", "A", 3))
    student.add_course(Course("Physics", "B", 4))
    student.add_course(Course("Chemistry", "C", 3))
    student.add_course(Course("English", "B", 2))

    # Displaying courses and CGPA
    student.display_courses()
    student.display_cgpa()

