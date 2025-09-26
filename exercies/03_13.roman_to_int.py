"""
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution:
    @staticmethod
    def roman_to_int(s: str) -> int:

        arr = []
        for i in s:
            arr.append(i)

        arr_int = []
        if arr:
            for i in arr:
                if i == 'I':
                    arr_int.append(1)
                elif i == 'V':
                    arr_int.append(5)
                elif i == 'X':
                    arr_int.append(10)
                elif i == 'L':
                    arr_int.append(50)
                elif i == 'C':
                    arr_int.append(100)
                elif i == 'D':
                    arr_int.append(500)
                elif i == 'M':
                    arr_int.append(1000)

        result = 0
        if arr_int:
            for i in range(len(arr_int)-1):
                if arr_int[i] < arr_int[i + 1]:
                    result -= arr_int[i]
                else:
                    result += arr_int[i]
            result += arr_int[-1]
            print(result)
            return result
        else:
            return 0

    # print(romanToInt('MCMXCIV'))
