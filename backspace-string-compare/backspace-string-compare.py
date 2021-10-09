class Solution:
    def backspaceCompare(self, str1: str, str2: str) -> bool:
        str1_arr = list(str1)
        str2_arr = list(str2)

        new_arr1 = []
        new_arr2 = []

        for i in range(len(str1_arr)):
            if str1_arr[i] == '#':
                if len(new_arr1) > 0:
                    new_arr1.pop()
                
            else:
                new_arr1.append(str1_arr[i])

        for i in range(len(str2_arr)):
            if str2_arr[i] == '#':
                if len(new_arr2) > 0:
                    new_arr2.pop()
            else:
                new_arr2.append(str2_arr[i])
        print(new_arr1)
        print(new_arr2)
        if new_arr2 != new_arr1:
            return False
        else:
            return True
