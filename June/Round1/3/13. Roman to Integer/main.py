class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the mappings of integers to Roman numerals
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman_num = ""
        i = 0
        # Loop through each symbol, stopping if num is 0
        while num > 0:
            # Determine the number of times the symbol can fit into num
            for _ in range(num // val[i]):
                roman_num += syms[i]
                num -= val[i]
            i += 1
        return roman_num

# Example usage:
sol = Solution()
print(sol.intToRoman(3749))  # Output: "MMMDCCXLIX"
print(sol.intToRoman(58))    # Output: "LVIII"
print(sol.intToRoman(1994))  # Output: "MCMXCIV"
