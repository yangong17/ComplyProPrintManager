import tkinter as tk
from tkinter import filedialog
import pygetwindow as gw
import pyautogui
import keyboard
import time
import os

## Function: Stop print
def stop_printing():
    global stop_flag
    stop_flag = True
    log("Stop printing command received.")

def check_esc_key():
    while True:
        if keyboard.is_pressed('Esc'):
            stop_printing()
            break
        time.sleep(0.1)

# Stop print listener thread
import threading
thread = threading.Thread(target=check_esc_key)
thread.daemon = True
thread.start()


## Function: Print label
def print_labels():
    quantity = quantity_entry.get()
    if not quantity.isdigit():
        log("Please enter a valid quantity")
        return
    
    # Check if the ComplyPro window is open
    complypro_window = None
    for window in gw.getAllWindows():
        if "complypro label designer" in window.title.lower():
            complypro_window = window
            break

    if complypro_window is None:
        log("ComplyPro window not found! Please make sure ComplyPro Label Designer is open.")
        return
    else:
        log(f"ComplyPro window found: {complypro_window.title}")

    # Maximize the window, bring into foreground
    complypro_window.maximize()
    complypro_window.activate()
    
    # Initialize ComplyPro: Close all tabs (Max of 11 tabs)
    for i in range(11):
        pyautogui.hotkey('ctrl', 'w')
    
    files_printed = 0  # Counter for the number of files printed

    for file in selected_files:
        if stop_flag:  # Check the stop flag
            log("Printing stopped by user.")
            break

        file_name = os.path.basename(file)  # Extracting file name
        log(f"Printing {file_name} with quantity {quantity}")

        # Open the label file
        os.startfile(file)
        
        # 5 second buffer
        time.sleep(5)
        
        # Make ComplyPro window active
        pyautogui.moveTo(complypro_window.left + complypro_window.width // 2, complypro_window.top + complypro_window.height // 2)
        pyautogui.click()
        
        # Perform key strokes to print label
        pyautogui.hotkey('alt', 'f')
        for i in range(7):
            pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.typewrite(str(quantity))
        pyautogui.press('enter')
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(int(quantity)*1.5) #Buffer to prevent overfilling of backlog


        log(f"Printed {file_name} with quantity {quantity}")
        files_printed += 1 # increment the counter
    log(f"{files_printed} files printed")  # Log the final count


def log(message):
    log_listbox.insert(tk.END, message)


def select_files():
    files = filedialog.askopenfilenames(filetypes=[("Label files", "*.ezpx")])
    for file in files:
        file_listbox.insert(tk.END, os.path.basename(file))
        selected_files.append(file)
    file_count_label.config(text=f"{len(selected_files)} files selected") # Update the file count

def on_right_click(event):
    # Determine the index of the selected file
    selected_index = file_listbox.curselection()
    
    # If a file is selected, create and show the context menu
    if selected_index:
        selected_index = selected_index[0]  # curselection returns a tuple, so get the first element
        context_menu = tk.Menu(root, tearoff=0)
        context_menu.add_command(label="Remove File", command=lambda: remove_selected_file(selected_index))
        context_menu.tk_popup(event.x_root, event.y_root)

def remove_selected_file(selected_index):
    file_listbox.delete(selected_index)
    del selected_files[selected_index]
    file_count_label.config(text=f"{len(selected_files)} files selected")


# GUI setup
root = tk.Tk()
root.title("Label Printing Manager V1.0 - Western Equipment Manufacturing")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_columnconfigure(5, weight=1) # Buffer to the right of the instructions
root.grid_columnconfigure(3, minsize=80) # Buffer to the right of the print quantity box

# Instructions Column
# Instructions Title (Bold)
instructions_title = tk.Label(root, text="Notes:", justify=tk.LEFT, anchor='n', font=("Helvetica", 10, "bold"))
instructions_title.grid(row=0, column=4, sticky='n') # Aligning to the top

# Instructions Content
instructions_text = """
1. Ensure that the correct label stock is loaded

2. Open ComplyPro Label Designer and wait for printer to connect before printing labels"""
instructions_label = tk.Label(root, text=instructions_text, justify=tk.LEFT, wraplength=200, anchor='n') # Create the content label
instructions_label.grid(row=1, column=4, sticky='n') # Below the title


file_count_label = tk.Label(root, text="0 files selected") # Label to show file count
file_count_label.grid(row=0, column=1, columnspan=3) # Positioned above file listbox

file_listbox = tk.Listbox(root, width=80, height=10)
file_listbox.grid(row=1, column=1, columnspan=3) # Centered by spanning three middle columns
file_listbox.bind("<Button-3>", on_right_click) # Bind the right-click event

select_button = tk.Button(root, text="Select Files", command=select_files)
select_button.grid(row=2, column=1) # Below the file listbox

quantity_label = tk.Label(root, text="Print Quantity:")
quantity_label.grid(row=2, column=2) # Same row as "Select Files" button

quantity_entry = tk.Entry(root)
quantity_entry.grid(row=2, column=3) # Next to "Print Quantity" label

log_listbox = tk.Listbox(root, width=80, height=10)
log_listbox.grid(row=3, column=1, columnspan=3) # Centered by spanning three middle columns

print_button = tk.Button(root, text="Print Labels", command=print_labels)
print_button.grid(row=4, column=1, columnspan=3) # Centered by spanning three middle columns

# Label to inform the user about the "Stop Printing" function
esc_label = tk.Label(root, text='press "ESC" to stop printing')
esc_label.grid(row=6, column=1, columnspan=3)

# List to store the full paths of selected files
selected_files = []

# Global flag to control the printing process
stop_flag = False

root.mainloop()


