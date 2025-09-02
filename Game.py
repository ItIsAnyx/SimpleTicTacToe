from Field import Field
import random
from dataclasses import dataclass, field

@dataclass
class Game:
    current_field: Field
    playmode: str = field(default="None", init=False)
    playmode_variations: tuple = field(default_factory=lambda: ("playerfirst", "botfirst", "local"), init=False)
    available_cells: list = field(default_factory=lambda: ["a0", "a1", "a2", "b0", "b1", "b2", "c0", "c1", "c2", "exit", "restart"], init=False)

    def select_playmode(self) -> bool:
        selection: str = input("Choose your playmode:\nplayerfirst - you are making the first move\nbotfirst - bot are making his first move\nlocal - play with your friend on this device\nexit - break programm\n\n")
        while selection not in self.playmode_variations:
            if selection == "exit":
                return False
            print("Choose your playmode:\nplayerfirst - you are making the first move\nbotfirst - bot are making his first move\nlocal - play with your friend on this device\nexit - break programm\n")
            selection: str = input()
        self.playmode = selection
        self.start_game()
        return True

    def bot_logic(self) -> str:
        result: str = self.current_field.check_win_situation()
        if result != "None":
            return result
        else:
            if self.current_field.check_empty("b1"):
                self.available_cells.remove("b1")
                return "b1"
            else:
                result: str = random.choice(self.available_cells)
                while result in ("exit", "restart"):
                    result: str = random.choice(self.available_cells)
                self.available_cells.remove(result)
        print(result)
        return result

    def start_game(self) -> None:
        if self.playmode == "local":
            self.localgame()
        elif self.playmode == "playerfirst":
            self.botgame(2)
        elif self.playmode == "botfirst":
            self.botgame(1)

    def localgame(self) -> None:
        player: int = 1
        position: str = ""
        while self.current_field.check_victory() == 0:
            print(self.current_field)
            while position not in self.available_cells:
                position: str = input(
                    f"Enter correct position of your move. \nWrite \"exit\" for break the game or \"restart\" to clear the field and start again. \nNow moving {self.current_field.symbol_localization(player)}: ")
                if position == "exit":
                    return
            if not(position == "restart"):
                self.available_cells.remove(position)
                self.current_field.move(player, position)
                player: int = player * (-1) + 3
                print()
            else:
                self.current_field: Field = Field()
                self.available_cells: list = ["a0", "a1", "a2", "b0", "b1", "b2", "c0", "c1", "c2", "exit", "restart"]
                position: str = ""
                print()
        print(self.current_field)
        print(f"{self.current_field.symbol_localization(self.current_field.check_victory())} won!")

    def botgame(self, player: int) -> None:
        position: str = ""

        while self.current_field.check_victory() == 0:
            if player == 1:
                self.current_field.move(1, self.bot_logic())
                print(self.current_field)
                if self.current_field.check_victory() != 0:
                    print(f"{self.current_field.symbol_localization(self.current_field.check_victory())} won!")
                    return
                player: int = 2
            print(self.current_field)

            while position not in self.available_cells:
                position: str = input(
                    f"Enter correct position of your move. \nWrite \"exit\" for break the game or \"restart\" to clear the field and start again. \nNow moving {self.current_field.symbol_localization(player)}: ")
                if position == "exit":
                    return

            if not (position == "restart"):
                self.available_cells.remove(position)
                self.current_field.move(player, position)
                player: int = 1
                print()

            else:
                self.current_field: Field = Field()
                self.available_cells: list = ["a0", "a1", "a2", "b0", "b1", "b2", "c0", "c1", "c2", "exit", "restart"]
                position: str = ""
                print()

        print(self.current_field)
        print(f"{self.current_field.symbol_localization(self.current_field.check_victory())} won!")


keyword = "restart"
while keyword == "restart":
    new_field = Field()
    game = Game(new_field)
    game.select_playmode()
    keyword = input("\nWanna start new game? \nWrite restart if you want to play again or write any word if you want to break programm:\n")