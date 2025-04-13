class Solution:
    def getInversions(self, arr):
        """
        For a given integer array/list 'ARR' of size 'N' containing all distinct values, 
        find the total number of 'Inversions' that may exist.
        An inversion is defined for a pair of integers in the array/list 
        when the following two conditions are met.
        A pair ('ARR[i]', 'ARR[j]') is said to be an inversion when:
            1. 'ARR[i] > 'ARR[j]' 
            2. 'i' < 'j'
        Where 'i' and 'j' denote the indices ranging from [0, 'N').
        Simple solution:
        Brute force:
        will be iterate over the array ARR and 
        for each element iterate over the array again with the above condition
        and only iterate after the given ith element.
        For given ith element, we only need to iterate the next remaining of the array
        because of the condition 2 that is 'i' < 'j'
        and while iterating just check for ith element which all element is lower in the remaining array 
        keep a count and return it
        if above conditions satisfies. keep a counter and increase it.
        """    
        # write your code here !!
        array_length = len(arr)
        count = 0
        for i in range(array_length):
            for j in range(i+1, array_length):                
                if arr[i] > arr[j]:
                    count += 1
            print()
        return count
    def run_test(self):
        a = self.getInversions([3,2,1, 0, -1])
        print(a)

a = Solution()
a.run_test()