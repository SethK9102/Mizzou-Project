from saving import Database_manager

class Highscores:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.db = Database_manager()
    def update_hs(self):
        data = self.db.read()
        x = 0
        for i, j in data[1].items():
            x += 1
            if self.score >= j:
                data_items = list(data[1].items())
                data_items.insert(x, (self.name, self.score))
                data_items.pop()
                data[1] = dict(data_items)
        self.db.update(data)


    def create_hs(self):
        high_scores = {
            "AAA": 0,
            "BBB": 0,
            "CCC": 0,
            "DDD": 0,
            "EEE": 0,
            "FFF": 0,
            "GGG": 0,
            "HHH": 0,
            "III": 0,
            "JJJ": 0
        }
        self.db.create()
        self.db.add(high_scores)

    def get_hs(self):
        data = self.db.read()
        return data[1]
    
    def reset_hs(self):
        self.db.delete()
        self.create_hs()
        return True
    