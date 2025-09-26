"""
Simple Bubble Sorting
Given: random list of numbers
Output: sorted list
"""


class Solving:
    # some_list = [1, 3, 8, 4, 5, 7, 9, 10, 2]
    # some_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    @staticmethod
    def bubble_sorting(arr: list) -> list:
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr

    # print(bubble_sorting(some_list))

