class Spreadsheet:

    def __init__(self, rows: int):
        self.spreadSheet = [ [0]*26 for rows in range(rows)]
        

    def setCell(self, cell: str, value: int) -> None:
        r = int(cell[1:])-1
        col = ord(cell[0])-ord('A')
        self.spreadSheet[r][col] = value
        

    def resetCell(self, cell: str) -> None:
        #use setCell method above
        self.setCell(cell, 0)

    #custom method
    def getCellValue(self, cell:str)->int:
        if cell[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            r = int(cell[1:])-1
            col = ord(cell[0])-ord('A')
            return self.spreadSheet[r][col]
        
        else:
            return int(cell)

    def getValue(self, formula: str) -> int:
        form = formula[1:].split('+')
        val1 = form[0]
        val2 = form[1]

        return self.getCellValue(val1)+self.getCellValue(val2)
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)