import random
from tkinter import Toplevel
import customtkinter as ctk
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

        self.charges_name_label = ctk.CTkLabel(self, text="Name:", font=("Segoe UI Emoji", 14, "bold"))
        self.charges_name_label.pack(anchor="w", padx=20, pady=5)
        self.charges_name_field = ctk.CTkEntry(self, font=("Segoe UI", 14, "bold"))
        self.charges_name_field.pack(padx=20, pady=5, fill="x")

        self.charges_amount_label = ctk.CTkLabel(self, text="Amount: Peso", font=("Segoe UI Emoji", 14, "bold"))
        self.charges_amount_label.pack(anchor="w", padx=20, pady=5)
        self.charges_amount_combo_box = ctk.CTkComboBox(self, values=["20", "30",
                                                                      "40", "50", "100"],
                                                        font=("Segoe UI", 14))
        self.charges_amount_combo_box.pack(anchor="w", padx=20, pady=5)

        self.charges_description_label = ctk.CTkLabel(self, text="Charges Description:", font=("Segoe UI Emoji", 14, "bold"))
        self.charges_description_label.pack(anchor="w", padx=20, pady=5)
        self.charges_description_combo_box = ctk.CTkComboBox(self, values=["Adjustment", "Repairs",
                                                                      "Damages", "Penalty"],
                                                        font=("Segoe UI", 14))
        self.charges_description_combo_box.pack(anchor="w", padx=20, pady=5)

        self.charges_submit_button = ctk.CTkButton(self, text="SUBMIT", font=("Segoe UI Symbol", 14, "bold"), command=self.submit_charges)
        self.charges_submit_button.pack(pady=20)
        self.charges_serial_id_field.bind("<KeyRelease>", self.on_serial_id_change)

    def submit_charges(self):
        serial_id = self.charges_serial_id_field.get()
        amount = self.charges_amount_combo_box.get()
        description = self.charges_description_combo_box.get()

        # Validation check before submission
        if not serial_id or not amount or not description:
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            self.add_charge_and_bill()

    def add_charge_and_bill(self):
        try:
            # Connect to the database
            con = mysql.connector.connect(
                host="localhost",
                user="WBSAdmin",
                password="WBS_@dmn.root",
                database="wbs"
            )
            cursor = con.cursor()

            # Retrieving input values
            serial_id = self.charges_serial_id_field.get()
            amount = self.charges_amount_combo_box.get()
            desc = self.charges_description_combo_box.get()
            billing_amount = float(amount)
            due_date = date.today()

            insert_charge_query = (
                """
                INSERT INTO charge (SerialID, ChargeAmount, DateIncurred, Type)
                VALUES (%s, %s, CURDATE() + INTERVAL 30 DAY, %s);
                """
            )

            cursor.execute(insert_charge_query, (serial_id, amount, desc))
            con.commit()

            charge_id = cursor.lastrowid

            insert_bill_query = (
                """
                INSERT INTO bill (SerialID, DebtID, ChargeID, BaseAmount, BillingAmount, DueDate, isPaid, LateFeeMultiplier)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                """
            )

            cursor.execute(insert_bill_query, (serial_id, 0, charge_id, billing_amount, billing_amount, due_date, 0, 0))
            con.commit()

            self.charges_serial_id_field.delete(0, 'end')
            self.charges_amount_combo_box.set("")
            self.charges_description_combo_box.set("")
            ChargesDialog.destroy(self)
            messagebox.showinfo("Success", "Charge and Bill successfully added!")


        except mysql.connector.Error as e:
            con.rollback()
            messagebox.showerror("Error", f"An error occurred: {e}")

        finally:
            if cursor:
                cursor.close()
            if con:
                con.close()

    def on_serial_id_change(self, event):
        serial = self.charges_serial_id_field.get()
        try:
            name = get_name_charge(serial)
            self.charges_name_field.delete(0, ctk.END)
            self.charges_name_field.insert(0, str(name))
        except mysql.connector.Error as e:
            print(f"Error retrieving bill amount: {e}")


class PaymentDialog(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Payment")
        self.geometry("400x450")

        # Create widgets for Payment Dialog
        self.payment_title = ctk.CTkLabel(self, text="Payment Method", font=("Segoe UI", 18, "italic"))
        self.payment_title.pack(pady=10)

        self.payment_bill_id_label = ctk.CTkLabel(self, text="Bill ID:", font=("Segoe UI Emoji", 14, "bold"))
        self.payment_bill_id_label.pack(anchor="w", padx=20, pady=5)
        self.payment_bill_id_field = ctk.CTkEntry(self, font=("Segoe UI", 14, "bold"))
        self.payment_bill_id_field.pack(padx=20, pady=5, fill="x")

        self.payment_account_label = ctk.CTkLabel(self, text="Name:", font=("Segoe UI Emoji", 14, "bold"))
        self.payment_account_label.pack(anchor="w", padx=20, pady=5)
        self.payment_account_field = ctk.CTkEntry(self, font=("Segoe UI", 14, "bold"))
        self.payment_account_field.pack(padx=20, pady=5, fill="x")

        self.payment_amount_label = ctk.CTkLabel(self, text="Amount:", font=("Segoe UI Emoji", 14, "bold"))
        self.payment_amount_label.pack(anchor="w", padx=20, pady=5)
        self.payment_amount_field = ctk.CTkEntry(self, font=("Segoe UI", 14, "bold"))
        self.payment_amount_field.pack(padx=20, pady=5, fill="x")

        self.mop_label = ctk.CTkLabel(self, text="Mode of Payment:", font=("Segoe UI Emoji", 14, "bold"))
        self.mop_label.pack(anchor="w", padx=20, pady=5)
        self.mop_combo_box = ctk.CTkComboBox(self, values=["Gcash", "Maya", "Visa/Bancnet"], font=("Segoe UI", 12))
        self.mop_combo_box.pack(padx=20, pady=10, fill="x")

        self.payment_submit_button = ctk.CTkButton(self, text="Pay", font=("Segoe UI Symbol", 14, "bold"), command=self.submit_payment)
        self.payment_submit_button.pack(pady=20)
        self.payment_bill_id_field.bind("<KeyRelease>", self.on_bill_id_change)

    def submit_payment(self):
        bill_id = self.payment_bill_id_field.get()
        amount = self.payment_amount_field.get()
        account = self.payment_account_field.get()
        mop = self.mop_combo_box.get()

        # Validation check before submission
        if not bill_id or not amount or not account or not mop:
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            process_payment(bill_id)
            PaymentDialog.destroy(self)



    def on_bill_id_change(self, event):
        bill_id = self.payment_bill_id_field.get()
        try:
            bill = get_bill_amount(bill_id)
            name = get_name(bill_id)
            self.payment_amount_field.delete(0, ctk.END)
            self.payment_amount_field.insert(0, str(bill))
            self.payment_account_field.delete(0, ctk.END)
            self.payment_account_field.insert(0, str(name))
        except mysql.connector.Error as e:
            print(f"Error retrieving bill amount: {e}")



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
        self.serial_id_field.configure(state="normal")
        self.meter_id_field.configure(state="normal")
        serial_id = generate_serial_id()
        meter_id = generate_meter_id()

        self.serial_id_field.delete(0, ctk.END)
        self.serial_id_field.insert(0, serial_id)

        self.meter_id_field.delete(0, ctk.END)
        self.meter_id_field.insert(0, meter_id)

        self.serial_id_field.configure(state="readonly")
        self.meter_id_field.configure(state="readonly")

    def on_submit(self):
        # This function will handle the submit button click
        fname = self.fname_field.get()
        lname = self.lname_field.get()
        email = self.email_field.get()
        contact = self.contact_num_field.get()
        address = self.address_field.get()
        password = self.pass_field.get()
        concessionaire = self.concessionaire_combo_box.get()

        if not fname or not lname or not email or not contact or not address or not password or not concessionaire:
            messagebox.showerror("Error", "All fields must be filled in!")
        else:
            self.submit_action()
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
        self.generate_ids()
        NewUserDialog.destroy(self)

    def submit_action(self):
        fname = self.fname_field.get().strip()
        lname = self.lname_field.get().strip()
        password = self.pass_field.get().strip()
        address = self.address_field.get().strip()
        email = self.email_field.get().strip()
        contact = self.contact_num_field.get().strip()
        name = self.concessionaire_combo_box.get().strip()
        concessionaire_num = concessionaire(name)

        if not all([fname, lname, password, address, email, contact, concessionaire]):
            messagebox.showerror("Validation Error", "All fields are required and cannot be empty.")
            return

        try:
            con = mysql.connector.connect(
                host="localhost",
                user="WBSAdmin",
                password="WBS_@dmn.root",
                database="wbs"
            )

            if con.is_connected():
                cursor = con.cursor()

                meter_id = generate_meter_id()
                inspector_id = random.randint(1, 6)

                insert_consumer_query = (
                    """
                    INSERT INTO consumerinfo 
                    (Password, FirstName, LastName, Address, ContactNumber, Email, MeterID, InspectorID) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                    """
                )
                cursor.execute(insert_consumer_query,
                               (password, fname, lname, address, contact, email, meter_id, inspector_id))

                insert_water_meter_query = (
                    """
                    INSERT INTO watermeter 
                    (PresentReading, PreviousReading, ReadingDate, PreviousReadingDate, ConcessionaireID) 
                    VALUES (0, 0, CURDATE(), CURDATE(), %s)
                    """
                )
                cursor.execute(insert_water_meter_query, (concessionaire_num,))
                con.commit()

                messagebox.showinfo("Success", "Consumer successfully added!")


        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
            if con:
                con.rollback()

        finally:
            if con.is_connected():
                cursor.close()
                con.close()

class MeterReadingDialog(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Meter Reading")
        self.geometry("420x230")

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
        self.reading_meter_id_field.bind("<KeyRelease>", self.on_meter_id_change)

    def submit_reading(self):
        self.update_water_meter_and_insert_debt()

    def previous_reading(self,meter_id):
        con = mysql.connector.connect(
            host="localhost",
            user="WBSAdmin",
            password="WBS_@dmn.root",
            database="wbs"
        )
        try:
            cursor = con.cursor()
            query = "SELECT PresentReading FROM watermeter WHERE MeterID = %s"
            cursor.execute(query, (meter_id,))
            result = cursor.fetchone()
            return result[0] if result else 0
        except mysql.connector.Error as e:
            print(f"Error retrieving previous reading: {e}")
            raise
        finally:
            if con.is_connected():
                cursor.close()
                con.close()

    def update_water_meter_and_insert_debt(self):
        meter_id = self.reading_meter_id_field.get()
        present_reading = self.current_reading_field.get()
        try:
            con = mysql.connector.connect(
                host="localhost",
                user="WBSAdmin",
                password="WBS_@dmn.root",
                database="wbs"
            )
            cursor = con.cursor()

            prev_reading = previous_reading(meter_id)
            current_reading = float(present_reading)

            # Validate the current reading
            if current_reading < prev_reading:
                self.prev_reading_field.delete(0, ctk.END)
                messagebox.showwarning(
                    "Input Error",
                    "Warning: Current reading cannot be less than previous reading."
                )
                return

            update_query = """
                UPDATE watermeter
                SET 
                    PreviousReading = PresentReading,
                    PreviousReadingDate = ReadingDate,
                    PresentReading = %s,
                    ReadingDate = CURDATE()
                WHERE MeterID = %s
            """
            cursor.execute(update_query, (current_reading, meter_id))

            # Insert into debt table
            insert_query = """
                INSERT INTO debt (MeterID, FromDate, PreviousReading, ToDate, LatestReading, AmountDue)
                SELECT 
                    wm.MeterID,
                    wm.PreviousReadingDate AS FromDate,
                    wm.PreviousReading,
                    wm.ReadingDate AS ToDate,
                    wm.PresentReading AS LatestReading,
                    wm.Consumption * c.PricePerCubicMeter AS AmountDue
                FROM 
                    watermeter wm
                JOIN 
                    concessionaire c ON wm.ConcessionaireID = c.ConcessionaireID
                WHERE 
                    wm.MeterID = %s
            """
            cursor.execute(insert_query, (meter_id,))

            con.commit()
            messagebox.showinfo("Success",
                                f"Debt successfully inserted and water meter updated for MeterID: {meter_id}")
            MeterReadingDialog.destroy(self)

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            if con.is_connected():
                con.rollback()
        finally:
            if con.is_connected():
                cursor.close()
                con.close()

    def on_meter_id_change(self, event):

        meter_id = self.reading_meter_id_field.get()
        try:
            prev_reading = self.previous_reading(meter_id)
            self.prev_reading_field.delete(0, ctk.END)
            self.prev_reading_field.insert(0, str(prev_reading))
        except mysql.connector.Error as e:
            print(f"Error retrieving previous reading: {e}")