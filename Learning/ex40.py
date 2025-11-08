class Song(object):

    def __init__(self,lyrics):
        self.狗 = lyrics

    def sing_me_a_song(self):
        for line in self.狗:
         print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"]) # []中的是列表
"""

happy_bday应用了Song中的init,
此时happy_bday=self,
    lyrics="Happy birthday to you",
           "I don't want to get sued",
           "So I'll stop right there"
    self.狗为变量, 等于lyrics的值

"""

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

"""

    happy_bday.sing_me_a_song(),
    相当于sing_me_a_song(happy_bday),
    但是sing_me_a_song(happy_bday)只能在独立函数中应用，
    class中的函数不算独立函数

"""


bulls_on_parade.sing_me_a_song()