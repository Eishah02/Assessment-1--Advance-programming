import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import os
import sys

FNAME = "studentMarks.txt"
MAX_TOTAL = 160
MAX_EXAM = 100
MAX_COURSEWORK = 60


def get_grade(percent):
    #Calculates the final grade using if elif else chain.
    if percent >= 70:
        return "A"
    elif percent >= 60:
        return "B"
    elif percent >= 50:
        return "C"
    elif percent >= 40:
        return "D"
    else:
        return "F"


def calculate_stats(student):
    #Calculates derived values and returns a complete dictionary.
    cw_total = student["c1"] + student["c2"] + student["c3"]
    overall = cw_total + student["exam"]
    percent = (overall / MAX_TOTAL) * 100
    grade = get_grade(percent)

    student["cw_total"] = cw_total
    student["overall"] = overall
    student["percent"] = percent
    student["grade"] = grade
    return student


def parse_line_to_student(line):
    #Parses a single line from the file into a student dictionary.
    parts = [p.strip() for p in line.strip().split(",")]
    if len(parts) < 6:
        return None

    try:
        code = int(parts[0])
        name = parts[1]
        c_marks = [int(p) for p in parts[2:5]]
        exam = int(parts[5])

        student = {
            "code": code,
            "name": name,
            "c1": c_marks[0],
            "c2": c_marks[1],
            "c3": c_marks[2],
            "exam": exam,
        }
        return calculate_stats(student)
    except ValueError:
        return None


def load_data(fname):
    #Reads data from the file and loads it into a list of dicts.
    students=[]
    if not os.path.exists(fname):
        messagebox.showerror("File Error", f"'{fname}' not found.")
        return students

    with open(fname, "r", encoding="utf-8") as f:
        f.readline().strip()
        for line in f:
            student = parse_line_to_student(line)
            if student:
                students.append(student)

    return students


def save_data(fname, students):
    #Rewrites the entire file with the current student data.
    with open(fname, "w", encoding="utf-8") as f:
        f.write(f"{len(students)}\n")
        for s in students:
            line = f"{s['code']},{s['name']},{s['c1']},{s['c2']},{s['c3']},{s['exam']}\n"
            f.write(line)


def fmt_student(s):
    return (
        f"Student Record\n"
        f"Name:{s['name']}\n"
        f"Student Number:{s['code']}\n"
        f"Coursework (P1,P2,P3):{s['c1']},{s['c2']},{s['c3']}\n"
        f"Total Coursework Mark:{s['cw_total']}/{MAX_COURSEWORK}\n"
        f"Exam Mark:{s['exam']}/{MAX_EXAM}\n"
        f"Overall Score (out of {MAX_TOTAL}):{s['overall']}\n"
        f"Overall Percentage:{s['percent']:.2f}%\n"
        f"Grade:{s['grade']}\n"
        f"\n"
    )


def find_student_by_id(students, search_id):
    #Searches for a student by code.
    for s in students:
        if s["code"]==search_id:
            return s
    return None


class StudentApp:
    def __init__(self, root):
        self.root = root
        root.title("Student Marks Manager")
        root.geometry("1050x580")
        self.students = load_data(FNAME)

        left = tk.Frame(root, padx=10, pady=10)
        left.pack(side="left", fill="y")

        tk.Label(left, text="Students(Roll No. | Name)", font=("Arial", 11, "bold")).pack(pady=5)

        list_frame = tk.Frame(left)
        list_frame.pack(side="top",fill="y",expand=True)

        self.lb = tk.Listbox(list_frame,width=45,height=22,font=("Consolas", 11))
        self.lb.pack(side="left", fill="y")

        sb = tk.Scrollbar(list_frame,command=self.lb.yview)
        sb.pack(side="right",fill="y")
        self.lb.config(yscrollcommand=sb.set)
        self.lb.bind("<<ListboxSelect>>", self.on_select)

        right = tk.Frame(root, padx=10, pady=10)
        right.pack(side="right",fill="both",expand=True)

        self.text = scrolledtext.ScrolledText(right,wrap="word",font=("Consolas", 11))
        self.text.pack(fill="both",expand=True)

        btns_top = tk.Frame(right)
        btns_top.pack(fill="x",pady=5)

        tk.Button(btns_top, text="1. View All", command=self.view_all, width=12).pack(side="left", padx=3)
        tk.Button(btns_top, text="2. Search", command=self.search_student, width=12).pack(side="left", padx=3)
        tk.Button(btns_top, text="3. Highest", command=lambda: self.find_extreme(True), width=12).pack(side="left", padx=3)
        tk.Button(btns_top, text="4. Lowest", command=lambda: self.find_extreme(False), width=12).pack(side="left", padx=3)
        tk.Button(btns_top, text="5. Sort", command=self.sort_records, width=12).pack(side="left", padx=3)

        btns_bottom = tk.Frame(right)
        btns_bottom.pack(fill="x", pady=5)

        tk.Button(btns_bottom, text="6. Add Student", command=self.add_student, width=12).pack(side="left", padx=3)
        tk.Button(btns_bottom, text="7. Delete Student", command=self.delete_student, width=12).pack(side="left", padx=3)
        tk.Button(btns_bottom, text="8. Update Student", command=self.update_student, width=12).pack(side="left", padx=3)
        tk.Button(btns_bottom, text="Reload File", command=self.reload, width=12).pack(side="right", padx=3)

        self.populate_listbox()
        if self.students:
            self.lb.selection_set(0)
            self.on_select()


    def populate_listbox(self):
        self.lb.delete(0, tk.END)
        for s in self.students:
            self.lb.insert(tk.END, f"{s['code']} | {s['name']}")

    def on_select(self, event=None):
        selected_indices = self.lb.curselection()
        if selected_indices:
            index = selected_indices[0]
            student = self.students[index]
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, fmt_student(student))

    def show_not_implemented(self):
        messagebox.showinfo()

    def view_all(self):
        self.show_not_implemented()
        #logic for viewing all students 

    def search_student(self):
        self.show_not_implemented()
        #logic for searching

    def find_extreme(self, is_highest):
        self.show_not_implemented()
        #logic for finding highest-lowest 
        
    def sort_records(self):
        self.show_not_implemented()
        #logic for sorting 

    def add_student(self):
        self.show_not_implemented()
        #logic for adding a student 

    def delete_student(self):
        self.show_not_implemented()
        #logic for deleting a student 

    def update_student(self):
        self.show_not_implemented()
        #logic for updating a student 
    def reload(self):
        self.students = load_data(FNAME)
        self.populate_listbox()
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END)


if __name__ == "__main__":  
    root = tk.Tk() 
    app = StudentApp(root)
    root.mainloop()   