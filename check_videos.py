import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts
from PIL import Image, ImageTk

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Delete existing content
    text_area.insert("1.0", content)  # Enter text

def rating_to_stars(rating):
    max_rating = 5  
    full_star = '★'
    empty_star = '☆'
    
    stars = full_star * min(rating, max_rating)  
    stars += empty_star * (max_rating - min(rating, max_rating))  
    
    return stars

class CheckVideos:
    def __init__(self, window):
        window.geometry("1000x500")  # Set the size of the window to accommodate new elements
        window.title("Check Videos")  # Set the window's title

        top_frame = tk.Frame(window)  # Create top frame
        top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")  # Set grid appearance

        list_videos_btn = tk.Button(top_frame, text="List All Videos", command=self.list_videos_clicked)  # Button to list all videos
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10, sticky="ew")  # Set grid appearance

        enter_id_lbl = tk.Label(top_frame, text="Enter Video Number")  # Make a label to instruct users on entering video number
        enter_id_lbl.grid(row=0, column=1, padx=10, pady=10)  # Set grid appearance

        self.input_id_txt = tk.Entry(top_frame, width=20)  # The area where users can input the video number
        self.input_id_txt.grid(row=0, column=2, padx=10, pady=10)  # Set grid appearance

        check_video_btn = tk.Button(top_frame, text="Check Video Number", command=self.check_video_clicked)  # Create a button labeled "Check Video Number", and upon clicking it, the check_video_clicked method is called
        check_video_btn.grid(row=0, column=3, padx=10, pady=10, sticky="ew")  # Set grid appearance

        enter_name_lbl = tk.Label(top_frame, text="Enter Video Name")  # Make a label to instruct users on entering movie name
        enter_name_lbl.grid(row=1, column=1, padx=10, pady=10)  # Set grid appearance

        self.input_name_txt = tk.Entry(top_frame, width=20)  # The area where users can input the movie name
        self.input_name_txt.grid(row=1, column=2, padx=10, pady=10)  # Set grid appearance 

        check_name_btn = tk.Button(top_frame, text="Check Video Name", command=self.check_movie_name_clicked)  # Create a button labeled "Check Video Name", and upon clicking it, the check_movie_name_clicked method is called
        check_name_btn.grid(row=1, column=3, padx=10, pady=10, sticky="ew")  # Set grid appearance

        enter_dir_lbl = tk.Label(top_frame, text="Enter Director Name")  # Make a label to instruct users on entering director name
        enter_dir_lbl.grid(row=2, column=1, padx=10, pady=10)  # Set grid appearance

        self.input_dir_txt = tk.Entry(top_frame, width=20)  # The area where users can input the director name
        self.input_dir_txt.grid(row=2, column=2, padx=10, pady=10)  # Set grid appearance 

        check_director_name_btn = tk.Button(top_frame, text="Check Director Name", command=self.check_director_name_clicked)  # Create a button labeled "Check Director Name", and upon clicking it, the check_director_name_clicked method is called
        check_director_name_btn.grid(row=2, column=3, padx=10, pady=10, sticky="ew")  # Set grid appearance

        enter_rating_lbl = tk.Label(top_frame, text="Enter Rating")  # Make a label to instruct users on entering rating
        enter_rating_lbl.grid(row=3, column=1, padx=10, pady=10)  # Set grid appearance

        self.input_rating_txt = tk.Entry(top_frame, width=20)  # The area where users can input the rating
        self.input_rating_txt.grid(row=3, column=2, padx=10, pady=10)  # Set grid appearance

        check_rating_btn = tk.Button(top_frame, text="Check Video Rating", command=self.check_video_rating_clicked)  # Create a button labeled "Check Video Rating", and upon clicking it, the check_video_rating_clicked method is called
        check_rating_btn.grid(row=3, column=3, padx=10, pady=10, sticky="ew")  # Set grid appearance

        middle_frame = tk.Frame(window)  # Create middle frame
        middle_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")  # Set grid appearance

        self.list_txt = tkst.ScrolledText(middle_frame, width=48, height=12, wrap="none")  # Make a text area which can be scrolled up and down
        self.list_txt.grid(row=0, column=0, columnspan=3, sticky="ew", padx=10, pady=10)  # Set grid appearance

        self.video_txt = tkst.ScrolledText(middle_frame, width=48, height=12, wrap="word")  # Updated to ScrolledText for scrolling and word wrap
        self.video_txt.grid(row=0, column=3, sticky="ew", padx=10, pady=10)  # Set grid appearance

        bottom_frame = tk.Frame(window)  # Create bottom frame
        bottom_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")  # Set grid appearance

        self.status_lbl = tk.Label(bottom_frame, text="", font=("Helvetica", 10))  # View the status of the video
        self.status_lbl.grid(row=0, column=0, columnspan=4, sticky="w", padx=10, pady=10)  # Set grid appearance

        self.list_videos_clicked()  # Invoke the list_videos_clicked function

        self.picture_library = {"01": "VideoPlayer COMP1752/Picture/tom_jerry.jpg", "02": "VideoPlayer COMP1752/Picture/Breakfast_at_Tiffany’s.jpg", "03": "VideoPlayer COMP1752/Picture/Casablanca.jpg", "04": "VideoPlayer COMP1752/Picture/The_sound_of_music.jpg", "05": "VideoPlayer COMP1752/Picture/Gone_with_the_wind.jpg"}  # Map video IDs to picture paths
        self.picture_lbl = tk.Label(window)  # Create and position a label to display the video image
        self.picture_lbl.grid(row=0, column=4, padx=10, pady=10)

        self.current_video_id = None  # Variable to store the current video ID

    def list_videos_clicked(self):
        video_list = lib.list_all()  # Obtain a list of all videos from lib
        set_text(self.list_txt, video_list)  # Display the list of videos
        self.status_lbl.configure(text="List Videos button was clicked!")  # Update the status
        self.current_video_id = None  # Clear current video ID after listing

    def check_video_clicked(self):
        key = self.input_id_txt.get()  # Obtain the entered video number
        self.current_video_id = key  # Update the current video ID
        name = lib.get_name(key)
        director = lib.get_director(key)
        rating = lib.get_rating(key)
        play_count = lib.get_play_count(key)
        description = lib.get_description(key)  # Retrieve description dynamically

        if name is not None:
            video_details = (f"Video name: {name}\n"
                         f"Director name: {director}\n"
                         f"Rating: {rating}\n"
                         f"Play count: {play_count}\n"
                         f"Description: {description}")
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, f"Video {key} is not found")

        self.status_lbl.configure(text="Check Video number button was clicked!")
        self.show_picture_clicked()  # Update picture display after checking

    def check_director_name_clicked(self):
        director_name = self.input_dir_txt.get().strip().lower()  # Convert input to lowercase
        video_list = lib.list_by_director(director_name)  # Call updated function
        
        if video_list:
            set_text(self.video_txt, video_list)  # Display the list of videos by the director
            self.current_video_id = None  # No specific video ID after listing by director
        else:
            set_text(self.video_txt, f"No video found for director: {director_name}")  # Display message if no videos found

        self.status_lbl.configure(text="Check Director Name button was clicked!")
        self.show_picture_clicked()  # Update picture display after checking

    def check_movie_name_clicked(self):
        movie_name = self.input_name_txt.get().strip()  # Get the entered movie name
        key = lib.get_key_by_name(movie_name)  # Retrieve the video number by movie name
        self.current_video_id = key  # Update the current video ID

        if key:
            director = lib.get_director(key)  # Retrieve the director name using the video number
            rating = lib.get_rating(key)  # Retrieve the rating using the video number
            description = lib.get_description(key)  # Retrieve the description using the video number

            movie_details = f"Director name: {director}\nRating: {rating}\nDescription: {description}"
            set_text(self.video_txt, movie_details)  # Provide movie details information and show it in a window
        else:
            set_text(self.video_txt, f"No video found with name: {movie_name}")  # Display message if movie is not found

        self.status_lbl.configure(text="Check Video Name button was clicked!")
        self.show_picture_clicked()  # Update picture display after checking

    def check_video_rating_clicked(self):
        rating_input = self.input_rating_txt.get()  # Get the rating from input_rating_txt Entry
        try:
            rating = int(rating_input)  # Convert the rating input to an integer
            videos = lib.list_by_rating(rating)  # Call list_by_rating() from video_library to get a list of videos by rating
            self.current_video_id = None  # No specific video ID after listing by rating

            if videos:
                set_text(self.video_txt, videos)  # Display videos in video_txt text area if found
            else:
                set_text(self.video_txt, f"No video found with rating: {rating}")  # Display message if no videos found
        except ValueError:
            set_text(self.video_txt, f"No video found with rating: {rating_input}")  # Handle the case where input is not a valid integer
            self.status_lbl.config(text="Please enter a valid rating number.")

        self.status_lbl.configure(text="Check Video Rating button was clicked!")
        self.show_picture_clicked()  # Update picture display after checking

    def show_picture_clicked(self):
        if self.current_video_id:
            self.create_image(self.current_video_id)  # Use the latest video ID
        else:
            # Check if any video was listed recently and use its ID if available
            if self.video_txt.get("1.0", tk.END).strip():
                video_ids = [line.split()[1] for line in self.video_txt.get("1.0", tk.END).splitlines() if line.startswith("Video ID:")]
                if video_ids:
                    self.create_image(video_ids[0])
                else:
                    self.picture_lbl.configure(image="")
            else:
                self.picture_lbl.configure(image="")  # Clear image if no video ID is set

    def create_image(self, key):
        picture_key = self.picture_library.get(key)  # Retrieve the picture file path using the video ID
        if picture_key:
            try:
                picture = Image.open(picture_key)  # Open the image file
                picture = picture.resize((170, 200))  # Resize the image to fit the label
                tk_picture = ImageTk.PhotoImage(picture)  # Convert image to PhotoImage for Tkinter
                self.picture_lbl.configure(image=tk_picture)  # Update the label with the new image
                self.picture_lbl.image = tk_picture  # Keep a reference to avoid garbage collection
            except Exception as e:
                self.picture_lbl.configure(image="")  # Clear image if there is an error
                print(f"Error loading image: {e}")  # Print error message
        else:
            self.picture_lbl.configure(image="")  # Clear image if no picture path is found

if __name__ == "__main__":
    window = tk.Tk()  # Create a TK object
    fonts.configure()  # Configure the fonts
    CheckVideos(window)  # Open the CheckVideo GUI
    window.mainloop()  # Run the window main loop, reacting to button presses, etc
