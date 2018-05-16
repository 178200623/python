from unittest import TestCase
from python.Exercise.Py47.Py47 import Room

class TestRoom(TestCase):

    def test_room(self):
        gold = Room("GoldRoom", '''
           this room has gold in it you can grab.
           There's a door to the north.
           ''')
        assert gold.name == "GoldRoom"
        assert gold.paths=={},'111'

    def test_room_paths(self):
        center = Room("Center", "Test room in the center.")
        north = Room("North", "Test room in the north.")
        south = Room("South", "Test room in the south.")

        center.add_paths({'north': north, 'south': south})
        assert center.go('north') == 1,"aaaaa"
        assert center.go('south'), south

    def test_map(self):
        start = Room("start", "Youcan west and down a hole.")
        west = Room("Trees", "There are trees here,youcan go east.")
        down = Room("Dungeon", "It's dark down here,youcan go up.")

        start.add_paths({'west': west, 'down': down})
        west.add_paths({'east': start})
        down.add_paths({'up': start})

        assert start.go('west'), west
        assert start.go('west').go('east'), start
        assert start.go('down').go('up'), start