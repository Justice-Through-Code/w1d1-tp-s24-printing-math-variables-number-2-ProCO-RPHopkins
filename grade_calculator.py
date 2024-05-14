def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    student_name = input("Please enter your name: ")

    # Prompt the user for their scores in Math, Science, and English
    # Store the scores in the respective variables: math_score, science_score, english_score
    """Must add int() function or the output will be: 1686700.00.
    Not sure where that comes from? Perhaps something to do with
    the string before converting?"""

    math_score = int(input("Please input your Math score: "))
    science_score = int(input("Please input your Science score: "))
    english_score = int(input("Please input your English score: "))

    # Calculate the average grade
    # Used order of operations here and had to use the int() function
    average_grade = int(math_score + science_score + english_score)/3

    # Return the student's name and their average grade
    return student_name, average_grade

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    # The f-string followed by the {} is a way to add expressions of the variables to the string
    # The : .2f makes the returned grade into a float with two decimals
    print(f"{student_name}'s average grade is: {average_grade: .2f}")