import random



# creating the computer class
class Computer:
    def __init__(self) -> None:
        pass

    def randomfetch(self):
        with open("countries_and_capitals.txt") as f:
            game_data = Computer.cleaner(f.readlines())
            
            print(game_data)
    
    def cleaner(data:str):
        return [i.strip("\n") for i in data]


if __name__ == "__main__":
    virtual_player = Computer()
    virtual_player.randomfetch()
