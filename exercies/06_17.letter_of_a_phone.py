"""Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""


class Solution:
    @staticmethod
    def letter_combinations(digits: str) -> list[str]:
        filtered_digits = [d for d in digits if d not in '01']
        print(filtered_digits)
        if not filtered_digits:
            return []

        letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        def backtrack(index, current_comb):
            if index == len(filtered_digits):
                result.append(current_comb)
                return

            current_digit = filtered_digits[index]
            for letter in letters[current_digit]:
                backtrack(index + 1, current_comb + letter)

        result = []
        backtrack(0, "")
        return result


print(Solution.letter_combinations('32'))  # ['dd', 'de', 'df', 'ed', 'ee', 'ef', 'fd', 'fe', 'ff']
