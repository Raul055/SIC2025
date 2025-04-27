import tkinter as tk
import webbrowser
import mysql.connector
from tkinter import messagebox
from api_handler import fetch_gene_info
from db_handler import insert_data_db

# Global to hold DB credentials
db_config = {}

def open_id_window():
    id_window = tk.Toplevel()
    id_window.title("Insert Gene ID")
    id_window.geometry("300x150")

    tk.Label(id_window, text="Enter Gene ID:").pack(pady=5)
    gene_id_entry = tk.Entry(id_window)
    gene_id_entry.pack()

    # ⬇️ Informational text
    tk.Label(id_window, text="Check for gene IDs").pack(pady=(10, 0))

    # ⬇️ Clickable link
    link = tk.Label(id_window, text="NCBI Gene Database", fg="blue", cursor="hand2")
    link.pack()
    link.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.ncbi.nlm.nih.gov/gene"))


    def fetch_and_insert():
        gene_id = gene_id_entry.get()
        try:
            fetch_gene_info(gene_id)
            insert_data_db(db_config["host"],
                           db_config["port"],
                           db_config["user"],
                           db_config["password"],
                           db_config["database"])
            messagebox.showinfo("Success", "Data inserted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")

    tk.Button(id_window, text="Submit", command=fetch_and_insert).pack(pady=10)

def login():
    '''
    host = localhost
    port = 3306
    user = alumno
    password = Pce@6ooAdH
    '''
    
    host = host_entry.get()
    port = port_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    database = database_entry.get()
    
    try:
        conn = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            auth_plugin='mysql_native_password'
        )
        conn.close()
        # Save credentials
        db_config["host"] = host
        db_config["port"] = port
        db_config["user"] = user
        db_config["password"] = password
        db_config["database"] = database

        root.withdraw()
        messagebox.showinfo("Success", "Connected to database.")
        open_id_window()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", str(err))

root = tk.Tk()
root.title("API to Database")

# Host
tk.Label(root, text="Host:").pack()
host_entry = tk.Entry(root)
host_entry.pack()

# Port
tk.Label(root, text="Port:").pack()
port_entry = tk.Entry(root)
port_entry.pack()

# User
tk.Label(root, text="User:").pack()
user_entry = tk.Entry(root)
user_entry.pack()

# Password
tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root)
password_entry.pack()

# Database
tk.Label(root, text="Database:").pack()
database_entry = tk.Entry(root)
database_entry.pack()

# Run Button
tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()
