import tkinter as tk
import video_library as lib

class UpdateVideos:
    def __init__(self, main_window):
        main_window.geometry("700x200")
        main_window.title("Update Video Rating")

        self.movie_listbox = tk.Listbox(main_window, width=40, height=10, selectmode=tk.SINGLE)
        self.movie_listbox.grid(row=0, column=0, padx=10, pady=10, rowspan=2)

        update_frame = tk.Frame(main_window)
        update_frame.grid(row=0, column=1, padx=10, pady=10, rowspan=2)

        self.video_name_label = tk.Label(update_frame, text="Enter Video Name:")
        self.video_name_label.grid(row=0, column=0, padx=10, pady=5)

        self.video_name_entry = tk.Entry(update_frame, width=15)
        self.video_name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.rating_label = tk.Label(update_frame, text="Enter New Rating:")
        self.rating_label.grid(row=1, column=0, padx=10, pady=5)

        self.new_rating_entry = tk.Entry(update_frame, width=15)
        self.new_rating_entry.grid(row=1, column=1, padx=10, pady=5)

        update_button = tk.Button(update_frame, text="Update Rating", command=self.modify_rating)
        update_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.message_label = tk.Label(update_frame, text="", font=("Helvetica", 10))
        self.message_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.load_movies()

    def load_movies(self):
        self.movie_listbox.delete(0, tk.END)
        for video_id in lib.get_all_video_ids():
            video_name = lib.get_name(video_id)
            video_rating = lib.get_rating(video_id)
            self.movie_listbox.insert(tk.END, f"{video_name} - {video_rating}")

    def modify_rating(self):
        video_name = self.video_name_entry.get().strip()
        try:
            new_rating = int(self.new_rating_entry.get().strip())
        except ValueError:
            self.message_label.configure(text="The rating must be an integer.")
            return

        if new_rating < 1 or new_rating > 5:
            self.message_label.configure(text="Rating must be between 1 and 5")
            return

        video_id = lib.get_key_by_name(video_name)
        if not video_id:
            self.message_label.configure(text="Video is not found.")
            return

        if lib.update_rating(video_id, new_rating):
            updated_rating = lib.get_rating(video_id)
            self.message_label.configure(text=f"{video_name} rating updated to: {updated_rating}")
            self.load_movies()
        else:
            self.message_label.configure(text="Failed to update rating. Please try again.")


if __name__ == "__main__":
    main_window = tk.Tk()
    application = UpdateVideos(main_window)
    main_window.mainloop()
