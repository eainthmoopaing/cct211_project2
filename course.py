import tkinter as tk
from tkinter import ttk
from gpa_calculator import calculate_course_gpa

def open_course_window(semester_name, course_name, courses):
    syllabus = courses[course_name]

    def add_assignment():
        assignment_name = assignment_entry.get().strip()
        grade = grade_entry.get().strip()
        target_grade = target_grade_entry.get().strip()

        if not assignment_name or not grade or not target_grade:
            status_label.config(text="All fields are required!", fg="red")
            return

        try:
            grade = float(grade)
            target_grade = float(target_grade)
            syllabus.append((assignment_name, grade, target_grade))
            assignment_list.insert(tk.END, f"{assignment_name} - Grade: {grade}, Target: {target_grade}")
            status_label.config(text=f"Added '{assignment_name}' successfully!", fg="green")
        except ValueError:
            status_label.config(text="Invalid grade values!", fg="red")

    def calculate_course_gpa():
        if syllabus:
            course_gpa = calculate_course_gpa(syllabus)
            gpa_label.config(text=f"Course GPA: {course_gpa:.2f}", fg="blue")
            courses[course_name] = syllabus + [course_gpa]
        else:
            gpa_label.config(text="No assignments to calculate GPA!", fg="red")

    root = tk.Tk()
    root.title(f"Course: {course_name} ({semester_name})")
    root.geometry("500x400")

    tk.Label(root, text=f"Course: {course_name}", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(root, text="Assignment Name:", font=("Arial", 12)).pack(pady=5)
    assignment_entry = ttk.Entry(root, width=30)
    assignment_entry.pack(pady=5)

    tk.Label(root, text="Grade (Actual):", font=("Arial", 12)).pack(pady=5)
    grade_entry = ttk.Entry(root, width=10)
    grade_entry.pack(pady=5)

    tk.Label(root, text="Target Grade:", font=("Arial", 12)).pack(pady=5)
    target_grade_entry = ttk.Entry(root, width=10)
    target_grade_entry.pack(pady=5)

    ttk.Button(root, text="Add Assignment", command=add_assignment).pack(pady=10)

    assignment_list = tk.Listbox(root, width=50, height=10)
    assignment_list.pack(pady=5)

    gpa_label = tk.Label(root, text="", font=("Arial", 12))
    gpa_label.pack(pady=10)

    ttk.Button(root, text="Calculate Course GPA", command=calculate_course_gpa).pack(pady=5)

    status_label = tk.Label(root, text="", font=("Arial", 10))
    status_label.pack(pady=5)

    root.mainloop()
