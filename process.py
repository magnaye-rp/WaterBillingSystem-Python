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

