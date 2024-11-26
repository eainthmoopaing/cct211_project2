import tkinter as tk
from tkinter import ttk
from semester import open_semester_window

semesters = set()

def main_window():
    def add_semester():
        semester_name = semester_entry.get().strip()
        if not semester_name:
            status_label.config(text="Semester name cannot be empty!", fg="red")
        elif semester_name in semesters:
            status_label.config(text="Semester already exists!", fg="red")
        else:
            semesters.add(semester_name)
            status_label.config(text=f"Added '{semester_name}' successfully!", fg="green")
            semester_list.insert(tk.END, semester_name)

    def open_selected_semester():
        selected = semester_list.curselection()
        if selected:
            semester_name = semester_list.get(selected[0])
            root.destroy()
            open_semester_window(semester_name)
        else:
            status_label.config(text="Please select a semester!", fg="red")

    root = tk.Tk()
    root.title("GPA Calculator - Semesters")
    root.geometry("400x400")

    tk.Label(root, text="Add Semester", font=("Arial", 14, "bold")).pack(pady=10)
    semester_entry = ttk.Entry(root, width=30)
    semester_entry.pack(pady=5)

    ttk.Button(root, text="Add Semester", command=add_semester).pack(pady=5)

    tk.Label(root, text="Semesters List", font=("Arial", 14, "bold")).pack(pady=10)
    semester_list = tk.Listbox(root, width=30, height=10)
    semester_list.pack(pady=5)

    ttk.Button(root, text="Open Semester", command=open_selected_semester).pack(pady=10)

    status_label = tk.Label(root, text="", font=("Arial", 10))
    status_label.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main_window()
