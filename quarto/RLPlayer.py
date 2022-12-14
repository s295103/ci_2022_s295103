import Quarto


class RLPlayer(Quarto.Player):
    def __init__(self, quarto: Quarto.Quarto) -> None:
        super.__init__(quarto)

    def choose_piece(self) -> int:
        pass

    def place_piece(self) -> tuple[int, int]:
        pass
