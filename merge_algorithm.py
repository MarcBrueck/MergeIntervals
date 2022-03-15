from collections import defaultdict

test_list1 = [[25, 30], [2, 19], [14, 23], [4, 8]]
test_list2 = [[14, 19], [12, 29], [-3, 12], [-3, 1], [31, 34]]
test_list3 = [[3, 6]]
test_list4 = [[14, 'abs'], [12, 29], [-3, 12], [-3, 1], [31, 34]]
test_list5 = [[14, 16], [12, 29], 3, [-3, 1], [31, 34]]

class IntervalCombinator:

    @staticmethod
    def merge(interval_list: list[list[int]], use_own_sorting=True) -> list[list[int]]:
        """
        Function that takes a list of intervals and merges the overlapping parts, then returns new list
        Example: [[25, 30], [2, 19], [14, 23], [4, 8]] -> [[2, 23], [25, 30]]
        Parameters
        ----------
        interval_list : list
            Input list that contains the intervals which are getting merged
        use_own_sorting : bool
            Decides whether to use build in python sort algorithm or own merge sort algorithm
        Returns
        -------
        new_list: list
            Output list which contains the sorted and merged intervals
        """

        if not interval_list:
            return []

        IntervalCombinator._test_input(interval_list)  # test if input is valid    O(N)

        if use_own_sorting:
            interval_list = IntervalCombinator._merge_sort_intervals(interval_list)  # Merge sort O(N log(N))

        if not use_own_sorting:
            interval_list.sort(key=lambda x: x[0])  # Timsort O(N log(N))

        new_list = [interval_list[0]]
        # Merge the sorted intervals
        for interval in interval_list[1:]:  # Iterating over list O(N)
            if new_list[-1][1] >= interval[0]:
                new_list[-1][1] = max(new_list[-1][1], interval[1])  # Changing list entries O(1)
            else:
                new_list.append(interval)
        # Total time complexity: O(N log N) + O(N) + O(1) -> O(N log(N))
        # Space Complexity: we store input values in new array -> O(N)
        return new_list

    @staticmethod
    def _test_input(interval_list: list):
        """
        Test the validity of the input for the merge method.
        interval_list needs to be list of list with 2 numbers
        Parameters
        ----------
        interval_list : list
            Input list that contains the intervals which are getting merged

        Returns
        -------

        """
        for interval in interval_list:  # Iterating over list O(N)
            if type(interval) != list:
                raise ValueError("interval_list needs to be list of lists with  2 numbers")
            if len(interval) != 2:
                raise ValueError("interval_list needs to be list of lists with  2 numbers")
            if not (type(interval[0]) == int or type(interval[0]) == float):
                raise ValueError("interval_list needs to be list of lists with 2 numbers")
            if not (type(interval[1]) == int or type(interval[1]) == float):
                raise ValueError("interval_list needs to be list of lists with 2 numbers")

    @staticmethod
    def _merge_sort_intervals(interval_list: list[list[int]]) -> list[list[int]]:
        """
        Uses the merge sort algorithm to sort the interval list
        Parameters
        ----------
        interval_list : list
            Input list that contains the intervals which are getting merged

        Returns
        -------
        output : list
            Output list that contains the sorted and merged intervals
        """
        # First we need to prepare the input, so we can apply the merge sort for 1-dim array
        interval_index = defaultdict(list)
        sorting_list = []
        output = []
        for interval in interval_list:  # Iterating over list O(N)
            interval_index[interval[0]].append(interval[1])
            sorting_list.append(interval[0])

        # Now the very well known merge sort algorithm can be used to sort 1-dimensional list
        IntervalCombinator._simple_merge_sort(sorting_list)  # O(N log(N))

        # Construct an interval list from the sorted array
        for index in sorting_list:
            for interval_end in interval_index[index]:
                output.append([index, interval_end])
        return output

    @staticmethod
    def _simple_merge_sort(arr: list):
        """
        Famous merge sort algorithm for sorting a one dimensional array
        Parameters
        ----------
        arr: list
            Contains the numbers that are to be sorted

        Returns
        -------

        """
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            IntervalCombinator._simple_merge_sort(left)

            IntervalCombinator._simple_merge_sort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1


if __name__ == '__main__':
    combinator = IntervalCombinator()
    test_list = combinator.merge(test_list3)
    print(test_list)

