import customtkinter as ctk
from tkinter import ttk, Toplevel
from tkinter import messagebox


# Dialog for Charges
class ChargesDialog(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Charges")
        self.geometry("470x230")

        # Create widgets for Charges Dialog
        self.charges_title = ctk.CTkLabel(self, text="Charges", font=("Segoe UI Emoji", 18, "italic"))
        self.charges_title.pack(pady=10)

        self.charges_serial_id_label = ctk.CTkLabel(self, text="Serial ID:", font=("Segoe UI Emoji", 14, "bold"))
        self.charges_serial_id_label.pack(anchor="w", padx=20, pady=5)
        self.charges_serial_id_field = ctk.CTkEntry(self, font=("Segoe UI", 14, "bold"))
        self.charges_serial_id_field.pack(padx=20, pady=5, fill="x")

        self.charges_amount_label = ctk.CTkLabel(self, text="Amount:", font=("Segoe UI Emoji", 14, "bold"))
        self.charges_amount_label.pack(anchor="w", padx=20, pady=5)
        self.charges_amount_field = ctk.CTkEntry(self, font=("Segoe UI", 14, "bold"))
        self.charges_amount_field.pack(padx=20, pady=5, fill="x")

        self.charges_description_label = ctk.CTkLabel(self, text="Charges Description:", font=("Segoe UI Emoji", 14, "bold"))
        self.charges_description_label.pack(anchor="w", padx=20, pady=5)
        self.charges_description_field = ctk.CTkEntry(self, font=("Segoe UI", 14, "bold"))
        self.charges_description_field.pack(padx=20, pady=5, fill="x")

        self.charges_submit_button = ctk.CTkButton(self, text="SUBMIT", font=("Segoe UI Symbol", 14, "bold"), command=self.submit_charges)
        self.charges_submit_button.pack(pady=20)

    def submit_charges(self):
        serial_id = self.charges_serial_id_field.get()
        amount = self.charges_amount_field.get()
        description = self.charges_description_field.get()

        # Validation check before submission
        if not serial_id or not amount or not description:
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            messagebox.showinfo("Charges", f"Charges of {amount} for Serial ID {serial_id} with description '{description}' submitted successfully!")


# Dialog for Payment
class PaymentDialog(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Payment")
        self.geometry("400x250")

        # Create widgets for Payment Dialog
        self.payment_title = ctk.CTkLabel(self, text="Payment Method", font=("Segoe UI", 18, "italic"))
        self.payment_title.pack(pady=10)

        self.payment_serial_id_label = ctk.CTkLabel(self, text="Serial ID:", font=("Segoe UI Emoji", 14, "bold"))
        self.payment_serial_id_label.pack(anchor="w", padx=20, pady=5)
        self.payment_serial_id_field = ctk.CTkEntry(self, font=("Segoe UI", 14, "bold"))
        self.payment_serial_id_field.pack(padx=20, pady=5, fill="x")

        self.payment_amount_label = ctk.CTkLabel(self, text="Amount:", font=("Segoe UI Emoji", 14, "bold"))
        self.payment_amount_label.pack(anchor="w", padx=20, pady=5)
        self.payment_amount_field = ctk.CTkEntry(self, font=("Segoe UI", 14, "bold"))
        self.payment_amount_field.pack(padx=20, pady=5, fill="x")

        self.payment_account_label = ctk.CTkLabel(self, text="Account:", font=("Segoe UI Emoji", 14, "bold"))
        self.payment_account_label.pack(anchor="w", padx=20, pady=5)
        self.payment_account_field = ctk.CTkEntry(self, font=("Segoe UI", 14, "bold"))
        self.payment_account_field.pack(padx=20, pady=5, fill="x")

        self.mop_combo_box = ctk.CTkComboBox(self, values=["Gcash", "Maya", "Visa/Bancnet"], font=("Segoe UI", 12))
        self.mop_combo_box.pack(padx=20, pady=10, fill="x")

        self.payment_submit_button = ctk.CTkButton(self, text="Pay", font=("Segoe UI Symbol", 14, "bold"), command=self.submit_payment)
        self.payment_submit_button.pack(pady=20)

    def submit_payment(self):
        serial_id = self.payment_serial_id_field.get()
        amount = self.payment_amount_field.get()
        account = self.payment_account_field.get()
        mop = self.mop_combo_box.get()

        # Validation check before submission
        if not serial_id or not amount or not account or not mop:
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            messagebox.showinfo("Payment", f"Payment of {amount} for Serial ID {serial_id} from account {account} via {mop} processed successfully!")


#Dialog for New User
class NewUserDialog(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add New Consumer")
        self.geometry("900x600")
        self.resizable(False, False)

        # Define widgets using customtkinter
        self.fname_label = ctk.CTkLabel(self, text="First Name:", font=("Segoe UI", 14, "bold"))
        self.lname_label = ctk.CTkLabel(self, text="Last Name:", font=("Segoe UI", 14, "bold"))
        self.email_label = ctk.CTkLabel(self, text="Email:", font=("Segoe UI", 14, "bold"))
        self.contact_num_label = ctk.CTkLabel(self, text="Contact Number:", font=("Segoe UI", 14, "bold"))
        self.address_label = ctk.CTkLabel(self, text="Address:", font=("Segoe UI", 14, "bold"))
        self.concessionaire_label = ctk.CTkLabel(self, text="Concessionaire:", font=("Segoe UI", 14, "bold"))
        self.serial_id_label = ctk.CTkLabel(self, text="Serial ID:", font=("Segoe UI", 14, "bold"))
        self.meter_id_label = ctk.CTkLabel(self, text="Meter ID:", font=("Segoe UI", 14, "bold"))
        self.pass_label = ctk.CTkLabel(self, text="Password:", font=("Segoe UI", 14, "bold"))

        self.fname_field = ctk.CTkEntry(self, font=("Segoe UI", 14))
        self.lname_field = ctk.CTkEntry(self, font=("Segoe UI", 14))
        self.email_field = ctk.CTkEntry(self, font=("Segoe UI", 14))
        self.contact_num_field = ctk.CTkEntry(self, font=("Segoe UI", 14))
        self.address_field = ctk.CTkEntry(self, font=("Segoe UI", 14))
        self.pass_field = ctk.CTkEntry(self, font=("Segoe UI", 14), show="*")
        self.serial_id_field = ctk.CTkEntry(self, font=("Segoe UI", 14), state="readonly")
        self.meter_id_field = ctk.CTkEntry(self, font=("Segoe UI", 14), state="readonly")

        self.concessionaire_combo_box = ctk.CTkComboBox(self, values=["NasugbuWaters", "BalayanWaterSystem",
                                                                      "LemeryWaterDistrict", "CalataganWaterElement"],
                                                         font=("Segoe UI", 14))
        self.newuser_submit_button = ctk.CTkButton(
            self,
            text="SUBMIT",
            font=("Segoe UI Symbol", 14, "bold"),
            command=self.on_submit
        )

        # Layout the widgets
        self.fname_label.grid(row=1, column=0, pady=5, sticky="w")
        self.fname_field.grid(row=1, column=1, pady=5)

        self.lname_label.grid(row=1, column=2, pady=5, sticky="w")
        self.lname_field.grid(row=1, column=3, pady=5)

        self.email_label.grid(row=2, column=0, pady=5, sticky="w")
        self.email_field.grid(row=2, column=1, pady=5)

        self.contact_num_label.grid(row=3, column=0, pady=5, sticky="w")
        self.contact_num_field.grid(row=3, column=1, pady=5)

        self.address_label.grid(row=4, column=0, pady=5, sticky="w")
        self.address_field.grid(row=4, column=1, pady=5)

        self.pass_label.grid(row=5, column=0, pady=5, sticky="w")
        self.pass_field.grid(row=5, column=1, pady=5)

        self.serial_id_label.grid(row=6, column=0, pady=5, sticky="w")
        self.serial_id_field.grid(row=6, column=1, pady=5)

        self.meter_id_label.grid(row=6, column=2, pady=5, sticky="w")
        self.meter_id_field.grid(row=6, column=3, pady=5)

        self.concessionaire_label.grid(row=7, column=0, pady=5, sticky="w")
        self.concessionaire_combo_box.grid(row=7, column=1, pady=5)

        self.newuser_submit_button.grid(row=8, column=1, columnspan=2, pady=20)

        # Title label
        self.txt = ctk.CTkLabel(self, text="WATER BILLING SYSTEM", font=("Rockwell Extra Bold", 24), text_color="black")
        self.txt.grid(row=0, column=0, columnspan=4, pady=20)

        # Generate Serial ID and Meter ID
        self.generate_ids()

    def generate_ids(self):
        # Automatically generate Serial ID and Meter ID
        self.serial_id_field.configure(state="normal")  # Enable to modify
        self.meter_id_field.configure(state="normal")  # Enable to modify

        serial_id = "S" + str(1001)  # Example serial ID, generate dynamically
        meter_id = "M" + str(5001)  # Example meter ID, generate dynamically

        self.serial_id_field.delete(0, ctk.END)
        self.serial_id_field.insert(0, serial_id)

        self.meter_id_field.delete(0, ctk.END)
        self.meter_id_field.insert(0, meter_id)

        self.serial_id_field.configure(state="readonly")  # Disable after setting value
        self.meter_id_field.configure(state="readonly")  # Disable after setting value

    def on_submit(self):
        # This function will handle the submit button click
        fname = self.fname_field.get()
        lname = self.lname_field.get()
        email = self.email_field.get()
        contact = self.contact_num_field.get()
        address = self.address_field.get()
        password = self.pass_field.get()
        concessionaire = self.concessionaire_combo_box.get()
        serial_id = self.serial_id_field.get()
        meter_id = self.meter_id_field.get()

        # Validation
        if not fname or not lname or not email or not contact or not address or not password or not concessionaire:
            messagebox.showerror("Error", "All fields must be filled in!")
        else:
            # If everything is valid, process the data
            # For now, we just show a success message
            messagebox.showinfo("Success", "New user successfully added!")

            # Optionally, clear the fields after submission
            self.clear_fields()

    def clear_fields(self):
        # Clear the fields after successful submission
        self.fname_field.delete(0, ctk.END)
        self.lname_field.delete(0, ctk.END)
        self.email_field.delete(0, ctk.END)
        self.contact_num_field.delete(0, ctk.END)
        self.address_field.delete(0, ctk.END)
        self.pass_field.delete(0, ctk.END)
        self.concessionaire_combo_box.set('')
        self.generate_ids()  # Regenerate IDs



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
        consumer_tab = self.tab_control.add("Consumers")
        consumer_frame = ctk.CTkFrame(consumer_tab)
        consumer_frame.pack(expand=1, fill="both", padx=10, pady=10)
        consumer_table = ttk.Treeview(consumer_frame, columns=("ID", "Name", "Address", "Phone"), show="headings")
        consumer_table.pack(expand=1, fill="both")
        for col in consumer_table["columns"]:
            consumer_table.heading(col, text=col)

    def create_concessionaire_tab(self):
        concessionaire_tab = self.tab_control.add("Concessionaire")
        concessionaire_frame = ctk.CTkFrame(concessionaire_tab)
        concessionaire_frame.pack(expand=1, fill="both", padx=10, pady=10)
        concessionaire_table = ttk.Treeview(concessionaire_frame, columns=("ID", "Name", "Details"), show="headings")
        concessionaire_table.pack(expand=1, fill="both")
        for col in concessionaire_table["columns"]:
            concessionaire_table.heading(col, text=col)

    def create_arrears_tab(self):
        arrears_tab = self.tab_control.add("Arrears")
        arrears_frame = ctk.CTkFrame(arrears_tab)
        arrears_frame.pack(expand=1, fill="both", padx=10, pady=10)
        arrears_table = ttk.Treeview(arrears_frame, columns=("ID", "Name", "Amount Due", "Due Date"), show="headings")
        arrears_table.pack(expand=1, fill="both")
        for col in arrears_table["columns"]:
            arrears_table.heading(col, text=col)

    def create_charges_tab(self):
        charges_tab = self.tab_control.add("Charges")
        charges_frame = ctk.CTkFrame(charges_tab)
        charges_frame.pack(expand=1, fill="both", padx=10, pady=10)
        charges_table = ttk.Treeview(charges_frame, columns=("ID", "Description", "Amount"), show="headings")
        charges_table.pack(expand=1, fill="both")
        for col in charges_table["columns"]:
            charges_table.heading(col, text=col)

    def create_disconnection_tab(self):
        disconnection_tab = self.tab_control.add("For Disconnection")
        disconnection_frame = ctk.CTkFrame(disconnection_tab)
        disconnection_frame.pack(expand=1, fill="both", padx=10, pady=10)
        disconnection_table = ttk.Treeview(disconnection_frame, columns=("ID", "Name", "Reason"), show="headings")
        disconnection_table.pack(expand=1, fill="both")
        for col in disconnection_table["columns"]:
            disconnection_table.heading(col, text=col)

        disconnect_button = ctk.CTkButton(disconnection_frame, text="Disconnect Consumer", command=self.disconnect_consumer)
        disconnect_button.pack(pady=10)

    def create_disconnected_tab(self):
        disconnected_tab = self.tab_control.add("Disconnected Consumers")
        disconnected_frame = ctk.CTkFrame(disconnected_tab)
        disconnected_frame.pack(expand=1, fill="both", padx=10, pady=10)
        disconnected_table = ttk.Treeview(disconnected_frame, columns=("ID", "Name", "Disconnection Date"), show="headings")
        disconnected_table.pack(expand=1, fill="both")
        for col in disconnected_table["columns"]:
            disconnected_table.heading(col, text=col)

        reconnect_button = ctk.CTkButton(disconnected_frame, text="Reconnect Consumer", command=self.reconnect_consumer)
        reconnect_button.pack(pady=10)

    def create_bills_ledger_tab(self):
        bills_ledger_tab = self.tab_control.add("Bills and Ledger")
        ledger_frame = ctk.CTkFrame(bills_ledger_tab)
        ledger_frame.pack(expand=1, fill="both", padx=10, pady=5)
        ledger_table = ttk.Treeview(ledger_frame, columns=("ID", "Transaction", "Amount", "Date"), show="headings")
        ledger_table.pack(expand=1, fill="both")
        for col in ledger_table["columns"]:
            ledger_table.heading(col, text=col)

        bills_frame = ctk.CTkFrame(bills_ledger_tab)
        bills_frame.pack(expand=1, fill="both", padx=10, pady=5)
        bills_table = ttk.Treeview(bills_frame, columns=("Bill ID", "Name", "Total", "Due Date"), show="headings")
        bills_table.pack(expand=1, fill="both")
        for col in bills_table["columns"]:
            bills_table.heading(col, text=col)

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

