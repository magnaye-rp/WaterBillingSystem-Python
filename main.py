from tkinter import ttk
import mysql.connector
from dialogs import *

def fetch_and_display_data(table, query):
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host="localhost",
            user="WBSAdmin",
            password="WBS_@dmn.root",
            database="wbs"
        )
        cursor = connection.cursor()
        cursor.execute(query)

        # Fetch all rows
        rows = cursor.fetchall()

        # Insert rows into the table
        for row in rows:
            table.insert("", "end", values=row)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            connection.close()


# Main WaterBillingSystem
class WaterBillingSystem(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.title("Water Billing System")
        self.geometry("1200x700")

        # Title Label
        self.title_label = ctk.CTkLabel(self, text="Water Billing System", font=("Nirmala UI", 36, "bold"))
        self.title_label.pack(pady=10)

        # Tabs
        self.tab_control = ctk.CTkTabview(self)
        self.tab_control.pack(expand=1, fill="both", padx=10, pady=10)

        # Create Tabs
        self.create_consumer_tab()
        self.create_concessionaire_tab()
        self.create_arrears_tab()
        self.create_charges_tab()
        self.create_disconnection_tab()
        self.create_disconnected_tab()
        self.create_bills_ledger_tab()

        # Bottom Buttons
        self.create_bottom_buttons()

    def create_consumer_tab(self):
        # Create Consumer Tab
        consumer_tab = self.tab_control.add("Consumers")
        consumer_frame = ctk.CTkFrame(consumer_tab)
        consumer_frame.pack(expand=1, fill="both", padx=10, pady=10)

        # Create Consumer Table
        self.consumer_table = ttk.Treeview(
            consumer_frame,
            columns=("SerialID", "MeterID", "FirstName", "LastName", "Address", "ContactNumber", "Email", "Inspector", "Contact"),
            show="headings"
        )
        self.consumer_table.pack(expand=1, fill="both")

        # Configure Table Columns
        for col in self.consumer_table["columns"]:
            self.consumer_table.heading(col, text=col)
            self.consumer_table.column(col, width=150, anchor="center")
        #initialize query
        query = """
                SELECT ci.SerialID, ci.MeterID, ci.FirstName, ci.LastName, ci.Address, ci.ContactNumber, ci.Email, 
                mi.Name AS InspectorName, mi.ContactNumber AS InspectorContactNumber FROM consumerinfo ci 
                JOIN meterinspector mi ON mi.InspectorID = ci.InspectorID WHERE ci.isConnected = 1
                """
        # Fetch and display data
        fetch_and_display_data(self.consumer_table, query)

    def create_concessionaire_tab(self):
        concessionaire_tab = self.tab_control.add("Concessionaire")
        concessionaire_frame = ctk.CTkFrame(concessionaire_tab)
        concessionaire_frame.pack(expand=1, fill="both", padx=10, pady=10)

        self.concessionaire_table = ttk.Treeview(
            concessionaire_frame,
            columns=("concessionaireID", "concessionaireName", "PricePerCubicMeter"),
            show="headings"
        )
        for col in self.concessionaire_table["columns"]:
            self.concessionaire_table.heading(col, text=col)
            self.concessionaire_table.column(col, width=150, anchor="center")

        self.concessionaire_table.pack(expand=1, fill="both")
        # initialize query
        query = """
                SELECT * FROM concessionaire
                """
        # Fetch and display data
        fetch_and_display_data(self.concessionaire_table, query)


    def create_arrears_tab(self):
        arrears_tab = self.tab_control.add("Arrears")
        arrears_frame = ctk.CTkFrame(arrears_tab)
        arrears_frame.pack(expand=1, fill="both", padx=10, pady=10)

        self.arrears_table = ttk.Treeview(
            arrears_frame,
            columns=("SerialID", "FirstName", "LastName", "Address", "BillingID", "BillingAmount", "DueDate", "isConnected"),
            show="headings"
        )
        for col in self.arrears_table["columns"]:
            self.arrears_table.heading(col, text=col)
            self.arrears_table.column(col, width=150, anchor="center")

        self.arrears_table.pack(expand=1, fill="both")
        # initialize query
        query = """
                SELECT b.SerialID, ci.FirstName, ci.LastName,ci.Address, b.BillingID, b.BillingAmount, b.DueDate, 
                ci.isConnected FROM bill b JOIN consumerinfo ci ON b.SerialID = ci.SerialID WHERE b.isPaid = 0 
                AND b.DueDate < CURDATE()
                """
        # Fetch and display data
        fetch_and_display_data(self.arrears_table, query)

    def create_charges_tab(self):
        charges_tab = self.tab_control.add("Charges")
        charges_frame = ctk.CTkFrame(charges_tab)
        charges_frame.pack(expand=1, fill="both", padx=10, pady=10)

        self.charges_table = ttk.Treeview(
            charges_frame,
            columns=("ChargeID", "SerialID", "ChargeAmount", "DateIncurred", "Type"),
            show="headings"
        )
        for col in self.charges_table["columns"]:
            self.charges_table.heading(col, text=col)
            self.charges_table.column(col, width=150, anchor="center")

        self.charges_table.pack(expand=1, fill="both")
        # initialize query
        query = """
                SELECT ChargeID, SerialID, ChargeAmount, DateIncurred, Type FROM charge WHERE isDebt = 0
                """
        # Fetch and display data
        fetch_and_display_data(self.charges_table, query)

    def create_disconnection_tab(self):
        disconnection_tab = self.tab_control.add("For Disconnection")
        disconnection_frame = ctk.CTkFrame(disconnection_tab)
        disconnection_frame.pack(expand=1, fill="both", padx=10, pady=10)

        self.disconnection_table = ttk.Treeview(
            disconnection_frame,
            columns=("SerialID", "FirstName", "LastName", "MeterID"),
            show="headings"
        )
        for col in self.disconnection_table["columns"]:
            self.disconnection_table.heading(col, text=col)
            self.disconnection_table.column(col, width=150, anchor="center")

        self.disconnection_table.pack(expand=1, fill="both")
        # initialize query
        query = """SELECT DISTINCT ci.SerialID, ci.FirstName, ci.LastName, ci.MeterID FROM bill b JOIN consumerinfo ci 
        ON b.SerialID = ci.SerialID WHERE b.DueDate < CURDATE() AND b.isPaid = 0 AND ci.isConnected = 1 AND b.SerialID 
        IN ( SELECT SerialID FROM bill WHERE DueDate < CURDATE() AND isPaid = 0 GROUP BY SerialID HAVING 
        COUNT(SerialID) >= 3 ) ORDER BY ci.SerialID"""

        # Fetch and display data
        fetch_and_display_data(self.disconnection_table, query)

    def create_disconnected_tab(self):
        disconnected_tab = self.tab_control.add("Disconnected Consumers")
        disconnected_frame = ctk.CTkFrame(disconnected_tab)
        disconnected_frame.pack(expand=1, fill="both", padx=10, pady=10)

        self.disconnected_table = ttk.Treeview(
            disconnected_frame,
            columns=("SerialID", "MeterID", "FirstName", "LastName", "Address", "ContactNumber", "Email"),
            show="headings"
        )
        for col in self.disconnected_table["columns"]:
            self.disconnected_table.heading(col, text=col)
            self.disconnected_table.column(col, width=150, anchor="center")

        self.disconnected_table.pack(expand=1, fill="both")
        # initialize query
        query = """SELECT SerialID, MeterID, FirstName, LastName, Address, ContactNumber, Email FROM 
        `consumerinfo` WHERE isConnected = 0"""

        # Fetch and display data
        fetch_and_display_data(self.disconnected_table, query)

        reconnect_button = ctk.CTkButton(disconnected_frame, text="Reconnect Consumer", command=self.reconnect_consumer)
        reconnect_button.pack(pady=10)

    def create_bills_ledger_tab(self):
        bills_ledger_tab = self.tab_control.add("Bills and Ledger")
        ledger_frame = ctk.CTkFrame(bills_ledger_tab)
        ledger_frame.pack(expand=1, fill="both", padx=10, pady=5)

        self.ledger_table = ttk.Treeview(
            ledger_frame,
            columns=("LedgerID", "BillingID", "FirstName", "LastName", "AmountPaid", "PaymentDate"),
            show="headings"
        )
        for col in self.ledger_table["columns"]:
            self.ledger_table.heading(col, text=col)
            self.ledger_table.column(col, width=150, anchor="center")

        self.ledger_table.pack(expand=1, fill="both")
        # initialize query
        query = """SELECT l.LedgerID, l.BillingID, ci.FirstName, ci.LastName, l.AmountPaid, 
        l.PaymentDate FROM ledger l JOIN bill b ON l.BillingID = b.BillingID JOIN consumerinfo ci ON b.SerialID = ci.SerialID; """

        # Fetch and display data
        fetch_and_display_data(self.ledger_table, query)

        bills_frame = ctk.CTkFrame(bills_ledger_tab)
        bills_frame.pack(expand=1, fill="both", padx=10, pady=5)

        self.bills_table = ttk.Treeview(
            bills_frame,
            columns=("BillingID", "SerialID", "DebtID", "ChargeID", "BillingAmount", "DueDate"),
            show="headings"
        )
        for col in self.bills_table["columns"]:
            self.bills_table.heading(col, text=col)
            self.bills_table.column(col, width=150, anchor="center")

        self.bills_table.pack(expand=1, fill="both")
        # initialize query
        query = """SELECT BillingID, SerialID, DebtID, ChargeID, BillingAmount, DueDate from bill"""

        # Fetch and display data
        fetch_and_display_data(self.bills_table, query)

    def create_bottom_buttons(self):
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10, fill="x")

        buttons = [
            ("Open User", self.open_user),
            ("Payment", self.payment),
            ("New Reading", self.new_reading),
            ("Add Charges", self.add_charges),
            ("Generate Bills", self.generate_bills),
            ("New User", self.new_user),
        ]
        for text, command in buttons:
            ctk.CTkButton(button_frame, text=text, command=command).pack(side="left", padx=10)

    def open_user(self):
        print("Open User clicked")
        # Implement functionality to open an existing user, maybe a dialog

    def disconnect_consumer(self):
        print("Disconnect Consumer clicked")  # Placeholder for actual implementation

    def reconnect_consumer(self):
        print("Reconnect Consumer clicked")

    def payment(self):
        PaymentDialog(self)

    def new_reading(self):
        print("New Reading clicked")
        # Implement functionality to enter a new reading, similar to other dialogs

    def add_charges(self):
        ChargesDialog(self)

    def generate_bills(self):
        print("Generate Bills clicked")
        # Implement functionality to generate bills, perhaps another dialog or process

    def new_user(self):
        NewUserDialog(self)  # Opens the New User dialog


# Run the application
if __name__ == "__main__":
    app = WaterBillingSystem()  # Instantiate the main app
    app.mainloop()  # Start the Tkinter event loop

