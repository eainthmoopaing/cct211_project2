import tkinter as tk
from tkinter import ttk
from course import open_course_window

def open_semester_window(semester_name):
    courses = {}

    def add_course():
        course_name = course_entry.get().strip()
        if not course_name:
            status_label.config(text="Course name cannot be empty!", fg="red")
        elif course_name in courses:
            status_label.config(text="Course already exists!", fg="red")
        else:
            courses[course_name] = []
            course_list.insert(tk.END, course_name)
            status_label.config(text=f"Added '{course_name}' successfully!", fg="green")

    def open_selected_course():
        selected = course_list.curselection()
        if selected:
            course_name = course_list.get(selected[0])
            open_course_window(semester_name, course_name, courses)
        else:
            status_label.config(text="Please select a course!", fg="red")

    def calculate_gpa():
        if courses:
            total_gpa = sum(course[-1] for course in courses.values() if course) / len(courses)
            gpa_label.config(text=f"Semester GPA: {total_gpa:.2f}", fg="blue")
        else:
            gpa_label.config(text="No courses to calculate GPA!", fg="red")

    root = tk.Tk()
    root.title(f"Semester: {semester_name}")
    root.geometry("400x400")

    tk.Label(root, text=f"Semester: {semester_name}", font=("Arial", 14, "bold")).pack(pady=10)

    course_entry = ttk.Entry(root, width=30)
    course_entry.pack(pady=5)

    ttk.Button(root, text="Add Course", command=add_course).pack(pady=5)

    course_list = tk.Listbox(root, width=30, height=10)
    course_list.pack(pady=5)

    ttk.Button(root, text="Open Course", command=open_selected_course).pack(pady=10)

    gpa_label = tk.Label(root, text="", font=("Arial", 12))
    gpa_label.pack(pady=10)

    ttk.Button(root, text="Calculate Semester GPA", command=calculate_gpa).pack(pady=5)

    status_label = tk.Label(root, text="", font=("Arial", 10))
    status_label.pack(pady=5)

    root.mainloop()
