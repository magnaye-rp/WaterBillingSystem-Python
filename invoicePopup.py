import tkinter as tk
from tkinter import messagebox, Scrollbar
from tkinter import ttk
import sqlite3
from decimal import Decimal

class InvoicePopup(tk.Toplevel):

    def __init__(self, parent, billing_id):
        super().__init__(parent)
        self.title("Invoice Details")
        self.geometry("500x700")
        self.resizable(False, False)
        self.fetch_and_display_invoice(billing_id)

    def fetch_and_display_invoice(self, billing_id):
        # Create dictionaries to store the fetched data
        consumer_data = {}
        billing_data = {}
        payment_data = {}
        meter_data = {}
        concessionaire_data = {}

        try:
            # Connect to the database
            con = sqlite3.connect("your_database.db")
            cursor = con.cursor()

            # Fetch Consumer Information using BillingID
            cursor.execute("SELECT FirstName, LastName, Address, Email FROM consumerinfo WHERE SerialID = (SELECT SerialID FROM bill WHERE BillingID = ?)", (billing_id,))
            consumer_row = cursor.fetchone()
            if consumer_row:
                consumer_data["Name"] = f"{consumer_row[0]} {consumer_row[1]}"
                consumer_data["Address"] = consumer_row[2]
                consumer_data["Email"] = consumer_row[3]

            # Fetch Billing Information using BillingID
            cursor.execute("SELECT BillingID, BillingAmount, DueDate FROM bill WHERE BillingID = ?", (billing_id,))
            billing_row = cursor.fetchone()
            if billing_row:
                billing_data["Billing ID"] = str(billing_row[0])
                billing_data["Amount"] = str(billing_row[1])
                billing_data["Due Date"] = billing_row[2]

            # Fetch Payment Information using SerialID from the bill table
            cursor.execute("SELECT AmountPaid, PaymentDate FROM ledger WHERE SerialID = (SELECT SerialID FROM bill WHERE BillingID = ?)", (billing_id,))
            payment_rows = cursor.fetchall()
            for row in payment_rows:
                payment_data["Amount Paid"] = str(row[0])
                payment_data["Payment Date"] = row[1]

            # Fetch Meter Information using the MeterID from the bill's related SerialID
            cursor.execute("SELECT PresentReading, PreviousReading FROM watermeter WHERE MeterID = (SELECT MeterID FROM consumerinfo WHERE SerialID = (SELECT SerialID FROM bill WHERE BillingID = ?))", (billing_id,))
            meter_row = cursor.fetchone()
            if meter_row:
                meter_data["Previous Reading"] = str(meter_row[1])
                meter_data["Present Reading"] = str(meter_row[0])

            # Fetch Concessionaire Information
            cursor.execute("SELECT ConcessionaireName, PricePerCubicMeter FROM concessionaire WHERE ConcessionaireID = (SELECT ConcessionaireID FROM watermeter WHERE MeterID = (SELECT MeterID FROM consumerinfo WHERE SerialID = (SELECT SerialID FROM bill WHERE BillingID = ?)))", (billing_id,))
            concessionaire_row = cursor.fetchone()
            if concessionaire_row:
                concessionaire_data["Concessionaire"] = concessionaire_row[0]
                concessionaire_data["Price per Cubic Meter"] = str(concessionaire_row[1])

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred while fetching data: {e}")
        finally:
            con.close()

        self.show_dynamic_invoice_popup(consumer_data, billing_data, payment_data, meter_data, concessionaire_data)

    def show_dynamic_invoice_popup(self, consumer_data, billing_data, payment_data, meter_data, concessionaire_data):
        main_frame = tk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        title_label = tk.Label(main_frame, text="Invoice Details", font=("Segoe UI", 20, "bold"), fg="#2196F3")
        title_label.pack(pady=10, anchor="center")

        consumer_info_panel = self.create_info_panel(main_frame, "Consumer Information", consumer_data)
        billing_info_panel = self.create_info_panel(main_frame, "Billing Information", billing_data)
        payment_info_panel = self.create_info_panel(main_frame, "Payment Information", payment_data)
        meter_info_panel = self.create_info_panel(main_frame, "Meter Information", meter_data)
        concessionaire_info_panel = self.create_info_panel(main_frame, "Concessionaire Information", concessionaire_data)

        total_amount = Decimal(billing_data.get("Amount", 0))
        total_paid = Decimal(payment_data.get("Amount Paid", 0))
        balance_due = total_amount - total_paid

        total_label = tk.Label(main_frame, text=f"Total Amount: ${self.format_amount(total_amount)}", font=("Segoe UI", 16, "bold"), anchor="e")
        paid_label = tk.Label(main_frame, text=f"Amount Paid: ${self.format_amount(total_paid)}", font=("Segoe UI", 16, "bold"), anchor="e")
        balance_label = tk.Label(main_frame, text=f"Balance Due: ${self.format_amount(balance_due)}", font=("Segoe UI", 16, "bold"), anchor="e", fg="red" if balance_due > 0 else "green")

        total_label.pack(fill=tk.X, pady=5)
        paid_label.pack(fill=tk.X, pady=5)
        balance_label.pack(fill=tk.X, pady=5)

        # Add a scrollbar
        canvas = tk.Canvas(main_frame)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollable_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        scrollable_frame.pack(fill=tk.BOTH, expand=True)

        # Add the panels to the scrollable frame
        consumer_info_panel.pack(fill=tk.X, pady=5)
        billing_info_panel.pack(fill=tk.X, pady=5)
        payment_info_panel.pack(fill=tk.X, pady=5)
        meter_info_panel.pack(fill=tk.X, pady=5)
        concessionaire_info_panel.pack(fill=tk.X, pady=5)

        scrollable_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def create_info_panel(self, parent, title, data):
        panel = tk.Frame(parent)
        panel.pack(fill=tk.X, pady=5)

        title_label = tk.Label(panel, text=title, font=("Segoe UI", 14, "bold"))
        title_label.pack(fill=tk.X)

        for key, value in data.items():
            label = tk.Label(panel, text=f"{key}: {value}", font=("Segoe UI", 12))
            label.pack(fill=tk.X, padx=5, pady=2)

        return panel

    def format_amount(self, amount):
        return "{:,.2f}".format(amount)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    sample_billing_id = 1
    InvoicePopup(root, sample_billing_id)
    root.mainloop()
