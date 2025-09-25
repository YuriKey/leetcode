class Solution:
    # _x = 121

    @staticmethod
    def is_palindrome(x: int) -> bool:
        value_1 = str(x)
        value_2 = value_1[::-1]
        if value_1 == value_2:
            return True
        else:
            return False

    # print(is_palindrome(_x))
