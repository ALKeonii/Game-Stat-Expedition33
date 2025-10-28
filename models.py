# models.py

class GameStat:
    def __init__(self, id=None, party_name="", favorite_character="", achievements=0, time_played="", levels_reached=0):
        self.id = id
        self.party_name = party_name
        self.favorite_character = favorite_character
        self.achievements = achievements
        self.time_played = time_played
        self.levels_reached = levels_reached

    def __repr__(self):
        return f"<GameStat {self.party_name}, {self.favorite_character}>"