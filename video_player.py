import tkinter as tk
import font_manager as fonts
from check_videos import CheckVideos
from create_video_list import CreateVideoList
from update_videos import UpdateVideos

def update_status_message(name):
    status_label.configure(text=f"Welcome {name}, My name is Video Player!")

def submit_name():
    name = name_entry.get()
    if name:
        update_status_message(name)
    else:
        status_label.configure(text="Please enter your name!")

def toggle_theme():
    global theme_index
    themes = [
        {"bg": "white", "fg": "black", "entry_bg": "white", "entry_fg": "black", "button_bg": "lightgray", "button_fg": "black", "button_text": "Change Theme"},
        {"bg": "lightcoral", "fg": "black", "entry_bg": "lightcoral", "entry_fg": "black", "button_bg": "salmon", "button_fg": "black", "button_text": "Change Theme"},
        {"bg": "lightblue", "fg": "black", "entry_bg": "lightblue", "entry_fg": "black", "button_bg": "skyblue", "button_fg": "black", "button_text": "Change Theme"},
        {"bg": "lightgray", "fg": "black", "entry_bg": "lightgray", "entry_fg": "black", "button_bg": "darkgray", "button_fg": "black", "button_text": "Change Theme"}
        
    ]
    
    theme = themes[theme_index]
    main_window.configure(bg=theme["bg"])
    header_label.configure(bg=theme["bg"], fg=theme["fg"])
    status_label.configure(bg=theme["bg"], fg=theme["fg"])
    enter_name_label.configure(bg=theme["bg"], fg=theme["fg"])
    name_entry.configure(bg=theme["entry_bg"], fg=theme["entry_fg"])
    submit_button.configure(bg=theme["button_bg"], fg=theme["button_fg"])
    change_theme_button.configure(text=theme["button_text"])
    
    theme_index = (theme_index + 1) % len(themes)

theme_index = 0 

main_window = tk.Tk()
main_window.geometry("570x230")
main_window.title("Video Player")

fonts.configure()

def check_videos():
    status_label.configure(text="Check Videos button was clicked!")
    CheckVideos(tk.Toplevel(main_window))

def create_video_list():
    status_label.configure(text="Create Video List button was clicked!")
    CreateVideoList(tk.Toplevel(main_window))

def update_videos():
    status_label.configure(text="Update Videos button was clicked!")
    UpdateVideos(tk.Toplevel(main_window))

def exit_application():
    thank_you_window = tk.Toplevel(main_window)
    thank_you_window.geometry("300x60")
    thank_you_window.title("Video Player Shut Down")
    tk.Label(thank_you_window, text="Thank you for using the Video Player!", font=("Helvetica", 12)).pack(pady=20)
    thank_you_window.after(2000, main_window.destroy)

main_window.configure(bg="white")

header_label = tk.Label(main_window, text="Select an option by clicking one of the buttons below", bg="white", fg="black")
header_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

check_videos_button = tk.Button(main_window, text="Check Videos", command=check_videos)
check_videos_button.grid(row=1, column=0, padx=10, pady=10)

create_video_list_button = tk.Button(main_window, text="Create Video List", command=create_video_list)
create_video_list_button.grid(row=1, column=1, padx=10, pady=10)

update_videos_button = tk.Button(main_window, text="Update Videos", command=update_videos)
update_videos_button.grid(row=1, column=2, padx=10, pady=10)

exit_button = tk.Button(main_window, text="Exit", command=exit_application)
exit_button.grid(row=1, column=3, padx=10, pady=10)

status_label = tk.Label(main_window, text="", font=("Helvetica", 10), bg="white", fg="black")
status_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

enter_name_label = tk.Label(main_window, text="Enter your name:", bg="white", fg="black")
enter_name_label.grid(row=2, column=0, padx=10, pady=10)

name_entry = tk.Entry(main_window, bg="white", fg="black")
name_entry.grid(row=2, column=1, padx=10, pady=10)

submit_button = tk.Button(main_window, text="Submit", command=submit_name, bg="lightgray", fg="black")
submit_button.grid(row=2, column=2, padx=10, pady=10)

change_theme_button = tk.Button(main_window, text="Change Theme", command=toggle_theme)
change_theme_button.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

main_window.mainloop()
