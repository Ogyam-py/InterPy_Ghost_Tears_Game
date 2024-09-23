import csv

# Creating the player class
class Player:
    # constructing the class attributes
    def __init__(self, name:str = "Player 1"):
        self.name = name
        self.score = 0
        self.lives = 5

    def weakness(self, word):
        # Constracting data to be recorded
        data = {"name":self.name, "country":word}

        # writing into the csv file.
        with open("weaknessDB.csv", "w") as weakness_fh:
            obj = csv.DictWriter(weakness_fh, ["name", "country"], delimiter=",")
            obj.writeheader()

            obj.writerow(data)


if __name__ == "__main__":
    player1 = Player("Kofi")
    player1.weakness("USA")
