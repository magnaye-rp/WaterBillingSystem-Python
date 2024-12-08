from tkinter import Toplevel
import customtkinter as ctk
from tkinter import messagebox
from aux_method import *

# Dialog for Charges
class ChargesDialog(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Charges")
        self.geometry("470x370")

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
        self.geometry("400x400")

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
        self.geometry("500x420")
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

        self.generate_ids()

    def generate_ids(self):
        # Automatically generate Serial ID and Meter ID
        self.serial_id_field.configure(state="normal")  # Enable to modify
        self.meter_id_field.configure(state="normal")  # Enable to modify

        serial_id = generate_serial_id()  # Example serial ID, generate dynamically
        meter_id = generate_meter_id()  # Example meter ID, generate dynamically

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


class MeterReadingDialog(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Meter Reading")
        self.geometry("420x230")

        # Create widgets
        self.reading_meter_id_label = ctk.CTkLabel(self, text="Meter ID:", font=("Segoe UI", 14, "bold"))
        self.reading_meter_id_label.place(x=110, y=50)

        self.reading_meter_id_field = ctk.CTkEntry(self, font=("Segoe UI", 14), width=110)
        self.reading_meter_id_field.place(x=200, y=50)

        self.prev_reading_label = ctk.CTkLabel(self, text="Previous Reading:", font=("Segoe UI", 14, "bold"))
        self.prev_reading_label.place(x=60, y=90)

        self.prev_reading_field = ctk.CTkEntry(self, font=("Segoe UI", 14), width=110)
        self.prev_reading_field.place(x=200, y=90)

        self.current_reading_label = ctk.CTkLabel(self, text="Current Reading:", font=("Segoe UI", 14, "bold"))
        self.current_reading_label.place(x=60, y=130)

        self.current_reading_field = ctk.CTkEntry(self, font=("Segoe UI", 14), width=110)
        self.current_reading_field.place(x=200, y=130)

        self.reading_submit_button = ctk.CTkButton(self, text="Submit", font=("Segoe UI", 14, "bold"),
                                                   command=self.submit_reading, width=97)
        self.reading_submit_button.place(x=260, y=190)

    def submit_reading(self):
        meter_id = self.reading_meter_id_field.get()
        prev_reading = self.prev_reading_field.get()
        current_reading = self.current_reading_field.get()

        # Add logic to handle the submitted readings (e.g., saving data to a database)

        ctk.CTkMessagebox(title="Submission", message="Meter reading submitted successfully!")

