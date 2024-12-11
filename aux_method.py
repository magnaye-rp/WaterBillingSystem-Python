from decimal import Decimal

import mysql.connector
from datetime import datetime, timedelta, date
from tkinter import messagebox


def get_serial_id(billing_id):
    serial_id = -1

    try:
        con = mysql.connector.connect(
            host="localhost",
            user="WBSAdmin",
            password="WBS_@dmn.root",
            database="wbs"
        )
        query = "SELECT SerialID FROM bill WHERE BillingID = %s"
        cur = con.cursor()
        cur.execute(query, (billing_id,))
        row = cur.fetchone()

        if row:
            serial_id = row[0]
        else:
            print(f"No matching record found for BillingID: {billing_id}")

    except mysql.connector.Error as e:
        print(f"Database error: {e}")

    return serial_id

#GET BILL AMOUNT
def get_bill_amount(billing_id):
    bill_amount = 0

    try:
        con = mysql.connector.connect(
            host="localhost",
            user="WBSAdmin",
            password="WBS_@dmn.root",
            database="wbs"
        )
        query = "SELECT BillingAmount FROM bill WHERE BillingID = %s"
        cur = con.cursor()
        cur.execute(query, (billing_id,))
        row = cur.fetchone()

        if row:
            bill_amount = row[0]
        else:
            print(f"No matching record found for BillingID: {billing_id}")

    except mysql.connector.Error as e:
        print(f"Database error: {e}")

    return bill_amount


def generate_serial_id():
    serial_id = 0

    try:
        con = mysql.connector.connect(
            host="localhost",
            user="WBSAdmin",
            password="WBS_@dmn.root",
            database="wbs"
        )
        max_serial_id_query = "SELECT MAX(SerialID) AS maxSerialID FROM consumerinfo"
        cur = con.cursor()
        cur.execute(max_serial_id_query)
        row = cur.fetchone()

        if row and row[0] is not None:
            serial_id = row[0] + 1
        else:
            serial_id = 1  # If the table is empty, start with SerialID = 1

    except mysql.connector.Error as e:
        print(f"Database error: {e}")

    return serial_id


def generate_meter_id():
    meter_id = 0

    try:
        con = mysql.connector.connect(
            host="localhost",
            user="WBSAdmin",
            password="WBS_@dmn.root",
            database="wbs"
        )
        max_meter_id_query = "SELECT MAX(MeterID) AS maxMeterID FROM watermeter"
        cur = con.cursor()
        cur.execute(max_meter_id_query)
        row = cur.fetchone()

        if row and row[0] is not None:
            meter_id = row[0] + 1  # Predict next MeterID
        else:
            meter_id = 1  # If the table is empty, start with MeterID = 1

    except mysql.connector.Error as e:
        print(f"Database error: {e}")

    return meter_id


def previous_reading(meter_id):
    reading = 0

    try:
        con = mysql.connector.connect(
            host="localhost",
            user="WBSAdmin",
            password="WBS_@dmn.root",
            database="wbs"
        )
        query = "SELECT PresentReading FROM watermeter WHERE MeterID = %s"
        cur = con.cursor()
        cur.execute(query, (meter_id,))
        row = cur.fetchone()

        if row:
            reading = row[0]

    except mysql.connector.Error as e:
        print(f"Database error: {e}")

    return reading

def process_payment(billing_id):
        try:
            con = mysql.connector.connect(
            host="localhost",
            user="WBSAdmin",
            password="WBS_@dmn.root",
            database="wbs"
            )
            con.isolation_level = None  # Disable autocommit

            check_query = "SELECT isPaid FROM bill WHERE BillingID = %s"
            cur = con.cursor()
            cur.execute(check_query, (billing_id,))
            row = cur.fetchone()

            if row is None:
                print("Bill Does Not Exist")
                raise Exception(f"Invalid BillingID: {billing_id}")

            if row[0] == 1:  # If isPaid is True (1)
                messagebox.showinfo("Notice",f"Bill with BillingID {billing_id} is already paid.")
                raise Exception(f"Bill with BillingID {billing_id} is already paid.")


            # Insert into ledger
            insert_ledger_query = """
                INSERT INTO ledger (BillingID, SerialID, AmountPaid, PaymentDate)
                SELECT BillingID, SerialID, BillingAmount, CURRENT_DATE
                FROM bill WHERE BillingID = %s
            """
            cur.execute(insert_ledger_query, (billing_id,))

            # Update isPaid in bill
            update_bill_query = "UPDATE bill SET isPaid = 1 WHERE BillingID = %s"
            cur.execute(update_bill_query, (billing_id,))

            # Update charge isDebt status
            update_charge_query = """
                UPDATE charge SET isDebt = 1 WHERE ChargeID = (SELECT ChargeID FROM bill WHERE BillingID = %s)
            """
            cur.execute(update_charge_query, (billing_id,))

            con.commit()
            messagebox.showinfo("Success", f"Payment processed successfully for BillingID: {billing_id}")
            print(f"Payment processed successfully for BillingID: {billing_id}")

        except mysql.connector.Error as e:
            if con:
                con.rollback()
            print(f"Database error: {e}")

        except Exception as ex:
            if con:
                con.rollback()
            print(f"Error: {ex}")

        finally:
            if con:
                con.isolation_level = ''  # Re-enable autocommit
                con.close()


def concessionaire(name):
    if name == "NasugbuWaters":
        return 1
    elif name == "BalayanWaterSystem":
        return 2
    elif name == "LemeryWaterDistrict":
        return 3
    elif name == "CalataganWaterElement":
        return 4
    return 0

def generate_bills():
    try:
        # Establish the database connection
        con = mysql.connector.connect(
            host="localhost",
            user="WBSAdmin",
            password="WBS_@dmn.root",
            database="wbs"
        )
        current_date = datetime.now().date()

        # Check the last generation date
        check_generation_query = "SELECT generation_date FROM bill_generation_log ORDER BY generation_date DESC LIMIT 1"
        cursor = con.cursor()  # Standard cursor
        cursor.execute(check_generation_query)
        row = cursor.fetchone()

        if row:
            last_generation_date = row[0]  # Access using index
            next_generation_date = last_generation_date + timedelta(days=30)
            if next_generation_date <= current_date:
                generate_bills_logic(con)  # Generate bills
                log_generation_date(con)  # Log the new generation
            else:
                messagebox.showinfo("Info", "Bills have already been generated for this period.")
        else:
            # No previous record exists, generate bills
            generate_bills_logic(con)
            log_generation_date(con)

        cursor.close()
        con.close()

    except mysql.connector.Error as e:
        print("generate_bills Database Error:", e)
    except Exception as ex:
        print("generate_bills Exception Error:", ex)


def generate_bills_logic(con):
    try:
        query = """
        SELECT ci.SerialID, d.DebtID, c.ChargeID, 
               AmountDue AS TotalAmount, 
               CURRENT_DATE + INTERVAL 30 DAY AS DueDate 
        FROM consumerinfo ci 
        LEFT JOIN debt d ON ci.SerialID = d.MeterID 
        LEFT JOIN charge c ON ci.SerialID = c.SerialID
        """
        cursor = con.cursor()  # Standard cursor
        cursor.execute(query)
        rows = cursor.fetchall()

        insert_query = """
        INSERT INTO bill (SerialID, DebtID, ChargeID, BaseAmount, BillingAmount, DueDate, lateFeeMultiplier, isPaid) 
        VALUES (%s, %s, 0, %s, %s, %s, 0, 0)
        """
        insert_cursor = con.cursor()
        for row in rows:
            SerialID = row[0]
            DebtID = row[1]
            BaseAmount = row[3]
            BillingAmount = BaseAmount
            DueDate = row[4]

            insert_cursor.execute(insert_query, (SerialID, DebtID, BaseAmount, BillingAmount, DueDate))

        con.commit()
        insert_cursor.close()
        cursor.close()

        messagebox.showinfo("Success", "Billing data successfully inserted")
        print("Billing data successfully inserted.")
    except mysql.connector.Error as e:
        print("generate_bills_logic Database Error:", e)
    except Exception as ex:
        print("generate_bills_logic Exception Error:", ex)


def log_generation_date(con):
    try:
        log_generation_query = "INSERT INTO bill_generation_log (generation_date) VALUES (CURRENT_DATE)"
        cursor = con.cursor()
        cursor.execute(log_generation_query)
        con.commit()
        cursor.close()
    except mysql.connector.Error as e:
        print("log_generation_date Database Error:", e)
    except Exception as ex:
        print("log_generation_date Exception Error:", ex)

# Function to disconnect
def disconnect(serialID):
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="WBSAdmin",
            password="WBS_@dmn.root",
            database="wbs"
        )

        # SQL query to disconnect user
        disconnect_query = "UPDATE consumerinfo SET isConnected = 0 WHERE SerialID = %s"
        cursor = con.cursor()
        cursor.execute(disconnect_query, (serialID,))
        con.commit()

        print(f"Disconnect successful for SerialID: {serialID}")
        messagebox.showinfo("Success",f"Disconnect successful for SerialID: {serialID}")
    except mysql.connector.Error as e:
        if con:
            con.rollback()
        print(f"Error: {e}")
    finally:
        if con:
            con.close()

# Function to reconnect
def reconnect(serialID):
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="WBSAdmin",
            password="WBS_@dmn.root",
            database="wbs"
        )
        reconnect_query = "UPDATE consumerinfo SET isConnected = 1 WHERE SerialID = %s"
        cursor = con.cursor()
        cursor.execute(reconnect_query, (serialID,))
        con.commit()

        print(f"Reconnect successful for SerialID: {serialID}")
        messagebox.showinfo("Success", f"Reconnect successful for SerialID: {serialID}")
    except mysql.connector.Error as e:
        if con:
            con.rollback()
        print(f"Error: {e}")
    finally:
        if con:
            con.close()


def setup_row_sorter(jtable1, jtable5):
    sorter = jtable1.get_table_row_sorter()
    jtable1.set_row_sorter(sorter)

    sorted_table = jtable5.get_table_row_sorter()
    jtable5.set_row_sorter(sorted_table)


def existing_arrears(serialID):
    exists = False

    try:
        con = mysql.connector.connect(
            host="localhost",
            user="WBSAdmin",
            password="WBS_@dmn.root",
            database="wbs"
        )
        query = """
            SELECT COUNT(*) 
            FROM bill b 
            JOIN consumerinfo ci ON b.SerialID = ci.SerialID 
            WHERE b.isPaid = 0 AND b.DueDate < CURRENT_DATE AND b.SerialID = %s
        """
        cursor = con.cursor()
        cursor.execute(query, (serialID,))
        rs = cursor.fetchone()

        if rs:
            exists = rs[0] > 0

    except mysql.connector.Error as e:
        print(f"Error checking existing arrears: {e}")
    finally:
        if con:
            con.close()

    return exists


def add_late_fees():
    con = None
    cursor = None
    rs = None

    today = date.today()
    day_of_month = today.day
    if day_of_month != 11:
        print("Late fees can only be added on the 27th of the month.")
        return

    try:
        con = mysql.connector.connect(
            host="localhost",
            user="WBSAdmin",
            password="WBS_@dmn.root",
            database="wbs"
        )

        cursor = con.cursor(dictionary=True)

        # Select overdue bills
        select_query = """
            SELECT b.BillingID, b.SerialID, b.BillingAmount, c.ChargeID, c.ChargeAmount 
            FROM bill b 
            LEFT JOIN charge c ON b.ChargeID = c.ChargeID 
            WHERE b.isPaid = 0 AND b.DueDate < CURRENT_DATE;
        """
        cursor.execute(select_query)
        rs = cursor.fetchall()

        # Prepare statement for updating bill
        update_bill_query = """
            UPDATE bill 
            SET BillingAmount = BillingAmount + %s, LateFeeMultiplier = LateFeeMultiplier + 1 
            WHERE BillingID = %s
        """

        # Process each overdue bill
        for row in rs:
            billingID = row['BillingID']
            chargeID = row['ChargeID']
            billingAmount = row['BillingAmount']

            if chargeID is None:
                # No charge, apply a late fee of 50 directly to the billing amount
                cursor.execute(update_bill_query, (Decimal(50), billingID))
            else:
                # Existing charge, increase the billing amount by 20%
                cursor.execute(update_bill_query, (Decimal(billingAmount) * Decimal(0.2), billingID))

        con.commit()  # Commit the transaction
        print("Late fees successfully added to overdue bills.")
    except mysql.connector.Error as e:
        if con:
            con.rollback()  # Rollback in case of error
        print(f"Error adding late fees: {e}")
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()