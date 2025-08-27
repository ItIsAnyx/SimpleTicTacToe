class Field:
    def __init__(self) -> None:
        self._cells: dict[str, int] = {"a0": 0, "a1": 0, "a2": 0, "b0": 0, "b1": 0, "b2": 0, "c0": 0, "c1": 0, "c2": 0}
        self._moves: int = 0
        self._winning_combinations: list[list[str]] = [
            ["a0", "a1", "a2"],  # горизонтали
            ["b0", "b1", "b2"],
            ["c0", "c1", "c2"],
            ["a0", "b0", "c0"],  # вертикали
            ["a1", "b1", "c1"],
            ["a2", "b2", "c2"],
            ["a0", "b1", "c2"],  # диагонали
            ["a2", "b1", "c0"]
        ]

    def __getitem__(self, item: str) -> int:
        return self._cells[item]

    def check_empty(self, pos: str) -> bool:
        return self._cells[pos] == 0

    # 1 - bot, 2 - player
    def move(self, player: int, pos: str) -> bool:
        if self.check_empty(pos):
            self._cells[pos] = player
            self._moves += 1
            return True

        else:
            return False

    def moves_amount(self) -> int:
        return self._moves

    def get_cells(self, *cells: list[str] | str) -> list[int]:
        result = []
        for element in cells:
            result.append(self._cells[element])
        return result

    def check_victory(self) -> int:
        for combo in self._winning_combinations:
            if self._cells[combo[0]] != 0 and (self._cells[combo[0]] == self._cells[combo[1]] == self._cells[combo[2]]):
                return self._cells[combo[0]]
        if self.moves_amount() >= 9:
            return 3
        return 0

    def check_win_situation(self) -> str:
        important_moves: list[str] = []
        for combo in self._winning_combinations:
            for pos in range(3):
                if self._cells[combo[pos]] == self._cells[combo[(pos + 1) % 3]] and self._cells[combo[pos]] != 0 and self._cells[combo[(pos + 2) % 3]] == 0:
                    if self._cells[combo[pos]] == 2:
                        return combo[(pos + 2) % 3]
                    important_moves.append(combo[(pos + 2) % 3])
                    break
        if len(important_moves) == 0:
            return "None"
        return important_moves[0]



    @staticmethod
    def symbol_localization(symbol: int) -> str:
        symbols: dict[int, str] = {0: "#", 1: "X", 2: "0", 3: "No one"}
        return symbols[symbol]

    def __str__(self):
        return (("    0 1 2\n")+(f"a | {Field.symbol_localization(self._cells['a0'])} {Field.symbol_localization(self._cells['a1'])} {Field.symbol_localization(self._cells['a2'])} |") +
                (f"\nb | {Field.symbol_localization(self._cells['b0'])} {Field.symbol_localization(self._cells['b1'])} {Field.symbol_localization(self._cells['b2'])} |") +
                (f"\nc | {Field.symbol_localization(self._cells['c0'])} {Field.symbol_localization(self._cells['c1'])} {Field.symbol_localization(self._cells['c2'])} |"))
