class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        colNum = 0
        for char in columnTitle:
            colNum = colNum * 26 + (ord(char) - 64)
        return colNum