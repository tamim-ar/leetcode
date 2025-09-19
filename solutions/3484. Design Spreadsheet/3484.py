class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.data = {}

    def setCell(self, cell: str, value: int) -> None:
        self.data[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.data:
            del self.data[cell]

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        x, y = formula.split("+")
        return self._get(x) + self._get(y)

    def _get(self, token: str) -> int:
        if token.isdigit():
            return int(token)
        return self.data.get(token, 0)
