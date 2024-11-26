import pandas as pd

def calculate_course_gpa(assignments):
    df = pd.DataFrame(assignments, columns=["Assignment", "Grade", "Target"])
    return df["Grade"].mean()
