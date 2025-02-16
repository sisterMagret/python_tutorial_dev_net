def calculate_cgpa(grades):
    """
    Function to calculate Cumulative Grade Point Average (CGPA).

    Parameters:
    grades (list of tuples): Each tuple contains [(grade_point, credit_hours)] for a course.

    Returns:
    float: The calculated CGPA rounded to 2 decimal places.
    """
    
    # Initialize total grade points and total credit hours
    total_grade_points = 0
    total_credit_hours = 0
    
    # Loop through each course's grade and credit hour
    for grade_point, credit_hour in grades:
        total_grade_points = total_grade_points + (grade_point * credit_hour)
        total_credit_hours = total_credit_hours + credit_hour
    
    
    # prevent division by zero error
    if total_credit_hours == 0:
        return 0.0
    
    # Compute CGPA
    cgpa =  total_grade_points / total_credit_hours
    
    # Return CGPA rounded to 2 decimal places
    return round(cgpa, 2)


courses = [(3.5, 3), (4.0, 4), (2.8, 2), (3.7, 3)]
cgpa = calculate_cgpa(courses)
print("CGPA:", cgpa)



