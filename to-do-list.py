import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3 as sql


def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values (?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')


def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)


def delete_task():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
            the_cursor.execute(
                'delete from tasks where title = ?', (the_value,))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')


def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box:
        tasks.clear()
        the_cursor.execute('delete from tasks')
        list_update()


def clear_list():
    task_listbox.delete(0, 'end')


def close():
    print(tasks)
    guiWindow.destroy()


def retrieve_database():
    tasks.clear()
    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])


if __name__ == "__main__":
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List Manager")
    guiWindow.geometry("600x600+600+200")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#3498DB")  # Blue background

    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')

    tasks = []

    header_frame = tk.Frame(guiWindow, bg="#2980B9")  # Dark blue header
    functions_frame = tk.Frame(guiWindow, bg="#3498DB")
    listbox_frame = tk.Frame(guiWindow, bg="#3498DB")

    header_frame.pack(fill="both")
    functions_frame.pack(side="left", expand=True, fill="both")
    listbox_frame.pack(side="right", expand=True, fill="both")

    header_label = ttk.Label(
        header_frame,
        text="To-Do List",
        font=("Arial", 36, "bold"),
        background="#2980B9",
        foreground="#FFFFFF"
    )
    header_label.pack(padx=20, pady=20)

    task_label = ttk.Label(
        functions_frame,
        text="Enter a Task:",
        font=("Arial", 14),
        background="#3498DB",
        foreground="#FFFFFF"
    )
    task_label.place(x=30, y=40)

    task_field = ttk.Entry(
        functions_frame,
        font=("Arial", 14),
        width=20,
        background="#ECF0F1",  # Light gray
        foreground="#333333"
    )
    task_field.place(x=30, y=80)

    add_button = ttk.Button(
        functions_frame,
        text="Add Task",
        width=20,
        command=add_task,
        style="TButton"
    )
    del_button = ttk.Button(
        functions_frame,
        text="Delete Task",
        width=20,
        command=delete_task,
        style="TButton"
    )
    del_all_button = ttk.Button(
        functions_frame,
        text="Delete All Tasks",
        width=20,
        command=delete_all_tasks,
        style="TButton"
    )
    exit_button = ttk.Button(
        functions_frame,
        text="Exit",
        width=20,
        command=close,
        style="TButton"
    )
    add_button.place(x=30, y=130)
    del_button.place(x=30, y=180)
    del_all_button.place(x=30, y=230)
    exit_button.place(x=30, y=280)

    task_listbox = tk.Listbox(
        listbox_frame,
        width=30,
        height=15,
        selectmode='SINGLE',
        background="#ECF0F1",
        foreground="#333333",
        selectbackground="#2980B9",
        selectforeground="#FFFFFF"
    )
    task_listbox.place(x=10, y=20)

    retrieve_database()
    list_update()
    guiWindow.mainloop()
    the_connection.commit()
    the_cursor.close()
