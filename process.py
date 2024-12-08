import tkinter as tk
from tkinter import messagebox
import logging



# from openuser button
from tkinter import messagebox
def openUser():
    selected_item = table.focus()  # Gets the currently selected item in the table
    if selected_item:  # Check if any row is selected
        try:
            item_values = table.item(selected_item, "values")  # Get values of the selected row
            id_value = item_values[0]  # Assuming the ID is in the first column
            user_ui = UserUI(id_value)  # Initialize UserUI with the ID
            user_ui.mainloop()  # Display the new UserUI window
        except Exception as ex:
            print(f"Error: {ex}")
    else:
        messagebox.showwarning("Warning", "Please select a row.")  # Show a warning if no row is selected


#Payment button
def open_dialog():
    dialog = Toplevel(root)
    dialog.title("Dialog")
    dialog.geometry("200x100")  # Optional: Adjust as needed

root = Tk()
Button(root, text="Open Dialog", command=open_dialog).pack()
root.mainloop()

#new reading button
def show_dialog():
    dialog = Toplevel(root)
    dialog.title("Dialog")
    dialog.geometry("200x100")  # Optional: Adjust size

root = Tk()
Button(root, text="Open Dialog", command=show_dialog).pack()
root.mainloop()

#add charges button
def show_charges():
    charges = Toplevel(root)
    charges.title("Charges")
    charges.geometry("300x200")  # Optional: Adjust size as needed

root = Tk()
Button(root, text="Generate Bills", command=show_charges).pack()
root.mainloop()

#generate bills button
def generatebills_action():
    generatebills()


#log out button
def jbutton3_action():
    root.destroy()  # Close the current window
    login_ui = Tk()  # Create a new window for the login page
    login_ui.title("Login Page")
    login_ui.mainloop()

#refresh button
def jbutton9_action():
    root.destroy()  # Close the current window
    new_admin_ui = Tk()  # Create a new window for the Admin UI
    new_admin_ui.title("Admin UI")
    new_admin_ui.mainloop()

#add new costumer button
def jbutton1_action():
    try:
        serial_id = generate_serial_id()
        serial_id_field.delete(0, END)
        serial_id_field.insert(0, str(serial_id))

        meter_id = generate_meter_id()
        meter_id_field.delete(0, END)
        meter_id_field.insert(0, str(meter_id))

    except Exception as ex:
        print(f"Error: {ex}")

    dialog.pack()
    dialog.deiconify()  # Show the dialog

# You would need to define generate_serial_id, generate_meter_id, and your GUI components like serial_id_field, meter_id_field, and dialog elsewhere in your code.
