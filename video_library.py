from library_item import LibraryItem

library = {}
library["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4, description="The movie is about the never-ending chase between Tom, a mischievous cat, and Jerry, a smart and cunning mouse. Although they always try to surpass each other and defeat the other, there is always a deep love and friendship between the two characters.")
library["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5, description="This is the story of a young woman in New York City who meets a young man when he moves into her apartment building. He is with an older woman who is very wealthy, but he wants to be a writer. She is working as an expensive escort and searching for a rich, older man to marry. But like Cinderella, it is a story about struggling to escape.")
library["03"] = LibraryItem("Casablanca", "Michael Curtiz", 2, description="Filmed and set during World War II, it focuses on an American expatriate (Bogart) who must choose between his love for a woman (Bergman) and helping her husband (Henreid), a Czechoslovak resistance leader, escape from the Vichy-controlled city of Casablanca to continue his fight against the Germans.")
library["04"] = LibraryItem("The Sound of Music", "Robert Wise", 1, description="A tuneful, heartwarming story, it is based on the real life story of the Von Trapp Family singers, one of the world's best-known concert groups in the era immediately preceding World War II. Maria, the tomboyish postulant at an Austrian abbey who becomes a governess in the home of a widowed naval captain with seven children, and brings a new love of life and music into the home.")
library["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3, description="A sheltered and manipulative Southern belle and a roguish profiteer face off in a turbulent romance as the society around them crumbles with the end of slavery and is rebuilt during the Civil War and Reconstruction periods. The epic tale of a woman's life during one of the most tumultuous periods in America's history.")

def get_name(video_id):
    item = library.get(video_id)
    return item.name if item else None

def get_director(video_id):
    item = library.get(video_id)
    return item.director if item else None

def get_rating(video_id):
    item = library.get(video_id)
    return '★' * item.rating if item else None

def get_play_count(video_id):
    item = library.get(video_id)
    return item.play_count if item else None

def get_description(video_id):
    item = library.get(video_id)
    return item.description if item else "No description available"

def list_all():
    return "\n".join(f"Video {key} - {val.name} - {val.director} - {'★' * val.rating}" for key, val in library.items())

def add_video(video_id, name, director, rating, description="No description available", play_count=0):
    if video_id not in library:
        library[video_id] = LibraryItem(name, director, rating, play_count, description)
        return True
    return False

def increment_play_count(video_id):
    if video_id in library:
        library[video_id].play_count += 1

def update_rating(video_id, new_rating):
    if video_id in library:
        library[video_id].rating = new_rating
        return True
    return False       

def get_all_video_ids():
    return list(library.keys())

def list_by_director(director_name):
    filtered_videos = [(item.name, '★' * item.rating, item.description) for item in library.values() if item.director.lower() == director_name.lower()]
    if filtered_videos:
        return "\n".join(f"Video name: {name}\nRating: {rating}\nDescription: {description}" for name, rating, description in filtered_videos)
    return None

def get_key_by_name(movie_name):
    for key, item in library.items():
        if item.name.lower() == movie_name.lower():
            return key
    return None

def list_by_rating(rating):
    filtered_videos = [(item.name, item.director, item.description) for item in library.values() if item.rating == rating]
    return "\n".join(f"Video name: {name}\nDirector name: {director}\nRating: {'★' * rating}\nDescription: {description}" for name, director, description in filtered_videos) if filtered_videos else None
