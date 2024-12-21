import mysql.connector
from dialogs import *
from Userui import *

def fetch_and_display_data(table, query):
    connection = mysql.connector.connect(
        host="localhost",
        user="WBSAdmin",
        password="WBS_@dmn.root",
        database="wbs"
    )
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        for item in table.get_children():
            table.delete(item)

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

        self.create_bottom_buttons()

    def create_consumer_tab(self):
        consumer_tab = self.tab_control.add("Consumers")
        consumer_frame = ctk.CTkFrame(consumer_tab)
        consumer_frame.pack(expand=1, fill="both", padx=10, pady=10)

        search_frame = ctk.CTkFrame(consumer_frame)
        search_frame.pack(fill="x", padx=10, pady=5)

        search_label = ctk.CTkLabel(search_frame, text="Search:")
        search_label.pack(side="left", padx=5)

        self.consumer_search_entry = ctk.CTkEntry(search_frame, placeholder_text="Enter name or ID...")
        self.consumer_search_entry.pack(side="left", fill="x", expand=True, padx=5)

        search_button = ctk.CTkButton(search_frame, text="Search", command=self.search_consumers)
        search_button.pack(side="left", padx=5)

        reset_button = ctk.CTkButton(search_frame, text="Reset", command=self.reset_consumer_search)
        reset_button.pack(side="left", padx=5)

        self.consumer_table = ttk.Treeview(
            consumer_frame,
            columns=("MeterID", "First Name", "Last Name", "Address", "Contact Number", "Email", "Inspector",
                     "Inspector Contact"),
            show="headings"
        )
        self.consumer_table.pack(expand=1, fill="both")

        # Configure Table Columns
        for col in self.consumer_table["columns"]:
            self.consumer_table.heading(col, text=col)
            self.consumer_table.column(col, width=150, anchor="center")

        openbutton = ctk.CTkButton(consumer_frame, text="Open User", command=self.new_user)
        openbutton.pack(side="right",pady=3, padx=5)
        newbutton = ctk.CTkButton(consumer_frame, text="New User", command=self.open_user)
        newbutton.pack(side="right",pady=3, padx=5)
        query = """
                SELECT ci.MeterID, ci.FirstName, ci.LastName, ci.Address, ci.ContactNumber, ci.Email, 
                mi.Name AS InspectorName, mi.ContactNumber AS InspectorContactNumber 
                FROM consumerinfo ci 
                JOIN meterinspector mi ON mi.InspectorID = ci.InspectorID 
                WHERE ci.isConnected = 'active'
                """
        fetch_and_display_data(self.consumer_table, query)

    def search_consumers(self):
        search_term = self.consumer_search_entry.get().strip()
        query = f"""
                SELECT ci.MeterID, ci.FirstName, ci.LastName, ci.Address, ci.ContactNumber, ci.Email, 
                mi.Name AS InspectorName, mi.ContactNumber AS InspectorContactNumber 
                FROM consumerinfo ci 
                JOIN meterinspector mi ON mi.InspectorID = ci.InspectorID 
                WHERE ci.isConnected = 1 AND 
                (ci.FirstName LIKE '%{search_term}%' OR ci.LastName LIKE '%{search_term}%')
                """
        fetch_and_display_data(self.consumer_table, query)

    def reset_consumer_search(self):
        self.consumer_search_entry.delete(0, "end")

        query = """
                SELECT ci.MeterID, ci.FirstName, ci.LastName, ci.Address, ci.ContactNumber, ci.Email, 
                mi.Name AS InspectorName, mi.ContactNumber AS InspectorContactNumber 
                FROM consumerinfo ci 
                JOIN meterinspector mi ON mi.InspectorID = ci.InspectorID 
                WHERE ci.isConnected = 1
                """
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

        search_frame = ctk.CTkFrame(arrears_frame)
        search_frame.pack(fill="x", padx=10, pady=5)

        search_label = ctk.CTkLabel(search_frame, text="Search:")
        search_label.pack(side="left", padx=5)

        self.consumer_arrear_entry = ctk.CTkEntry(search_frame, placeholder_text="Enter name or ID...")
        self.consumer_arrear_entry.pack(side="left", fill="x", expand=True, padx=5)

        search_button = ctk.CTkButton(search_frame, text="Search", command=self.search_arrears)
        search_button.pack(side="left", padx=5)

        reset_button = ctk.CTkButton(search_frame, text="Reset", command=self.reset_arrears_search)
        reset_button.pack(side="left", padx=5)

        self.arrears_table = ttk.Treeview(
            arrears_frame,
            columns=("FirstName", "LastName", "Address", "BillingID", "BillingAmount", "DueDate", "Status"),
            show="headings"
        )
        for col in self.arrears_table["columns"]:
            self.arrears_table.heading(col, text=col)
            self.arrears_table.column(col, width=150, anchor="center")
        self.arrears_table.pack(expand=1, fill="both")
        button = ctk.CTkButton(arrears_frame, text="Make Payment", command=self.payment)
        button.pack(side="right",pady=3, padx=10)
        latebutton = ctk.CTkButton(arrears_frame, text="Add Late Fees", command=self.add_late_fees)
        latebutton.pack(side="right", pady=3)
        # initialize query
        query = """
                SELECT ci.FirstName, ci.LastName,ci.Address, b.BillingID, b.BillingAmount, b.DueDate, 
                ci.isConnected FROM bill b JOIN consumerinfo ci ON b.SerialID = ci.SerialID WHERE b.isPaid = 0 
                AND b.DueDate < CURDATE()
                """
        # Fetch and display data
        fetch_and_display_data(self.arrears_table, query)

    def search_arrears(self):
        search_term = self.consumer_arrear_entry.get().strip()

        query = f"""
                SELECT ci.FirstName, ci.LastName,ci.Address, b.BillingID, b.BillingAmount, b.DueDate, 
                ci.isConnected FROM bill b JOIN consumerinfo ci ON b.SerialID = ci.SerialID WHERE b.isPaid = 0 
                AND b.DueDate < CURDATE() AND 
                (ci.FirstName LIKE '%{search_term}%' OR ci.LastName LIKE '%{search_term}%')
                """
        fetch_and_display_data(self.arrears_table, query)

    def reset_arrears_search(self):
        self.consumer_arrear_entry.delete(0, "end")

        query = """
                SELECT ci.FirstName, ci.LastName,ci.Address, b.BillingID, b.BillingAmount, b.DueDate, 
                ci.isConnected FROM bill b JOIN consumerinfo ci ON b.SerialID = ci.SerialID WHERE b.isPaid = 0 
                AND b.DueDate < CURDATE()
                """
        fetch_and_display_data(self.arrears_table, query)

    def create_charges_tab(self):
        charges_tab = self.tab_control.add("Charges")
        charges_frame = ctk.CTkFrame(charges_tab)
        charges_frame.pack(expand=1, fill="both", padx=10, pady=10)

        self.charges_table = ttk.Treeview(
            charges_frame,
            columns=("First Name", "Last Name", "Charge Amount", "Date Incurred", "Type"),
            show="headings"
        )
        for col in self.charges_table["columns"]:
            self.charges_table.heading(col, text=col)
            self.charges_table.column(col, width=150, anchor="center")

        self.charges_table.pack(expand=1, fill="both")
        button = ctk.CTkButton(charges_frame, text="Add Charges", command=self.add_charges)
        button.pack( pady=3)
        # initialize query
        query = """
                SELECT ci.FirstName, ci.LastName, c.ChargeAmount, c.DateIncurred, c.Type FROM charge c Join consumerinfo ci on ci.SerialID = c.SerialID
                """
        # Fetch and display data
        fetch_and_display_data(self.charges_table, query)


    def create_disconnection_tab(self):
        disconnection_tab = self.tab_control.add("For Disconnection")
        disconnection_frame = ctk.CTkFrame(disconnection_tab)
        disconnection_frame.pack(expand=1, fill="both", padx=10, pady=10)

        self.disconnection_table = ttk.Treeview(
            disconnection_frame,
            columns=("FirstName", "LastName", "MeterID"),
            show="headings"
        )
        for col in self.disconnection_table["columns"]:
            self.disconnection_table.heading(col, text=col)
            self.disconnection_table.column(col, width=150, anchor="center")

        self.disconnection_table.pack(expand=1, fill="both")
        # initialize query
        query = """SELECT DISTINCT ci.FirstName, ci.LastName, ci.MeterID FROM bill b JOIN consumerinfo ci 
        ON b.SerialID = ci.SerialID WHERE b.DueDate < CURDATE() AND b.isPaid = 0 AND ci.isConnected = 'active' AND b.SerialID 
        IN ( SELECT SerialID FROM bill WHERE DueDate < CURDATE() AND isPaid = 0 GROUP BY SerialID HAVING 
        COUNT(SerialID) >= 3 ) ORDER BY ci.SerialID"""

        # Fetch and display data
        fetch_and_display_data(self.disconnection_table, query)

        disconnect_button = ctk.CTkButton(disconnection_frame, text="Disconnect Consumer", command=self.disconnect_consumer)
        disconnect_button.pack(pady=3)

    def create_disconnected_tab(self):
        disconnected_tab = self.tab_control.add("Disconnected Consumers")
        disconnected_frame = ctk.CTkFrame(disconnected_tab)
        disconnected_frame.pack(expand=1, fill="both", padx=10, pady=10)

        self.disconnected_table = ttk.Treeview(
            disconnected_frame,
            columns=("MeterID", "FirstName", "LastName", "Address", "ContactNumber", "Email"),
            show="headings"
        )
        for col in self.disconnected_table["columns"]:
            self.disconnected_table.heading(col, text=col)
            self.disconnected_table.column(col, width=150, anchor="center")

        self.disconnected_table.pack(expand=1, fill="both")
        # initialize query
        query = """SELECT MeterID, FirstName, LastName, Address, ContactNumber, Email FROM 
        `consumerinfo` WHERE isConnected = 'inactive'"""

        # Fetch and display data
        fetch_and_display_data(self.disconnected_table, query)

        reconnect_button = ctk.CTkButton(disconnected_frame, text="Reconnect Consumer", command=self.reconnect_consumer)
        reconnect_button.pack(pady=3)

    def create_bills_ledger_tab(self):
        bills_ledger_tab = self.tab_control.add("Ledger and Bills")
        ledger_frame = ctk.CTkFrame(bills_ledger_tab)
        ledger_frame.pack(expand=1, fill="both", padx=10, pady=5)

        self.ledger_table = ttk.Treeview(
            ledger_frame,
            columns=("BillingID", "FirstName", "LastName", "AmountPaid", "PaymentDate"),
            show="headings"
        )
        for col in self.ledger_table["columns"]:
            self.ledger_table.heading(col, text=col)
            self.ledger_table.column(col, width=150, anchor="center")

        self.ledger_table.pack(expand=1, fill="both")
        # initialize query
        lquery = """SELECT l.BillingID, ci.FirstName, ci.LastName, l.AmountPaid, 
        l.PaymentDate FROM ledger l JOIN bill b ON l.BillingID = b.BillingID JOIN consumerinfo ci ON b.SerialID = ci.SerialID; """

        # Fetch and display data
        fetch_and_display_data(self.ledger_table, lquery)

        bills_frame = ctk.CTkFrame(bills_ledger_tab)
        bills_frame.pack(expand=1, fill="both", padx=10, pady=5)

        self.bills_table = ttk.Treeview(
            bills_frame,
            columns=("First Name", "Last Name", "Billing Amount", "Due Date"),
            show="headings"
        )
        for col in self.bills_table["columns"]:
            self.bills_table.heading(col, text=col)
            self.bills_table.column(col, width=150, anchor="center")

        self.bills_table.pack(expand=1, fill="both")
        # initialize query
        bquery = """SELECT ci.FirstName, ci.LastName, b.BillingAmount, DueDate from bill b join consumerinfo ci on ci.SerialID = b.SerialID where isPaid = 0"""

        # Fetch and display data
        fetch_and_display_data(self.bills_table, bquery)

    def create_bottom_buttons(self):
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10, fill="x")

        buttons = [
            ("New Reading", self.new_reading),
            ("Generate Bills", self.generate_bills),
            ("Refresh", self.refresh),
        ]
        for text, command in buttons:
            ctk.CTkButton(button_frame, text=text, command=command).pack(side="left", padx=10)

    def open_user(self):
        selected_item = self.consumer_table.focus()
        item_values = self.consumer_table.item(selected_item, "values")
        #(0, pangalan, adrress....)
        serial_id = item_values[0]
        UserUI(serial_id)
        print("Open User clicked")

    def disconnect_consumer(self):
        selected_item = self.disconnection_table.focus()
        if not selected_item:
            messagebox.showerror("Error", "No consumer selected.")
            return
        item_values = self.disconnection_table.item(selected_item, "values")
        id = item_values[2]
        name = item_values[0]
        serial_id = get_serial_name(id, name)
        disconnect(serial_id)
        try:
            query = """
                    SELECT ci.MeterID, ci.FirstName, ci.LastName, ci.Address, ci.ContactNumber, ci.Email, 
                    mi.Name AS InspectorName, mi.ContactNumber AS InspectorContactNumber FROM consumerinfo ci 
                    JOIN meterinspector mi ON mi.InspectorID = ci.InspectorID WHERE ci.isConnected = 'active'
                    """
            fetch_and_display_data(self.consumer_table, query)
        except Exception as e:
            print(f"Error refreshing consumer data: {e}")
        try:
            query = """SELECT DISTINCT ci.FirstName, ci.LastName, ci.MeterID FROM bill b JOIN consumerinfo ci 
                    ON b.SerialID = ci.SerialID WHERE b.DueDate < CURDATE() AND b.isPaid = 0 AND ci.isConnected = 'active' AND b.SerialID 
                    IN ( SELECT SerialID FROM bill WHERE DueDate < CURDATE() AND isPaid = 0 GROUP BY SerialID HAVING 
                    COUNT(SerialID) >= 3 ) ORDER BY ci.SerialID"""
            fetch_and_display_data(self.disconnection_table, query)
        except Exception as e:
            print(f"Error refreshing disconnection data: {e}")

        try:
            query = """SELECT MeterID, FirstName, LastName, Address, ContactNumber, Email FROM 
                    `consumerinfo` WHERE isConnected = 'inactive'"""
            fetch_and_display_data(self.disconnected_table, query)
        except Exception as e:
            print(f"Error refreshing disconnected data: {e}")

    def reconnect_consumer(self):
        selected_item = self.disconnected_table.focus()
        item_values = self.disconnected_table.item(selected_item, "values")
        id = item_values[0]
        name = item_values[1]
        serial_id = get_serial_name(id, name)
        if existing_arrears(serial_id):
            messagebox.showerror("Error", "Please Settle arrears first!!")
        else:
            reconnect(serial_id)
        try:
            query = """
                    SELECT ci.MeterID, ci.FirstName, ci.LastName, ci.Address, ci.ContactNumber, ci.Email, 
                    mi.Name AS InspectorName, mi.ContactNumber AS InspectorContactNumber FROM consumerinfo ci 
                    JOIN meterinspector mi ON mi.InspectorID = ci.InspectorID WHERE ci.isConnected = 'active'
                    """
            fetch_and_display_data(self.consumer_table, query)
        except Exception as e:
            print(f"Error refreshing consumer data: {e}")
        try:
            query = """SELECT DISTINCT ci.FirstName, ci.LastName, ci.MeterID FROM bill b JOIN consumerinfo ci 
                    ON b.SerialID = ci.SerialID WHERE b.DueDate < CURDATE() AND b.isPaid = 0 AND ci.isConnected = 'active' AND b.SerialID 
                    IN ( SELECT SerialID FROM bill WHERE DueDate < CURDATE() AND isPaid = 0 GROUP BY SerialID HAVING 
                    COUNT(SerialID) >= 3 ) ORDER BY ci.SerialID"""
            fetch_and_display_data(self.disconnection_table, query)
        except Exception as e:
            print(f"Error refreshing disconnection data: {e}")

        try:
            query = """SELECT MeterID, FirstName, LastName, Address, ContactNumber, Email FROM 
                    `consumerinfo` WHERE isConnected = 'inactive'"""
            fetch_and_display_data(self.disconnected_table, query)
        except Exception as e:
            print(f"Error refreshing disconnected data: {e}")

    def payment(self):
        PaymentDialog(self)
        try:
            query = """
                    SELECT ci.FirstName, ci.LastName,ci.Address, b.BillingID, b.BillingAmount, b.DueDate, 
                    ci.isConnected FROM bill b JOIN consumerinfo ci ON b.SerialID = ci.SerialID WHERE b.isPaid = 0 
                    AND b.DueDate < CURDATE()
                    """
            fetch_and_display_data(self.arrears_table, query)
        except Exception as e:
            print(f"Error refreshing arrears data: {e}")

    def new_reading(self):
        MeterReadingDialog(self)

    def add_charges(self):
        ChargesDialog(self)

    def new_user(self):
        NewUserDialog(self)

    def generate_bills(self):
        generate_bills()
        print("Generate Bills clicked")

    def add_late_fees(self):
        add_late_fees()

    def refresh(self):
        try:
            query = """
                    SELECT ci.MeterID, ci.FirstName, ci.LastName, ci.Address, ci.ContactNumber, ci.Email, 
                    mi.Name AS InspectorName, mi.ContactNumber AS InspectorContactNumber FROM consumerinfo ci 
                    JOIN meterinspector mi ON mi.InspectorID = ci.InspectorID WHERE ci.isConnected = 'active'
                    """
            fetch_and_display_data(self.consumer_table, query)
        except Exception as e:
            print(f"Error refreshing consumer data: {e}")

        try:
            query = """
                    SELECT ci.FirstName, ci.LastName,ci.Address, b.BillingID, b.BillingAmount, b.DueDate, 
                    ci.isConnected FROM bill b JOIN consumerinfo ci ON b.SerialID = ci.SerialID WHERE b.isPaid = 0 
                    AND b.DueDate < CURDATE()
                    """
            fetch_and_display_data(self.arrears_table, query)
        except Exception as e:
            print(f"Error refreshing arrears data: {e}")

        try:
            query = """
                    SELECT ci.FirstName, ci.LastName, c.ChargeAmount, c.DateIncurred, c.Type FROM charge c Join consumerinfo ci on ci.SerialID = c.SerialID
                    """
            fetch_and_display_data(self.charges_table, query)
        except Exception as e:
            print(f"Error refreshing charges data: {e}")

        try:
            query = """SELECT DISTINCT ci.FirstName, ci.LastName, ci.MeterID FROM bill b JOIN consumerinfo ci 
                    ON b.SerialID = ci.SerialID WHERE b.DueDate < CURDATE() AND b.isPaid = 0 AND ci.isConnected = 'active' AND b.SerialID 
                    IN ( SELECT SerialID FROM bill WHERE DueDate < CURDATE() AND isPaid = 0 GROUP BY SerialID HAVING 
                    COUNT(SerialID) >= 3 ) ORDER BY ci.SerialID"""
            fetch_and_display_data(self.disconnection_table, query)
        except Exception as e:
            print(f"Error refreshing disconnection data: {e}")

        try:
            query = """SELECT MeterID, FirstName, LastName, Address, ContactNumber, Email FROM 
                    `consumerinfo` WHERE isConnected = 'inactive'"""
            fetch_and_display_data(self.disconnected_table, query)
        except Exception as e:
            print(f"Error refreshing disconnected data: {e}")

        try:
            bquery = """SELECT ci.FirstName, ci.LastName, b.BillingAmount, DueDate from bill b join consumerinfo ci on ci.SerialID = b.SerialID where isPaid = 0"""
            fetch_and_display_data(self.bills_table, bquery)
        except Exception as e:
            print(f"Error refreshing bills data: {e}")

        try:
            lquery = """SELECT l.BillingID, ci.FirstName, ci.LastName, l.AmountPaid, 
                    l.PaymentDate FROM ledger l JOIN bill b ON l.BillingID = b.BillingID JOIN consumerinfo ci ON b.SerialID = ci.SerialID; """
            fetch_and_display_data(self.ledger_table, lquery)
        except Exception as e:
            print(f"Error refreshing ledger data: {e}")


# Run the application
if __name__ == "__main__":
    app = WaterBillingSystem()
    app.mainloop()

