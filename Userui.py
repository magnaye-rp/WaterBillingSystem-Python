import mysql.connector
import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk
from invoicePopup import *


class UserUI:
    def __init__(self, user_id):
        self.user_id = user_id
        self.root = ctk.CTk()
        self.root.title("Water Billing System")
        self.root.geometry("1000x562")

        self.create_widgets()
        self.fetch_data_from_database()
        self.root.mainloop()

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(self.root, text="WATER BILLING SYSTEM", font=("Rockwell Extra Bold", 24))
        self.title_label.place(x=270, y=10)

        self.user_info_table = ttk.Treeview(self.root, columns=("Column Name", "Value"), show="headings")
        self.user_info_table.heading("Column Name", text="Column Name")
        self.user_info_table.heading("Value", text="Value")
        self.user_info_table.place(x=70, y=40, width=820, height=180)

        self.ledger_table = ttk.Treeview(self.root, columns=("LedgerID", "BillingID", "AmountPaid", "PaymentDate"),
                                         show="headings")
        self.ledger_table.heading("LedgerID", text="LedgerID")
        self.ledger_table.heading("BillingID", text="BillingID")
        self.ledger_table.heading("AmountPaid", text="AmountPaid")
        self.ledger_table.heading("PaymentDate", text="PaymentDate")
        self.ledger_table.place(x=70, y=220, width=820, height=150)

        self.bills_table = ttk.Treeview(self.root,
                                        columns=("BillingID", "DebtID", "ChargeID", "BillingAmount", "DueDate"),
                                        show="headings")
        self.bills_table.heading("BillingID", text="BillingID")
        self.bills_table.heading("DebtID", text="DebtID")
        self.bills_table.heading("ChargeID", text="ChargeID")
        self.bills_table.heading("BillingAmount", text="BillingAmount")
        self.bills_table.heading("DueDate", text="DueDate")
        self.bills_table.place(x=70, y=370, width=820, height=140)

        self.print_invoice_button = ctk.CTkButton(self.root, text="Print Invoice", font=("Nirmala UI Semilight", 14),
                                                  command=self.print_invoice)
        self.print_invoice_button.place(x=400, y=520)

    def fetch_data_from_database(self):
        try:
            conn = mysql.connector.connect(
            host="localhost",
            user="WBSAdmin",
            password="WBS_@dmn.root",
            database="wbs"
        )

            cursor = conn.cursor()

            query = """
                SELECT A.SerialID, A.FirstName, A.LastName, A.Address, A.ContactNumber, A.Email, A.MeterID, B.PresentReading, 
                B.ReadingDate, B.PreviousReading, B.PreviousReadingDate, B.Consumption, C.ConcessionaireName, C.PricePerCubicMeter, 
                D.Name as InspectorName, D.ContactNumber 
                FROM consumerinfo A 
                JOIN watermeter B ON A.MeterID = B.MeterID 
                JOIN concessionaire C ON B.ConcessionaireID = C.ConcessionaireID 
                JOIN meterinspector D ON D.InspectorID = A.InspectorID 
                WHERE A.SerialID = %s AND A.isConnected = 1;
            """
            cursor.execute(query, (self.user_id,))
            rows = cursor.fetchall()

            for row in rows:
                for col_name, value in zip(cursor.description, row):
                    self.user_info_table.insert("", "end", values=(col_name[0], value))

            query = "SELECT LedgerID, BillingID, AmountPaid, PaymentDate FROM ledger WHERE SerialID = %s"
            cursor.execute(query, (self.user_id,))
            rows = cursor.fetchall()

            for row in rows:
                self.ledger_table.insert("", "end", values=row)

            query = "SELECT BillingID, DebtID, ChargeID, BillingAmount, DueDate FROM bill WHERE SerialID = %s AND isPaid = 0"
            cursor.execute(query, (self.user_id,))
            rows = cursor.fetchall()

            for row in rows:
                self.bills_table.insert("", "end", values=row)

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    def print_invoice(self):
        selected_item = self.bills_table.selection()
        if selected_item:
            bill_id = self.bills_table.item(selected_item, 'values')[0]
            print(f"Generating invoice for BillingID: {bill_id}")
            InvoicePopup(self.root, bill_id)
        else:
            messagebox.showwarning("Selection Error", "Please select a row to print the invoice.")
