import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
from decimal import Decimal

class InvoicePopup(tk.Toplevel):
    def __init__(self, parent, billing_id):
        super().__init__(parent)
        self.title("Invoice Details")
        self.geometry("500x700")
        self.resizable(False, False)
        self.fetch_and_display_invoice(billing_id)

    def fetch_and_display_invoice(self, billing_id):
        consumer_data = {}
        billing_data = {}
        meter_data = {}
        concessionaire_data = {}

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="WBSAdmin",
                password="WBS_@dmn.root",
                database="wbs"
            )
            cursor = conn.cursor()

            consumer_query = """
                SELECT FirstName, LastName, Address, Email
                FROM consumerinfo 
                WHERE SerialID = (SELECT SerialID FROM bill WHERE BillingID = %s)
            """
            cursor.execute(consumer_query, (billing_id,))
            consumer = cursor.fetchone()
            if consumer:
                consumer_data["Name"] = f"{consumer[0]} {consumer[1]}"
                consumer_data["Address"] = consumer[2]
                consumer_data["Email"] = consumer[3]

            billing_query = """
                SELECT BillingID, BaseAmount, DueDate 
                FROM bill WHERE BillingID = %s
            """
            cursor.execute(billing_query, (billing_id,))
            billing = cursor.fetchone()
            if billing:
                billing_data["Billing ID"] = str(billing[0])
                billing_data["Amount"] = f"${billing[1]:,.2f}"
                billing_data["Due Date"] = str(billing[2])


            meter_query = """
                SELECT PresentReading, PreviousReading
                FROM watermeter 
                WHERE MeterID = (SELECT MeterID FROM consumerinfo 
                                 WHERE SerialID = (SELECT SerialID FROM bill WHERE BillingID = %s))
            """
            cursor.execute(meter_query, (billing_id,))
            meter = cursor.fetchone()
            if meter:
                meter_data["Previous Reading"] = f"{meter[1]:,.2f}"
                meter_data["Present Reading"] = f"{meter[0]:,.2f}"

            concessionaire_query = """
                SELECT ConcessionaireName, PricePerCubicMeter 
                FROM concessionaire 
                WHERE ConcessionaireID = (SELECT ConcessionaireID FROM watermeter 
                                          WHERE MeterID = (SELECT MeterID FROM consumerinfo 
                                                           WHERE SerialID = (SELECT SerialID FROM bill WHERE BillingID = %s)))
            """
            cursor.execute(concessionaire_query, (billing_id,))
            concessionaire = cursor.fetchone()
            if concessionaire:
                concessionaire_data["Concessionaire"] = concessionaire[0]
                concessionaire_data["Price per Cubic Meter"] = f"${concessionaire[1]:,.2f}"

            late_fee_query = "SELECT LateFeeMultiplier, BaseAmount FROM bill WHERE BillingID = %s"
            cursor.execute(late_fee_query, (billing_id,))
            late_fee = cursor.fetchone()
            late_fee_multiplier = late_fee[0] if late_fee else 1
            base_amount = late_fee[1] if late_fee else 0

            conn.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
            return

        late_fee_multiplier = Decimal(1.20) ** late_fee_multiplier
        late_fee_amount = (Decimal(base_amount) * late_fee_multiplier) - Decimal(base_amount)
        total_amount = Decimal(billing_data.get("Amount", "0").replace('$', '').replace(',', ''))

        billing_data["Late Fee"] = f"${late_fee_amount:,.2f}"
        billing_data["Total Amount with Late Fee"] = f"${total_amount + late_fee_amount:,.2f}"

        self.show_dynamic_invoice_popup(consumer_data, billing_data, meter_data, concessionaire_data, billing_data["Total Amount with Late Fee"])

    def show_dynamic_invoice_popup(self, consumer_data, billing_data, meter_data, concessionaire_data, total_amount):
        main_frame = tk.Frame(self)
        main_frame.pack(pady=10)

        title_label = tk.Label(main_frame, text="Invoice Details", font=("Segoe UI", 20, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.create_info_panel(main_frame, "Consumer Information", consumer_data, 1)
        self.create_info_panel(main_frame, "Billing Information", billing_data, 2)
        self.create_info_panel(main_frame, "Meter Information", meter_data, 3)
        self.create_info_panel(main_frame, "Concessionaire Information", concessionaire_data, 4)

        balance_label = tk.Label(main_frame, text=f"Balance Due: {total_amount}", fg="red", font=("Segoe UI", 14, "bold"))
        balance_label.grid(row=6, column=0, columnspan=2, pady=10)

        self.grab_set()
        self.wait_window()

    def create_info_panel(self, parent, title, data, row):
        panel_frame = tk.Frame(parent)
        panel_frame.grid(row=row, column=0, padx=10, pady=5, sticky="w")

        title_label = tk.Label(panel_frame, text=title, font=("Segoe UI", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=5)

        for idx, (key, value) in enumerate(data.items(), 1):
            label = tk.Label(panel_frame, text=f"{key}: {value}", font=("Segoe UI", 12))
            label.grid(row=idx, column=0, sticky="w")

    def format_amount(self, amount):
        return f"${amount:,.2f}"
