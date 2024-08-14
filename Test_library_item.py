from library_item import LibraryItem
def test_default_rating():
    key = LibraryItem("Casablanca","Michael Curtiz",0)
    assert key.name =="Casablanca"
    assert key.director =="Michael Curtiz"
    assert key.rating == 0
    assert key.play_count == 0
def test_video_details():
    key = LibraryItem("Casablanca", "Michael Curtiz",2)
    assert key.name =="Casablanca"
    assert key.director =="Michael Curtiz"
    assert key.rating == 2
    assert key.play_count == 0
def test_info():
    key = LibraryItem("Casablanca", "Michael Curtiz",2)
    assert key.info() =="Casablanca - Michael Curtiz ☆☆"
def test_stars():
    key = LibraryItem("Casablanca", "Michael Curtiz",2)
    assert key.stars() == "☆☆"
def test_play_count():
    key = LibraryItem("Casablanca", "Michael Curtiz",2)
    key.play_count +=1
    assert key.play_count == 1