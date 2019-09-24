class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        for digit in digits:
            string += str(digit)
        number = int(string)  + 1
        st_ls = list(str(number))
        digits = [int(c) for c in st_ls]
        return digits
