import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3  # or use another database connector, e.g., MySQLdb for MySQL
import logging

# Set up logging for error messages
logging.basicConfig(level=logging.ERROR)

class UserUI:
    def __init__(self, ID):
        self.ID = ID
        self.window = tk.Tk()
        self.window.title("User Interface")
        self.create_widgets()
        self.fetch_data_from_database()

    def create_widgets(self):
        self.jLabel3 = tk.Label(self.window, text="Payment Method", font=("STKaiti", 20, "italic"))
        self.jLabel3.grid(row=0, column=1, pady=10)

        # Create Entry fields, Labels, ComboBox, and Buttons
        self.jLabel4 = tk.Label(self.window, text="Amount:")
        self.jLabel4.grid(row=1, column=0)

        self.jTextField1 = tk.Entry(self.window)
        self.jTextField1.grid(row=1, column=1)

        self.jComboBox1 = ttk.Combobox(self.window, values=["Gcash", "Maya", "Visa/Bancnet"])
        self.jComboBox1.grid(row=2, column=1)

        self.jButton5 = tk.Button(self.window, text="Add Credit", command=self.add_credit)
        self.jButton5.grid(row=3, column=1, pady=10)

        self.jButton4 = tk.Button(self.window, text="Print Invoice", command=self.print_invoice)
        self.jButton4.grid(row=4, column=1, pady=10)

        # Table for user info
        self.user_info_table = ttk.Treeview(self.window)
        self.user_info_table.grid(row=5, column=0, columnspan=3)
        self.user_info_table["columns"] = ("Column Name", "Value")
        self.user_info_table.heading("#1", text="Column Name")
        self.user_info_table.heading("#2", text="Value")

        # Table for ledger info
        self.ledger_table = ttk.Treeview(self.window)
        self.ledger_table.grid(row=6, column=0, columnspan=3)
        self.ledger_table["columns"] = ("Billing ID", "Amount Paid", "Payment Date")
        self.ledger_table.heading("#1", text="Billing ID")
        self.ledger_table.heading("#2", text="Amount Paid")
        self.ledger_table.heading("#3", text="Payment Date")

        self.window.mainloop()

    def fetch_data_from_database(self):
        try:
            conn = sqlite3.connect('your_database.db')  # Replace with the appropriate database connection
            self.populate_vertical_table(conn)
            self.populate_horizontal_table(conn)
        except sqlite3.Error as e:
            logging.error(f"Error: {e}")
            messagebox.showerror("Database Error", f"Error: {e}")

    def populate_vertical_table(self, conn):
        try:
            query = """SELECT Column1, Column2 FROM Table WHERE ID = ?"""
            cursor = conn.cursor()
            cursor.execute(query, (self.ID,))
            rows = cursor.fetchall()

            for row in rows:
                self.user_info_table.insert("", "end", values=row)
        except sqlite3.Error as e:
            logging.error(f"Error: {e}")
            messagebox.showerror("Database Error", f"Error: {e}")

    def populate_horizontal_table(self, conn):
        try:
            query = """SELECT BillingID, AmountPaid, PaymentDate FROM Ledger WHERE ID = ?"""
            cursor = conn.cursor()
            cursor.execute(query, (self.ID,))
            rows = cursor.fetchall()

            for row in rows:
                self.ledger_table.insert("", "end", values=row)
        except sqlite3.Error as e:
            logging.error(f"Error: {e}")
            messagebox.showerror("Database Error", f"Error: {e}")

    def add_credit(self):
        # Functionality for adding credit
        messagebox.showinfo("Credit", "Credit Added Successfully")

    def print_invoice(self):
        selected_item = self.ledger_table.selection()
        if selected_item:
            invoice_id = self.ledger_table.item(selected_item)["values"][0]
            self.print_invoice_popup(invoice_id)
        else:
            messagebox.showwarning("Selection", "Please select a row.")

    def print_invoice_popup(self, invoice_id):
        # Open a new window or pop-up to print invoice
        invoice_popup = tk.Toplevel(self.window)
        invoice_popup.title(f"Invoice for {invoice_id}")
        invoice_label = tk.Label(invoice_popup, text=f"Invoice Details for {invoice_id}")
        invoice_label.pack()


# Replace this with actual user ID you want to pass
user_ui = UserUI("user123")
