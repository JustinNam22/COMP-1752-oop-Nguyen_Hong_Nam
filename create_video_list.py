import tkinter as tk
import tkinter.scrolledtext as tkst
from PIL import Image, ImageTk
import video_library as lib
import random

def update_text_area(text_widget, text_content):
    text_widget.delete("1.0", tk.END)
    text_widget.insert("1.0", text_content)

class CreateVideoList:
    def __init__(self, main_window):
        self.video_list = []
        self.current_video_id = None

        main_window.geometry("800x400")
        main_window.title("Create Video List")

        label_input = tk.Label(main_window, text="Enter Video Number")
        label_input.grid(row=0, column=0, padx=10, pady=10)

        self.entry_input = tk.Entry(main_window, width=5)
        self.entry_input.grid(row=0, column=1, padx=10, pady=10)

        button_add_video = tk.Button(main_window, text="Add to List", command=self.add_video_to_list)
        button_add_video.grid(row=0, column=2, padx=10, pady=10)

        button_play_list = tk.Button(main_window, text="Play Video", command=self.play_video_list)
        button_play_list.grid(row=0, column=3, padx=10, pady=10)

        button_reset_list = tk.Button(main_window, text="Clear List", command=self.clear_video_list)
        button_reset_list.grid(row=2, column=2, padx=10, pady=10)

        button_random_video = tk.Button(main_window, text="Randomize Video", command=self.add_random_video_to_list)
        button_random_video.grid(row=2, column=3, padx=10, pady=10)

        self.video_list_display = tkst.ScrolledText(main_window, width=75, height=15, wrap="none")
        self.video_list_display.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.status_label = tk.Label(main_window, text="", font=("Helvetica", 10))
        self.status_label.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.picture_lbl = tk.Label(main_window)
        self.picture_lbl.grid(row=1, column=4, rowspan=2, padx=10, pady=10)

        self.picture_library = {"01": "VideoPlayer COMP1752/Picture/tom_jerry.jpg", "02": "VideoPlayer COMP1752/Picture/Breakfast_at_Tiffany’s.jpg", "03": "VideoPlayer COMP1752/Picture/Casablanca.jpg", "04": "VideoPlayer COMP1752/Picture/The_sound_of_music.jpg", "05": "VideoPlayer COMP1752/Picture/Gone_with_the_wind.jpg"}  # Map video IDs to picture paths
        self.picture_lbl = tk.Label(main_window)  # Create and position a label to display the video image
        self.picture_lbl.grid(row=1, column=4, padx=10, pady=10)

    def add_video_to_list(self):
        video_identifier = self.entry_input.get()
        video_name = lib.get_name(video_identifier)
        if video_name:
            self.video_list.append(video_identifier)
            self.current_video_id = video_identifier
            self.refresh_video_list_display()
            self.status_label.configure(text=f"Video {video_identifier} has been added to the list!")
            self.show_picture_clicked()
        else:
            self.status_label.configure(text=f"Video {video_identifier} is not found!")

    def refresh_video_list_display(self):
        video_names = [lib.get_name(video_identifier) for video_identifier in self.video_list]
        update_text_area(self.video_list_display, "\n".join(video_names))

    def play_video_list(self):
        for video_identifier in self.video_list:
            lib.increment_play_count(video_identifier)
        self.status_label.configure(text="Video is played! Play count has been increased.")

    def clear_video_list(self):
        self.video_list = []
        self.current_video_id = None
        update_text_area(self.video_list_display, "")
        self.status_label.configure(text="Video List is cleared!")
        self.picture_lbl.configure(image="")

    def add_random_video_to_list(self):
        all_videos = lib.get_all_video_ids()
        if all_videos:
            random_video = random.choice(all_videos)
            self.video_list.append(random_video)
            self.current_video_id = random_video
            self.refresh_video_list_display()
            self.status_label.configure(text=f"Random Video {random_video} has been added to the list!")
            self.show_picture_clicked()
        else:
            self.status_label.configure(text="No videos available to choose from!")

    def show_picture_clicked(self):
        if self.current_video_id:
            self.create_image(self.current_video_id)
        else:
            self.picture_lbl.configure(image="")

    def create_image(self, key):
        picture_key = self.picture_library.get(key)
        if picture_key:
            try:
                picture = Image.open(picture_key)
                picture = picture.resize((170, 200))
                tk_picture = ImageTk.PhotoImage(picture)
                self.picture_lbl.configure(image=tk_picture)
                self.picture_lbl.image = tk_picture
            except Exception as e:
                self.picture_lbl.configure(image="")
                print(f"Error loading image: {e}")
        else:
            self.picture_lbl.configure(image="")

if __name__ == "__main__":
    main_app = tk.Tk()
    video_list_app = CreateVideoList(main_app)
    main_app.mainloop()
