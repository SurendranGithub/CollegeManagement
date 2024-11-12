from tkinter import *
import sqlite3
import tkinter as tk
from PIL import ImageTk, Image

connect = sqlite3.connect('college.db')
c = connect.cursor()

# faculty ("name" TEXT, "id" TEXT, "department" TEXT, "designation"	TEXT, "phonenumber" INTEGER, "address"	TEXT);

# student ("name" TEXT, "id" TEXT, "department" TEXT, "cgpa" TEXT, "dob" TEXT, "phonenumber" INTEGER, "address"	TEXT);

# General declarations =>
activeBackgroundColor = '#199ff3'
activeForeColor = 'black'
bgCol = 'skyblue'
bgCol2 = '#199ff3'
command = 0
LabelAlign = 'e'
formPadY = 7

root = tk.Tk()
root.title("College Management System - Imagine ChildWorks")
root.geometry("1000x600")
root.config(bg='black')
root.resizable(False, False)


def DisplayStudentDB(studentDBDisplayFrame, condition = ""):

    for widget in studentDBDisplayFrame.winfo_children():
        widget.destroy()
    
    if condition == "":
        c.execute("select * from student;")
        student = c.fetchall()
    else:
        try:
            cmd = "select * from student where " + condition + " ;"
            c.execute(cmd)
            student = c.fetchall()
        except:
            print("Invalid command")

    Label(studentDBDisplayFrame, text="Name").grid(row=0, column=0, ipadx=58)
    Label(studentDBDisplayFrame, text="ID").grid(row=0, column=1, ipadx=20)
    Label(studentDBDisplayFrame, text="Department").grid(row=0, column=2, ipadx=10)
    Label(studentDBDisplayFrame, text="Date of Birth").grid(row=0, column=3, ipadx=10)
    Label(studentDBDisplayFrame, text="CGPA").grid(row=0, column=4, ipadx=10)
    Label(studentDBDisplayFrame, text="Phone number").grid(row=0, column=5, ipadx=20)
    Label(studentDBDisplayFrame, text="Address").grid(row=0, column=6, ipadx=40)
    try:
        for i, student in enumerate(student):
            Label(studentDBDisplayFrame, text=student[0], bg=bgCol2).grid(row=i + 1, column=0)
            Label(studentDBDisplayFrame, text=student[1], bg=bgCol2).grid(row=i + 1, column=1)
            Label(studentDBDisplayFrame, text=student[2], bg=bgCol2).grid(row=i + 1, column=2)
            Label(studentDBDisplayFrame, text=student[3], bg=bgCol2).grid(row=i + 1, column=3)
            Label(studentDBDisplayFrame, text=student[4], bg=bgCol2).grid(row=i + 1, column=4)
            Label(studentDBDisplayFrame, text=student[5], bg=bgCol2).grid(row=i + 1, column=5)
            Label(studentDBDisplayFrame, text=student[6], bg=bgCol2).grid(row=i + 1, column=6)
    except:
        pass

def addStudent():
    name = nameEntry.get()
    id = idEntry.get()
    department = departmentEntry.get()
    cgpa = cgpaEntry.get()
    dob = dobEntry.get()
    phonenumber = phonenumberEntry.get()
    address = addressEntry.get()

    check = 1 if all(e != "" for e in [name, id, department, cgpa, dob, phonenumber, address]) else 0
    if check == 1:
        cmd = "insert into student(name, id, department, cgpa, dob, phonenumber, address) values ('" + name + "', '" + id + "', '" + department + "', '" + cgpa + "', '" + dob + "', " + phonenumber + ", '" + address + "');"

        c.execute(cmd)
        connect.commit()

        nameEntry.delete(0, END)
        idEntry.delete(0, END)
        departmentEntry.delete(0, END)
        cgpaEntry.delete(0, END)
        dobEntry.delete(0, END)
        phonenumberEntry.delete(0, END)
        addressEntry.delete(0, END)

        DisplayStudentDB(studentDBDisplayFrame)

def delete(table, id):
    cmd = "delete from " + table + " where id='" + id + "';"
    c.execute(cmd)
    connect.commit()
    DisplayStudentDB(studentDBDisplayFrame)
    DisplayFacultyDB(facultyDBDisplayFrame)

def deleteStudent():
    del_win = Toplevel(root)
    del_win.title("Delete a Student")
    del_win.geometry("300x150")
    del_win.config(bg=bgCol)

    entryLabel = Label(del_win, text="Enter the student id :", bg=bgCol)
    entryLabel.place(x=80, y=30)
    idEntry = Entry(del_win)
    idEntry.place(x=83, y=60)
    delButton = Button(del_win, text="Delete", command=lambda: delete("student", idEntry.get()))
    delButton.place(x=120, y=90)

def DisplayFacultyDB(facultyDBDisplayFrame, condition = ""):
    for widget in facultyDBDisplayFrame.winfo_children():
        widget.destroy()
    
    if condition == "":
        c.execute("select * from faculty;")
        faculty = c.fetchall()
    else:
        try:
            cmd = "select * from faculty where " + condition + " ;"
            c.execute(cmd)
            faculty = c.fetchall()
        except:
            print("Invalid command")

    Label(facultyDBDisplayFrame, text="Name").grid(row=0, column=0, ipadx=55)
    Label(facultyDBDisplayFrame, text="ID").grid(row=0, column=1, ipadx=20)
    Label(facultyDBDisplayFrame, text="Department").grid(row=0, column=2, ipadx=20)
    Label(facultyDBDisplayFrame, text="Designation").grid(row=0, column=3, ipadx=25)
    Label(facultyDBDisplayFrame, text="Phone number").grid(row=0, column=4, ipadx=25)
    Label(facultyDBDisplayFrame, text="Address").grid(row=0, column=5, ipadx=45)
    try:
        for i, faculty in enumerate(faculty):
            Label(facultyDBDisplayFrame, text=faculty[0], bg=bgCol2).grid(row=i + 1, column=0)
            Label(facultyDBDisplayFrame, text=faculty[1], bg=bgCol2).grid(row=i + 1, column=1)
            Label(facultyDBDisplayFrame, text=faculty[2], bg=bgCol2).grid(row=i + 1, column=2)
            Label(facultyDBDisplayFrame, text=faculty[3], bg=bgCol2).grid(row=i + 1, column=3)
            Label(facultyDBDisplayFrame, text=faculty[4], bg=bgCol2).grid(row=i + 1, column=4)
            Label(facultyDBDisplayFrame, text=faculty[5], bg=bgCol2).grid(row=i + 1, column=5)
    except:
        pass

def addFaculty():
    name = facultyNameEntry.get()
    id = facultyIdEntry.get()
    department = facultyDepartmentEntry.get()
    designation = facultyDesignationEntry.get()
    phonenumber = facultyPhonenumberEntry.get()
    address = facultyAddressEntry.get()

    check = 1 if all(e != "" for e in [name, id, department, designation, phonenumber, address]) else 0
    if check == 1:
        cmd = "insert into faculty(name, id, department, designation, phonenumber, address) values ('" + name + "', '" + id + "', '" + department + "', '"  + designation + "', " + phonenumber + ", '" + address + "');"

        c.execute(cmd)
        connect.commit()

        facultyNameEntry.delete(0, END)
        facultyIdEntry.delete(0, END)
        facultyDepartmentEntry.delete(0, END)
        facultyDesignationEntry.delete(0, END)
        facultyPhonenumberEntry.delete(0, END)
        facultyAddressEntry.delete(0, END)

        DisplayFacultyDB(facultyDBDisplayFrame)

def deleteFaculty():
    del_win = Toplevel(root)
    del_win.title("Delete a Faculty")
    del_win.geometry("300x150")
    del_win.config(bg=bgCol)

    entryLabel = Label(del_win, text="Enter the faculty id :", bg=bgCol)
    entryLabel.place(x=80, y=30)
    idEntry = Entry(del_win)
    idEntry.place(x=83, y=60)
    delButton = Button(del_win, text="Delete", command=lambda: delete("faculty", idEntry.get()))
    delButton.place(x=120, y=90)

# Changing the category frame
def ChangeCategoryFrame(status, fb, sb, sf, ff, sdb, fdb):
    global command
    if status != command:
        if command == 0:
            fb.config(bg=activeBackgroundColor, fg=activeForeColor)
            sb.config(bg='white', fg='black')
            ff.place(x=40, y=0)
            sf.place_forget()
            fdb.place(x=0, y=0)
            sdb.place_forget()
            command = 1
        else:
            fb.config(bg='white', fg='black')
            sb.config(bg=activeBackgroundColor, fg=activeForeColor)
            sf.place(x=40, y=0)
            ff.place_forget()
            fdb.place_forget()
            sdb.place(x=0, y=0)
            command = 0

# Frame =>
leftFrame = Frame(root, height=600, width=300, bg='black')
leftFrame.place(x=0, y=0)
rightFrame = Frame(root, height=600, width=700, bg=bgCol)
rightFrame.place(x=301, y=0)

# leftFrame definition =>
titleFrame = Frame(leftFrame, height=250, width=300, bg=bgCol)
titleFrame.place(x=0, y=0)
commandFrame = Frame(leftFrame, height=350, width=300, bg=activeBackgroundColor)
commandFrame.place(x=0, y=251)

# titleFrame definition =>
logo = ImageTk.PhotoImage(Image.open("Imagine_ChildWorks.jpg").resize((200, 200)))
logoLabel = Label(titleFrame, image=logo)
logoLabel.place(x=50, y=10)
categoryFrame = Frame(titleFrame, height=50, width=300)
categoryFrame.place(x=0, y=225)
studentButton = Button(categoryFrame, text="Student", padx=30, bg=activeBackgroundColor, fg=activeForeColor, command=lambda: ChangeCategoryFrame(0, facultyButton, studentButton, studentFrame, facultyFrame, studentDBFrame, facultyDBFrame))
studentButton.grid(row=0, column=0, ipadx=21)
facultyButton = Button(categoryFrame, text="Faculty", padx=30, command=lambda: ChangeCategoryFrame(1, facultyButton, studentButton, studentFrame, facultyFrame, studentDBFrame, facultyDBFrame))
facultyButton.grid(row=0, column=1, ipadx=21)

# commandFrame definition =>
studentFrame = Frame(commandFrame, height=350, width=260, bg=activeBackgroundColor)
studentFrame.place(x=40, y=0)
facultyFrame = Frame(commandFrame, height=350, width=260, bg=activeBackgroundColor)

# studentFrame definition =>
nameLabel = Label(studentFrame, text="Name : ", bg=bgCol2).grid(row=0, column=0, sticky=LabelAlign, pady=formPadY)
nameEntry = Entry(studentFrame)
nameEntry.grid(row=0, column=1)
idLabel = Label(studentFrame, text="ID : ", bg=bgCol2).grid(row=1, column=0, sticky=LabelAlign, pady=formPadY)
idEntry = Entry(studentFrame)
idEntry.grid(row=1, column=1)
dobLabel = Label(studentFrame, text="Date of Birth : ", bg=bgCol2).grid(row=2, column=0, sticky=LabelAlign, pady=formPadY)
dobEntry = Entry(studentFrame)
dobEntry.grid(row=2, column=1)
departmentLabel = Label(studentFrame, text="Department : ", bg=bgCol2).grid(row=3, column=0, sticky=LabelAlign, pady=formPadY)
departmentEntry = Entry(studentFrame)
departmentEntry.grid(row=3, column=1)
cgpaLabel = Label(studentFrame, text="CGPA : ", bg=bgCol2).grid(row=4, column=0, sticky=LabelAlign, pady=formPadY)
cgpaEntry = Entry(studentFrame)
cgpaEntry.grid(row=4, column=1)
phonenumberLabel = Label(studentFrame, text="Phone number : ", bg=bgCol2).grid(row=5, column=0, sticky=LabelAlign, pady=formPadY)
phonenumberEntry = Entry(studentFrame)
phonenumberEntry.grid(row=5, column=1)
addressLabel = Label(studentFrame, text="Address : ", bg=bgCol2).grid(row=6, column=0, sticky=LabelAlign, pady=formPadY)
addressEntry = Entry(studentFrame)
addressEntry.grid(row=6, column=1)

submitButton = Button(studentFrame, text="Submit", padx=20, command=addStudent)
submitButton.grid(row=7, column=0, columnspan=2, sticky='', pady=formPadY+10)
deleteButton = Button(studentFrame, text="Delete a student record", padx=50, command=deleteStudent)
deleteButton.grid(row=8, column=0, columnspan=2, pady=formPadY-5)

# facultyFrame definition =>
facultyNameLabel = Label(facultyFrame, text="Name : ", bg=bgCol2).grid(row=0, column=0, sticky=LabelAlign, pady=formPadY)
facultyNameEntry = Entry(facultyFrame)
facultyNameEntry.grid(row=0, column=1)
facultyIdLabel = Label(facultyFrame, text="ID : ", bg=bgCol2).grid(row=1, column=0, sticky=LabelAlign, pady=formPadY)
facultyIdEntry = Entry(facultyFrame)
facultyIdEntry.grid(row=1, column=1)
facultyDepartmentLabel = Label(facultyFrame, text="Department : ", bg=bgCol2).grid(row=2, column=0, sticky=LabelAlign, pady=formPadY)
facultyDepartmentEntry = Entry(facultyFrame)
facultyDepartmentEntry.grid(row=2, column=1)
facultyDesignationLabel = Label(facultyFrame, text="Designation : ", bg=bgCol2).grid(row=3, column=0, sticky=LabelAlign, pady=formPadY)
facultyDesignationEntry = Entry(facultyFrame)
facultyDesignationEntry.grid(row=3, column=1)
facultyPhonenumberLabel = Label(facultyFrame, text="Phone number : ", bg=bgCol2).grid(row=4, column=0, sticky=LabelAlign, pady=formPadY)
facultyPhonenumberEntry = Entry(facultyFrame)
facultyPhonenumberEntry.grid(row=4, column=1)
facultyAddressLabel = Label(facultyFrame, text="Address : ", bg=bgCol2).grid(row=5, column=0, sticky=LabelAlign, pady=formPadY)
facultyAddressEntry = Entry(facultyFrame)
facultyAddressEntry.grid(row=5, column=1)

facultySubmitButton = Button(facultyFrame, text="Submit", padx=20, command=addFaculty)
facultySubmitButton.grid(row=6, column=0, columnspan=2, sticky='', pady=formPadY+10)
facultyDeleteButton = Button(facultyFrame, text="Delete a faculty record", padx=52, command=deleteFaculty)
facultyDeleteButton.grid(row=7, column=0, columnspan=2, pady=formPadY-5)

# rightFrame definition =>
studentDBFrame = Frame(rightFrame, height=600, width=700, bg=bgCol2)
studentDBFrame.place(x=0, y=0)
facultyDBFrame = Frame(rightFrame, height=600, width=700, bg=bgCol2)

# studentDBFrame definition =>
studentQueryFrame = Frame(studentDBFrame, height=130, width=700, bg=bgCol)
studentQueryFrame.place(x=0, y=0)
studentDBLabel = Label(studentQueryFrame, text="Enter SQL query here (select * from student where ______ ;)", bg=bgCol)
studentDBLabel.place(x=50, y=40)
studentDBEntry = Entry(studentQueryFrame, width=80)
studentDBEntry.place(x=50, y=70)
EntryEnterButton = Button(studentQueryFrame, text="Search", borderwidth=0, bg=bgCol, command=lambda: DisplayStudentDB(studentDBDisplayFrame, studentDBEntry.get()))
EntryEnterButton.place(x=545, y=70)
ResetButton = Button(studentQueryFrame, text="Reset", borderwidth=0, bg=bgCol, command=lambda: [DisplayStudentDB(studentDBDisplayFrame), studentDBEntry.delete(0, END)])
ResetButton.place(x=600, y=70)

studentDBDisplayFrame = Frame(studentDBFrame, height=470, width=700, bg=bgCol2)
studentDBDisplayFrame.place(x=0, y=131)

DisplayStudentDB(studentDBDisplayFrame)

# facultyDBFrame definition =>
facultyQueryFrame = Frame(facultyDBFrame, height=130, width=700, bg=bgCol)
facultyQueryFrame.place(x=0, y=0)
facultyDBLabel = Label(facultyQueryFrame, text="Enter SQL query here (select * from faculty where ______ ;)", bg=bgCol)
facultyDBLabel.place(x=50, y=40)
facultyDBEntry = Entry(facultyQueryFrame, width=80)
facultyDBEntry.place(x=50, y=70)
EntryEnterButton = Button(facultyQueryFrame, text="Search", borderwidth=0, bg=bgCol, command=lambda: DisplayFacultyDB(facultyDBDisplayFrame, facultyDBEntry.get()))
EntryEnterButton.place(x=545, y=70)
ResetButton = Button(facultyQueryFrame, text="Reset", borderwidth=0, bg=bgCol, command=lambda: [DisplayFacultyDB(facultyDBDisplayFrame), facultyDBEntry.delete(0, END)])
ResetButton.place(x=600, y=70)

facultyDBDisplayFrame = Frame(facultyDBFrame, height=470, width=700, bg=bgCol2)
facultyDBDisplayFrame.place(x=0, y=131)

DisplayFacultyDB(facultyDBDisplayFrame)

root.mainloop()
connect.close()

# Imagine ChildWorks