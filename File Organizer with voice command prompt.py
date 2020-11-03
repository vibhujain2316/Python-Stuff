
from tkinter import *   # For tkinter widgets and windows
from tkinter import filedialog      # For opening file explorer
from tkinter import messagebox      # For error, information, warning message boxes
import os       # For making directories and joining paths
import shutil       # For copying and moving files
from watchdog.observers import Observer     # For monitoring directories
from watchdog.events import FileSystemEventHandler      # Handing the events
import time     # For timing functions like sleep
from tkinter import ttk     # For tkinter widgets and windows
import pyttsx3  # For Voice Command Prompt

# =======================================================
#   End Of Import Sections
# =======================================================

# =======================================================
#   For Voice command prompt
# =======================================================

engine = pyttsx3.init()
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# =======================================================
#   End Of voice command prompt
# =======================================================

# =======================================================
#   Directory Monitoring variables and functions
# =======================================================
my_event_handler = FileSystemEventHandler()

def on_created(event):
    f_name = event.src_path
    res=f_name.partition('\\')
    monitor_box.configure(state=NORMAL)
    monitor_box.insert(END, f"A new File  named:\n{res[2]} has been Added to {res[0]}\n\n")
    monitor_box.configure(state=DISABLED)
    monitor_box.yview("end")


def on_deleted(event):
    f_name = event.src_path
    res = f_name.partition('\\')
    monitor_box.configure(state=NORMAL)
    monitor_box.insert(END, f"File Named:\n{res[2]}has been Deleted or Moved from {res[0]}\n\n")
    monitor_box.configure(state=DISABLED)
    monitor_box.yview("end")


def on_modified(event):
    f_name = event.src_path
    res = f_name.partition('\\')
    monitor_box.configure(state=NORMAL)
    monitor_box.insert(END, f"File Named:\n{res[2]} in directory {res[0]} has been Modified\n\n")
    monitor_box.configure(state=DISABLED)
    monitor_box.yview("end")


def tempForPathValue(path):
    global my_observer
    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=True)

# =======================================================
#   End Of Directory Monitoring variables and functions
# =======================================================


# =======================================================
#   START OF ROOT WINDOW
# =======================================================

root = Tk()  # Creating root window
root.resizable(0, 0)  # For Disabling the maximize button
root.title("File Organizer")  # Root Window TITLE
root.iconphoto(False, PhotoImage(file='Icon.png'))  # Root Window Icon

canvas = Canvas(root, bg="red", width=1150, height=650, borderwidth=0, bd=-2)  # Canvas Creation
canvas.pack()

bg_image = PhotoImage(file="bg1.png")  # Placing background image on canvas
image = canvas.create_image(575, 315, image=bg_image)

# =======================================================
#   Start of Menu Section
# =======================================================

def howtouse():     # For How to Use window
    how_to_use = Toplevel()
    how_to_use.resizable(0, 0)
    how_to_use.title("How To Use")
    how_to_use.iconphoto(False, PhotoImage(file='Icon.png'))
    helpText = """\nSTEPS TO USE THE FILE ORGANIZER:\n\n1. Click on the Browse Button and Select A Directory to monitor.\n\n2. Click on the Mark As Active Button to startthe monitoring of the directory you selected in the previous step.\n\n3. Now select the parent directory to which you want the file(s) to be moved.. Click on the Browse in the Select the parent directory section.\n\n4. After selection of the parent directory same will be visible in the directory selected bar...,Now Inside the parent directory make selection for an Existing folder or Make a new folder\n\n5. After Clicking the Existing Folder Button The Complete Path of the parent directory will be visible in Final Destination bar\n\n6. On clicking New Folder button type the name of new folder in the entry box and click on the Create button.\n\n7. After making the exact selection of the path of parent directory the same will be visible in Final Destination bar.\n\n8. Click on the Select Button to select the files to be moved.\n\n9. Click on the Move Button to move the files to the selected parent directory path."""
    helpLabel = Label(how_to_use, text="Hello!! FILE ORGANIZER Welcomes You", bg="black", fg="yellow",
                      font=("Audiowide", 15), justify=CENTER)
    helpLabel.pack()
    sc_bar = Scrollbar(how_to_use)
    sc_bar.pack(side=RIGHT, fill=Y)
    te_box = Text(how_to_use, width=100, height=80, bg="black", fg="yellow", borderwidth=10,
                  insertbackground="Yellow", insertwidth=5, wrap=WORD, font=("Mogalaris", 18))
    te_box.pack()
    te_box.insert(END, helpText)
    te_box.configure(state=DISABLED)
    te_box.config(yscrollcommand=sc_bar.set)
    sc_bar.config(command=te_box.yview)
    how_to_use.configure(bg="black")
    how_to_use.geometry("550x550+450+100")


def about():        # For about window
    aboutWindow = Toplevel()
    aboutWindow.resizable(0, 0)
    aboutWindow.title("About")
    aboutWindow.iconphoto(False, PhotoImage(file='Icon.png'))
    aboutText = """This is a simple File Organizer designed by Vibhu Jain using tkinter and various python modules for more info visit the github link below:\nhttps://github.com/vibhujain2316/Python-Stuff"""
    ab_box = Text(aboutWindow, width=150, height=80, bg="black", fg="yellow", borderwidth=5,
                  insertbackground="Yellow", insertwidth=5, wrap=WORD, font=("Mogalaris", 18))
    ab_box.pack()
    ab_box.insert(END, aboutText)
    ab_box.configure(state=DISABLED)
    aboutWindow.geometry("550x180+450+200")


menu_bar = Menu(root)  # Menu bar creation
root.config(menu=menu_bar)
create_menu = Menu(menu_bar, tearoff=0, activebackground="red", activeforeground="white", relief=SUNKEN,
                   font=("Audiowide", 12))
menu_bar.add_cascade(label="⁝☰", menu=create_menu)
create_menu.add_command(label="HOW TO USE?", command=howtouse)  # Adding button and label to menu bar
create_menu.add_command(label="ABOUT", command=about)       # # Adding button and label to menu bar
create_menu.add_separator()         # Adding seperator between menu bar items
create_menu.add_command(label="EXIT", command=root.quit)    # # Adding button and label to menu bar

# =======================================================
#   End of Menu Section
# =======================================================

# ======================================================
#    Functions
# ======================================================

# For Setting The Geometry of root Window
def forRootgeometry(winwd, winht):
    userscreenwidth = root.winfo_screenwidth()
    userscreenheight = root.winfo_screenheight()
    x = (userscreenwidth / 2) - (winwd / 2)
    y = (userscreenheight / 2.15) - (winht / 2)
    return x, y

# For Browsing directory for monitoring
def browseFiles():
    global choose_directory
    choose_directory = filedialog.askdirectory(initialdir="/", title="Select A Directory/Folder")
    if (len(choose_directory) != 0):
        tempForPathValue(choose_directory)
        folder_entry_box1.configure(state=NORMAL)
        folder_entry_box1.delete(0, END)
        folder_entry_box1.insert(0, choose_directory)
        folder_entry_box1.configure(state=DISABLED)
        # folder_entry_box1.configure(state=DISABLED,disabledbackground="#2be9ff",disabledforeground="red")
        browse_btn.configure(state=DISABLED)
        release_directory_btn.configure(state=NORMAL)
    elif (len(choose_directory) == 0):
        folder_entry_box1.configure(folder_entry_box1.insert(0, "Click Browse to Select"), state=DISABLED)

# For Selection of files to move
def forSelectButton():
    global con_filenames
    initial_dir = folder_entry_box1.get()
    if (folder_entry_box1.get() == "Click Browse to Select"):
        messagebox.showerror("ERROR", "PLEASE FIRST SELECT A DIRECTORY TO MONITOR")
    elif (directory_selected_entry_box2.get() == "Click Browse to Select"):
        messagebox.showerror("ERROR", "PLEASE FIRST SELECT A PARENT DIRECTORY")
    elif (len(final_destination_entry_box3.get()) == 0):
        messagebox.showerror("ERROR","THERE IS AN ERROR IN YOUR FILE SELECTION PLEASE RECHECK YOUR SELECTED DIRECTORY PATHS AND TRY AGAIN")
    else:
        con_filenames = 0
        filenames = filedialog.askopenfilenames(initialdir=f'{initial_dir}', title='Choose  file(s)')
        con_filenames = list(filenames)
        info_label.pack()
        info_label.configure(text=f"{len(con_filenames)} FILE(S) SELECTED")
        engine.say(str(len(con_filenames)) + "FILES SELECTED")
        engine.runAndWait()

# For Releasing the directory which is locked for Monitoring
def releaseButton():
    try:
        browse_btn.configure(state=NORMAL)
        folder_entry_box1.configure(state=NORMAL)
        folder_entry_box1.delete(0, END)
        folder_entry_box1.insert(0, "Click Browse to Select")
        folder_entry_box1.configure(state=DISABLED)
        browse_btn.pack()
        release_directory_btn.configure(state=DISABLED)
        frame17.destroy()
        my_observer.stop()
        my_observer.join()
        messagebox.showinfo("Task Successful", "Monitoring Stopped")
        mark_as_active_btn.configure(state=NORMAL)
    except NameError:
        folder_entry_box1.configure(state=NORMAL)
        folder_entry_box1.delete(0, END)
        folder_entry_box1.insert(0, "Click Browse to Select")
        folder_entry_box1.configure(state=DISABLED)

# For Browsing a parent directory for moving files into
def browseForParent():
    if (folder_entry_box1.get() == "Click Browse to Select"):
        messagebox.showwarning("FILE ORGANIZER ERROR", "PLEASE FIRST SELECT A DIRECTORY TO MONITOR")

    elif (len(choose_directory) != 0):
        global choose_parent_dir
        choose_parent_dir = filedialog.askdirectory(initialdir="/", title="Select A PARENT DIRECTORY")
        if (len(choose_parent_dir) == 0):
            directory_selected_entry_box2.configure(state=NORMAL)
            directory_selected_entry_box2.delete(0, END)
            directory_selected_entry_box2.insert(0, "Click Browse to Select")
            directory_selected_entry_box2.configure(state=DISABLED)
        else:
            directory_selected_entry_box2.configure(state=NORMAL)
            directory_selected_entry_box2.delete(0, END)
            directory_selected_entry_box2.insert(0, choose_parent_dir)
            directory_selected_entry_box2.configure(state=DISABLED)

# For selecting a directory inside a previouly selected parent directory
def forExistingFolderButton():
    try:
        if (len(choose_parent_dir) != 0):
            choose_existing_folder = filedialog.askdirectory(initialdir="choose_parent_dir",
                                                             title="Select AN EXISTING FOLDER")
            final_destination_entry_box3.configure(state=NORMAL)
            final_destination_entry_box3.delete(0, END)
            final_destination_entry_box3.insert(0, choose_existing_folder)
            final_destination_entry_box3.configure(state=DISABLED)
        elif (directory_selected_entry_box2.get() == "Click Browse to Select"):
            messagebox.showerror("ERROR", "CHOOSE A PARENT DIRECTORY FIRST")
    except NameError:
        messagebox.showerror("ERROR", "CHOOSE A PARENT DIRECTORY FIRST")

# For opening widget for entering new folder name and create button
def forMakingNewFolder():
    global create_btn, frame16, frame15
    global new_folder_entry3
    frame15 = Frame(canvas, bg="#031941")       # For new_folder_entry3
    frame16 = Frame(canvas, bg="#031941")       # For create_btn
    canvas.create_window(650, 400, window=frame15)      # For setting new_folder_entry3 on canvas
    canvas.create_window(900, 400, window=frame16)      # For setting create_btn on canvas
    try:
        if (len(choose_parent_dir) != 0):
            create_btn = Button(frame16, image=bt9_img, borderwidth=0, bg="#031941", activebackground="#031941",
                                command=forCreateButton)
            create_btn.pack()
            new_folder_entry3 = Entry(frame15, borderwidth=5, width=30, bg="#2be9ff", fg="red", insertbackground="red")
            new_folder_entry3.pack()
            new_folder_entry3.insert(0, "Enter New Folder Name")
            new_folder_entry3.bind('<Button-1>', onMouseClick)
            new_folder_btn.configure(state=DISABLED)
        elif (directory_selected_entry_box2.get() == "Click Browse to Select"):
            messagebox.showerror("ERROR", "CHOOSE A PARENT DIRECTORY FIRST")
    except NameError:
        messagebox.showerror("ERROR", "CHOOSE A PARENT DIRECTORY FIRST")

# For providing name to the new folder inside the parent directory and giving final command for its creation
def forCreateButton():
    folder_name = new_folder_entry3.get()
    complete_path = os.path.join(choose_parent_dir, folder_name)
    try:
        if (new_folder_entry3.get() == "Enter New Folder Name"):
            messagebox.showerror("ERROR", "PLEASE ENTER A VALID FOLDER NAME")
        else:
            os.mkdir(complete_path)
            messagebox.showinfo("TASK SUCCESSFUL", "FOLDER NAMED " + folder_name + " CREATED SUCCESSFULLY")
            final_destination_entry_box3.configure(state=NORMAL)
            final_destination_entry_box3.delete(0, END)
            final_destination_entry_box3.insert(0, complete_path)
            final_destination_entry_box3.configure(state=DISABLED)
    except PermissionError:
        messagebox.showerror("ERROR", "PLEASE ENTER A VALID FOLDER NAME")
    except OSError as error:
        messagebox.showerror("ERROR", "FOLDER ALREADY EXISTS, PLEASE CREATE NEW ONE WITH DIFFERENT NAME")
    frame15.destroy()
    frame16.destroy()
    new_folder_btn.configure(state=NORMAL)

# For moving the selected files from the monitored directory to the previously selected parent directory
def forMoveButton():
    try:
        if (len(con_filenames) == 0):
            messagebox.showerror("ERROR", "PLEASE FIRST SELECT FILES TO MOVE")
        else:
            path_to_move_files = final_destination_entry_box3.get()
            for files in con_filenames:
                shutil.move(files, path_to_move_files)
            info_label.configure(text=f"{len(con_filenames)} FILE(S) MOVED SUCCESSFULLY")
            engine.say(str(len(con_filenames)) + "FILES MOVED SUCCESSFULLY")
            engine.runAndWait()
    except NameError:
        messagebox.showerror("ERROR", "PLEASE FIRST SELECT FILES TO MOVE")
    except shutil.Error:
        messagebox.showerror("ERROR", "PLEASE FIRST SELECT FILES TO MOVE")
    except FileNotFoundError:
        messagebox.showerror("ERROR", "FILE NOT FOUND PLEASE RECHECK YOUR DIRECTORY")
    except FileExistsError:
        messagebox.showerror("ERROR", "FILE AlREADY EXISTS IN THE DESTINATION")

# For marking and locking the directory selected for monitoring
def forMarkAsActiveButton():
    if (folder_entry_box1.get() == "Click Browse to Select"):
        messagebox.showerror("ERROR", "FIRST SELECT A DIRECTORY TO MONITOR")
    else:
        global monitor_box, frame17, startprog_bar
        frame17 = Frame(canvas, bg="#031941")       # For monitor_box
        canvas.create_window(860, 90, window=frame17)       # For setting monitor_box on canvas
        browse_btn.pack_forget()
        scrollbar = Scrollbar(frame17)      # For making the scrollbar for monitor box
        scrollbar.pack(side=RIGHT, fill=Y)
        monitor_box = Text(frame17, width=45, height=6, bg="black", fg="white", borderwidth=10, relief=SUNKEN,
                           insertbackground="Yellow", insertwidth=5, wrap=WORD, cursor="arrow", font=13)
        monitor_box.pack()
        monitor_box.config(yscrollcommand=scrollbar.set)        # For setting the scrollbar to scroll on y axis
        scrollbar.config(command=monitor_box.yview)     # For selecting the window to be scrolled
        mark_as_active_btn.configure(state=DISABLED)
        monitor_box.insert(END, "Starting the monitor please wait.....")
        startprog_bar = ttk.Progressbar(monitor_box, orient=HORIZONTAL, length=350, mode='determinate')
        startprog_bar.pack(side=RIGHT, pady=55)
        engine.say("Starting the monitor, please wait")
        engine.runAndWait()
        for te in range(5):
            startprog_bar['value'] += 20
            monitor_box.update_idletasks()
            time.sleep(0.4)
        monitor_box.delete(1.0, END)
        startprog_bar.pack_forget()
        engine.say("Monitoring Started")
        engine.runAndWait()
        my_observer.start()

# Event binded for mouse click in the new folder name entry box
def onMouseClick(event):
    new_folder_entry3.delete(0, END)

# Event binded for speaking out the path of directory selected for monitoring
def ent1(event):
    if (folder_entry_box1.get() == "Click Browse to Select"):
        engine.say(folder_entry_box1.get())
        engine.runAndWait()
    else:
        engine.say("Directory Selected is " + folder_entry_box1.get())
        engine.runAndWait()

# Event binded for speaking out the path of directory selected as a parent directory
def ent2(event):
    if (directory_selected_entry_box2.get() == "Click Browse to Select"):
        engine.say(directory_selected_entry_box2.get())
        engine.runAndWait()
    else:
        engine.say("Directory Selected is " + directory_selected_entry_box2.get())
        engine.runAndWait()

# Event binded for speaking out the Complete path to the parent directory
def ent3(event):
    if (len(final_destination_entry_box3.get()) == 0):
        engine.stop()

    elif (final_destination_entry_box3.get() == "Click Browse to Select"):
        engine.say(final_destination_entry_box3.get())
        engine.runAndWait()
    else:
        engine.say("Final Directory is " + final_destination_entry_box3.get())
        engine.runAndWait()

# Event binded for stoping the voice command prompt
def voice_stop(event):
    engine.stop()


# =======================================================
#   End Of Function Sections
# =======================================================

# =======================================================
#   Button Images
# =======================================================
bt1_img = PhotoImage(file="Button1 Browse.png")         # Image for the First Browse button
bt2_img = PhotoImage(file="Button2 Release directory.png")      # Image for the Release Directory button
bt3_img = PhotoImage(file="Button3 Mark as active.png")     # Image for the Mark As Active button
bt4_img = PhotoImage(file="Button4 browse2.png")        # Image for the Second Browse button
bt5_img = PhotoImage(file="Button5 Existing folder.png")    # Image for the Existing Folder button
bt6_img = PhotoImage(file="Button6 New folder.png")     # Image for the New Folder button
bt7_img = PhotoImage(file="Button7 Select.png")     # Image for the Select button
bt8_img = PhotoImage(file="Button8 Move.png")       # Image for the Move  button
bt9_img = PhotoImage(file="Button9 Create folder.png")      # Image for the Create button

# =======================================================
#   End Of Button Images
# =======================================================

# =======================================================
#   Frame Creation
# =======================================================

frame1 = Frame(canvas, bg="#031941")  # For line1, line2, folder_entry_box1
frame2 = Frame(canvas, bg="#031941")  # For release_directory_btn
frame3 = Frame(canvas, bg="#031941")  # For browse_button
frame4 = Frame(canvas, bg="#031941")  # For mark_as_active_btn
frame5 = Frame(canvas, bg="#031941")  # For line3
frame6 = Frame(canvas, bg="#031941")  # For line4, directory_selected_entry_box2
frame7 = Frame(canvas, bg="#031941")  # For browse2_btn
frame8 = Frame(canvas, bg="#031941")  # For line5
frame9 = Frame(canvas, bg="#031941")  # For existing_folder_btn
frame10 = Frame(canvas, bg="#031941")  # For new_folder_btn
frame11 = Frame(canvas, bg="#031941")  # For line6, final_destination_entry_box3
frame12 = Frame(canvas, bg="#031941")  # For line7
frame13 = Frame(canvas, bg="#031941")  # For select_btn
frame14 = Frame(canvas, bg="#031941")  # For move_btn
frame18 = Frame(canvas, bg="#031941")

# =======================================================
#   End Of Frame Creation
# =======================================================

# =======================================================
#   Label And Entry Box Creation
# =======================================================

# For SELECT FILE/DIRECTORY TO MONITOR Label
line1 = Label(frame1, text="SELECT FILE/DIRECTORY TO MONITOR", bg="#031941", fg="#ff9b2b", font=("Audiowide", 20))
line1.grid(row=0, column=0, columnspan=50)

# For Folder label
line2 = Label(frame1, text="FOLDER :", bg="#031941", fg="#ff9b2b", font=("Audiowide", 20))
line2.grid(row=1, column=0)

# Entry box for path of the directory selected to monitor
folder_entry_box1 = Entry(frame1, borderwidth=5, width=65, disabledbackground="#2be9ff", disabledforeground="red",
                          cursor="arrow")
folder_entry_box1.grid(row=1, column=2)
folder_entry_box1.insert(0, "Click Browse to Select")
folder_entry_box1.configure(state=DISABLED)
folder_entry_box1.bind('<Button-1>', ent1)
folder_entry_box1.bind('<ButtonRelease-1>', voice_stop)

# For SELECT A PARENT DIRECTORY TO MOVE FILES label
line3 = Label(frame5, text="SELECT A PARENT DIRECTORY TO MOVE FILES", bg="#031941", fg="#ff9b2b",
              font=("Audiowide", 20))
line3.grid(row=0, column=0, columnspan=50)

# For DIRECTORY SELECTED Label
line4 = Label(frame6, text="DIRECTORY SELECTED :", bg="#031941", fg="#ff9b2b", font=("Audiowide", 20))
line4.grid(row=0, column=0)

# Entry box for selected parent directory
directory_selected_entry_box2 = Entry(frame6, borderwidth=5, width=65, disabledbackground="#2be9ff",
                                      disabledforeground="red", cursor="arrow")
directory_selected_entry_box2.grid(row=0, column=1)
directory_selected_entry_box2.insert(0, "Click Browse to Select")
directory_selected_entry_box2.configure(state=DISABLED)
directory_selected_entry_box2.bind('<Button-1>', ent2)
directory_selected_entry_box2.bind('<ButtonRelease-1>', voice_stop)

# For CHOOSE FOR MOVING FILES INSIDE PARENT DIRECTORY Label
line5 = Label(frame8, text="CHOOSE FOR MOVING FILES INSIDE PARENT DIRECTORY", bg="#031941", fg="#ff9b2b",
              font=("Audiowide", 20))
line5.grid(row=0, column=0)

# For FINAL DESTINATION Label
line6 = Label(frame11, text="FINAL DESTINATION :", bg="#031941", fg="#ff9b2b", font=("Audiowide", 20))
line6.grid(row=0, column=0)

# Entry box for final path to the directory
final_destination_entry_box3 = Entry(frame11, borderwidth=5, width=65, state=DISABLED, disabledbackground="#2be9ff",
                                     disabledforeground="red", cursor="arrow")
final_destination_entry_box3.grid(row=0, column=1)
final_destination_entry_box3.bind('<Button-1>', ent3)
final_destination_entry_box3.bind('<ButtonRelease-1>', voice_stop)

# For SELECT FILES TO MOVE label
line7 = Label(frame12, text="SELECT FILES TO MOVE", bg="#031941", fg="#ff9b2b", font=("Audiowide", 20))
line7.grid(row=0, column=0)

# For Displaying the files selected and files moved information label
info_label = Label(frame18, text="", bg="#031941", fg="#ff9b2b", font=("Audiowide", 12))
info_label.pack()
info_label.pack_forget()
# =======================================================
#   End Of Label And Entry Box Creation Section
# =======================================================

# =======================================================
#   Button Creation
# =======================================================

# For selecting a directory to monitor
browse_btn = Button(frame3, image=bt1_img, borderwidth=0, bg="#031941", activebackground="#031941", command=browseFiles)
browse_btn.pack()

# For releasing the directory selected to monitor
release_directory_btn = Button(frame2, image=bt2_img, borderwidth=0, bg="#031941",
                               activebackground="#031941", state=DISABLED, command=releaseButton)
release_directory_btn.pack()

# For marking the directory as active to monitor
mark_as_active_btn = Button(frame4, image=bt3_img, borderwidth=0, bg="#031941", activebackground="#031941",
                            command=forMarkAsActiveButton)
mark_as_active_btn.pack()

# For selecting the parent directory to move files
browse2_btn = Button(frame7, image=bt4_img, borderwidth=0, bg="#031941", activebackground="#031941",
                     command=browseForParent)
browse2_btn.pack()

# For selecting an existing folder inside the parent directory selected
existing_folder_btn = Button(frame9, image=bt5_img, borderwidth=0, bg="#031941", activebackground="#031941",
                             command=forExistingFolderButton)
existing_folder_btn.pack()

# For Opening widgets for entering new folder name and create button
new_folder_btn = Button(frame10, image=bt6_img, borderwidth=0, bg="#031941", activebackground="#031941",
                        command=forMakingNewFolder)
new_folder_btn.pack()

# For selection of files to be moved to the selected parent directory
select_btn = Button(frame13, image=bt7_img, borderwidth=0, bg="#031941", activebackground="#031941",
                    command=forSelectButton)
select_btn.pack()

# Move button for moving files to the selected parent directory
move_btn = Button(frame14, image=bt8_img, borderwidth=0, bg="#031941", activebackground="#031941",
                  command=forMoveButton)
move_btn.pack()

# =======================================================
#   End of Button Creation
# =======================================================

# =======================================================
#   Placing Widgets On Screen
# =======================================================
canvas.create_window(315, 48, window=frame1)        # For setting line1, line2, folder_entry_box1 on canvas
canvas.create_window(170, 140, window=frame2)       # For setting release_directory_btn on canvas
canvas.create_window(750, 70, window=frame3)        # For setting browse_button on canvas
canvas.create_window(410, 140, window=frame4)       # For setting mark_as_active_btn on canvas
canvas.create_window(377, 207, window=frame5)       # For setting line3 on canvas
canvas.create_window(398, 265, window=frame6)       # For setting line4, directory_selected_entry_box2 on canvas
canvas.create_window(920, 265, window=frame7)       # For setting browse2_btn on canvas
canvas.create_window(447, 328, window=frame8)       # For setting line5 on canvas
canvas.create_window(170, 400, window=frame9)       # For setting existing_folder_btn on canvas
canvas.create_window(410, 400, window=frame10)      # For setting new_folder_btn on canvas
canvas.create_window(381, 470, window=frame11)      # For setting line6, final_destination_entry_box3 on canvas
canvas.create_window(199, 545, window=frame12)      # For setting line7 on canvas
canvas.create_window(540, 550, window=frame13)      # For setting select_btn on canvas
canvas.create_window(980, 550, window=frame14)      # For setting move_btn on canvas
canvas.create_window(175, 587, window=frame18)      # For setting Info label on canvas
# =======================================================
#   End Of Placing Widgets On Screen
# =======================================================

X_coordinate, Y_coordinate = forRootgeometry(1150, 650)     # For calling the function for getting the x and y coordiantes to place the root window
root.geometry(f'{1150}x{650}+{int(X_coordinate)}+{int(Y_coordinate)}')      # For setting the dimensions of the root window

root.mainloop()     # Running the root window in a loop

