import mysql.connector
import sqlite3
from datetime import datetime, timedelta, date
from tkinter import messagebox

connection = mysql.connector.connect(
            host="localhost",
            user="WBSAdmin",
            password="WBS_@dmn.root",
            database="wbs"
        )
def get_serial_id(billing_id):
    serial_id = -1

    try:
        con = connection
        query = "SELECT SerialID FROM bill WHERE BillingID = ?"
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
        con = connection
        query = "SELECT BillingAmount FROM bill WHERE BillingID = ?"
        cur = con.cursor()
        cur.execute(query, (billing_id,))
        row = cur.fetchone()

        if row:
            bill_amount = row[0]
        else:
            print(f"No matching record found for BillingID: {billing_id}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    return bill_amount


def generate_serial_id():
    serial_id = 0

    try:
        con = connection
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
        con = connection
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
        con = connection
        query = "SELECT PresentReading FROM watermeter WHERE MeterID = ?"
        cur = con.cursor()
        cur.execute(query, (meter_id,))
        row = cur.fetchone()

        if row:
            reading = row[0]

    except mysql.connector.Error as e:
        print(f"Database error: {e}")

    return reading


def check_if_paid(meter_id):
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="WBSAdmin",
            password="WBS_@dmn.root",
            database="wbs"
            )
        query = "SELECT isPaid FROM watermeter WHERE MeterID = ?"
        cur = con.cursor()
        cur.execute(query, (meter_id,))
        row = cur.fetchone()

        if row:
            return row[0]
        else:
            return -1
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return -1

def process_payment(billing_id):
        con = None
        try:
            con = mysql.connector.connect(
            host="localhost",
            user="WBSAdmin",
            password="WBS_@dmn.root",
            database="wbs"
            )
            con.isolation_level = None  # Disable autocommit

            # Validate BillingID and check if already paid
            check_query = "SELECT isPaid FROM bill WHERE BillingID = ?"
            cur = con.cursor()
            cur.execute(check_query, (billing_id,))
            row = cur.fetchone()

            if row is None:
                print("Bill Does Not Exist")
                raise Exception(f"Invalid BillingID: {billing_id}")

            if row[0] == 1:  # If isPaid is True (1)
                print("Already Paid")
                raise Exception(f"Bill with BillingID {billing_id} is already paid.")

            # Insert into ledger
            insert_ledger_query = """
                INSERT INTO ledger (BillingID, SerialID, AmountPaid, PaymentDate)
                SELECT BillingID, SerialID, BillingAmount, CURRENT_DATE
                FROM bill WHERE BillingID = ?
            """
            cur.execute(insert_ledger_query, (billing_id,))

            # Update isPaid in bill
            update_bill_query = "UPDATE bill SET isPaid = 1 WHERE BillingID = ?"
            cur.execute(update_bill_query, (billing_id,))

            # Update charge isDebt status
            update_charge_query = """
                UPDATE charge SET isDebt = 1 WHERE ChargeID = (SELECT ChargeID FROM bill WHERE BillingID = ?)
            """
            cur.execute(update_charge_query, (billing_id,))

            con.commit()
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


# Function to generate bills
def generate_bills():
    try:

        con = mysql.connector.connect(
            host="localhost",
            user="WBSAdmin",
            password="WBS_@dmn.root",
            database="wbs"
        )
        check_generation_query = "SELECT generation_date FROM bill_generation_log ORDER BY generation_date DESC LIMIT 1"
        cursor = con.cursor()
        cursor.execute(check_generation_query)

        current_date = datetime.now().date()

        row = cursor.fetchone()

        if row:
            last_generation_date = row[0]

            next_generation_date = last_generation_date + timedelta(days=30)

            if next_generation_date < current_date:
                generate_bills_logic(con)

                log_generation_query = "INSERT INTO bill_generation_log (generation_date) VALUES (CURRENT_DATE)"
                cursor.execute(log_generation_query)
                con.commit()

                messagebox.showinfo("Success", "Billing data successfully inserted")
                print("Billing data successfully inserted.")
            else:
                messagebox.showinfo("Info", "Bills have already been generated for this period.")
        else:
            generate_bills_logic(con)

            log_generation_query = "INSERT INTO bill_generation_log (generation_date) VALUES (CURRENT_DATE)"
            cursor.execute(log_generation_query)
            con.commit()

            messagebox.showinfo("Success", "Billing data successfully inserted")
            print("Billing data successfully inserted.")
    except sqlite3.Error as e:
        print("Error:", e)
    except Exception as ex:
        print("Error:", ex)

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

        cursor = con.cursor()
        cursor.execute(query)

        insert_query = """
        INSERT INTO bill (SerialID, DebtID, ChargeID, BillingAmount, DueDate, isPaid) 
        VALUES (?, ?, ?, ?, ?, 0)
        """
        insert_cursor = con.cursor()

        for row in cursor.fetchall():
            SerialID = row[0]
            DebtID = row[1]
            ChargeID = row[2]

            # Check if either DebtID or ChargeID is 0
            if DebtID == 0 and ChargeID == 0:
                print(f"Skipping bill generation for SerialID: {SerialID} due to DebtID or ChargeID being 0.")
                continue  # Skip this iteration and move to the next row

            Amount = row[3]
            DueDate = row[4]

            # Insert the data into the bill table
            insert_cursor.execute(insert_query, (SerialID, DebtID, ChargeID, Amount, DueDate))

        con.commit()
        messagebox.showinfo("Success", "Billing data successfully inserted")
        print("Billing data successfully inserted.")
    except sqlite3.Error as e:
        print("Error:", e)

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
    except sqlite3.Error as e:
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
        # Use `with` statement to manage the cursor
        with connection.cursor() as cursor:
            query = """
                SELECT COUNT(*) 
                FROM bill b 
                JOIN consumerinfo ci ON b.SerialID = ci.SerialID 
                WHERE b.isPaid = 0 AND b.DueDate < CURRENT_DATE AND b.SerialID = %s
            """
            cursor.execute(query, (serialID,))
            rs = cursor.fetchone()

            if rs:
                exists = rs[0] > 0  # If count > 0, arrears exist

    except sqlite3.Error as e:
        print(f"Error checking existing arrears: {e}")
    finally:
        # Close the connection if this function owns it
        if connection:
            connection.close()

    return exists


def add_late_fees():
    con = None
    select_stmt = None
    insert_charge_stmt = None
    update_charge_stmt = None
    update_bill_stmt = None
    rs = None

    today = date.today()
    day_of_month = today.day
    if day_of_month != 27:
        print("Late fees can only be added on the 27th of the month.")
        return

    try:
        con = connection
        con.begin()

        # Select overdue bills
        select_query = """
            SELECT b.BillingID, b.SerialID, b.BillingAmount, c.ChargeID, c.ChargeAmount 
            FROM bill b 
            LEFT JOIN charge c ON b.ChargeID = c.ChargeID 
            WHERE b.isPaid = 0 AND b.DueDate < CURRENT_DATE;
        """
        select_stmt = con.prepare(select_query)
        rs = select_stmt.execute_query()

        # Prepare statements for charge updates
        insert_charge_query = "INSERT INTO charge (SerialID, ChargeAmount, DateIncurred, Type) VALUES (?, 50, CURRENT_DATE, 'LateFee')"
        insert_charge_stmt = con.prepare(insert_charge_query)

        update_charge_query = "UPDATE charge SET ChargeAmount = ChargeAmount * 1.2 WHERE ChargeID = ?"
        update_charge_stmt = con.prepare(update_charge_query)

        update_bill_query = "UPDATE bill SET ChargeID = ?, BillingAmount = BillingAmount + ? WHERE BillingID = ?"
        update_bill_stmt = con.prepare(update_bill_query)

        # Process each overdue bill
        for row in rs:
            billingID = row[0]
            serialID = row[1]
            chargeID = row[2]
            billingAmount = row[3]

            if chargeID == 0:
                # No existing charge, insert new charge
                insert_charge_stmt.execute_query([serialID])
                chargeID = insert_charge_stmt.lastrowid  # Get the newly inserted chargeID

                # Update bill with new chargeID and amount
                update_bill_stmt.execute_query([chargeID, 50, billingID])
            else:
                # Existing charge, increase by 20%
                update_charge_stmt.execute_query([chargeID])

                # Update bill to reflect the increased charge
                update_bill_stmt.execute_query([chargeID, billingAmount * 0.2, billingID])

        con.commit()  # Commit the transaction
        print("Late fees successfully added to overdue bills.")
    except sqlite3.Error as e:
        if con:
            con.rollback()  # Rollback in case of error
        print(f"Error adding late fees: {e}")
    finally:
        if rs:
            rs.close()
        if select_stmt:
            select_stmt.close()
        if insert_charge_stmt:
            insert_charge_stmt.close()
        if update_charge_stmt:
            update_charge_stmt.close()
        if update_bill_stmt:
            update_bill_stmt.close()
        if con:
            con.close()

