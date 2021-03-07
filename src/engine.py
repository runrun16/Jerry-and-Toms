import random
from enum import Enum


class Context:
    __instance = None
    @staticmethod
    def get_instance():
        if Context.__instance is None:
            Context()
        return Context.__instance

    def __init__(self):
        if Context.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Context.__instance = self
        # TODO: if set not called, this will remain null
        self.cheese_x = None
        self.cheese_y = None

    def set_cheese_loc(self, x, y):
        self.cheese_x = x
        self.cheese_y = y

    def get_cheese_loc(self):
        return self.cheese_x, self.cheese_y


class Move(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Player:
    def move(self, x, y):
        context = Context.get_instance()
        cheese_x, cheese_y = context.get_cheese_loc()
        if x < cheese_x:
            return Move.DOWN
        if x > cheese_x:
            return Move.UP
        if y < cheese_y:
            return Move.RIGHT
        if y > cheese_y:
            return Move.LEFT


class Engine:
    def __init__(self):
        self.players = []
        self.players_loc = []
        self.context = Context.get_instance()
        self.m = 10
        self.n = 10

        # set cheese location
        cheese_x = random.randint(0, self.m)
        cheese_y = random.randint(0, self.n)
        self.context.set_cheese_loc(cheese_x, cheese_y)

    def add_player(self, player):
        self.players.append(player)
        x = random.randint(0, self.m)
        y = random.randint(0, self.n)
        self.players_loc.append([x, y])

    def update(self, x, y, move):
        if move == Move.UP and x > 0:
            x -= 1
        if move == Move.DOWN and x < self.m - 1:
            x += 1
        if move == Move.LEFT and y > 0:
            y -= 1
        if move == Move.RIGHT and y < self.n - 1:
            y += 1
        return x, y

    def start(self):
        game_on = True
        while game_on:
            for i, player in enumerate(self.players):
                x, y = self.players_loc[i]
                move = player.move(x, y)
                new_x, new_y = self.update(x, y, move)
                print(f"Player {i} move from {x},{y} to {new_x},{new_y}")
                self.players_loc[i] = new_x, new_y
                cheese_x, cheese_y = self.context.get_cheese_loc()
                if cheese_x == new_x and cheese_y == new_y:
                    print(f"{i} wins")
                    game_on = False
                    break

def main():
    engine = Engine()
    engine.add_player(Player())
    engine.add_player(Player())
    engine.start()

if __name__ == "__main__":
    main()
