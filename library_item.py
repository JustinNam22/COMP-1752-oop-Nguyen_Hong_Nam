class LibraryItem:
    all_items = []

    def __init__(self, name, director, rating=0, description="No description available"):
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = 0
        self.description = description  
        LibraryItem.all_items.append(self)

    def info(self):
        return f"{self.name} - {self.director} {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "☆"  
        return stars
