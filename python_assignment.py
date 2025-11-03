import numpy as np

def separator():
    print("\n---------------------------------------------------------------------------------------------------------------------")

def program_1():
    
    separator()
    
    # Program 1: Write a Python program to remove duplicates from a list.
    # Input:  [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    # Output: [10, 20, 30, 50, 60, 40, 80]

    # nums = input("Enter all the integers: ")
    # nums_arr = list(map(int, nums.split()))

    # nums = []

    nums_arr = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    nums = []
    num_map = set()

    print("Output:", end=" ")
    for i in nums_arr:
        if i not in num_map:
            nums.append(i)
            
        num_map.add(i)

    for i in nums:
        print(i, end=" ")
    
    separator()
    
def program_2():
    
    # Program 2: Write a Python program to find the list of words that are longer than n from a given list of words.
    # Input: "The quick brown fox" & 3
    # Output: quick brown
    
    # str = input("Enter the sentence")
    # n = int(input("Enter the threshold length"))

    str = "The quick brown fox"
    n = 3
    
    str = str.split(" ")

    print("Output:", end=" ")
    for i in str:
        if len(i) > n:
            print(i, end=" ")
            
    separator()

def program_3():
    
    # Program 3: Write a Python program to find the frequency of each element in a list and store it in a dictionary.
    # Input: [6,3,98,24,3,5,74,1,5,6,3]
    # Output: {6, 2}, {3, 3}, {98, 1}, {24, 1}, {5, 2}, {74, 1}, {1, 1}
    
    # nums = input("Enter all the integers: ")
    # nums_arr = list(map(int, nums.split()))

    nums_arr = [6, 3, 98, 24, 3, 5, 74, 1, 5, 6, 3]
    freq = {}

    for i in nums_arr:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] = freq[i] + 1

    print("Output:", end=" ")
    for key in freq.keys():
        print(f"{{{key}, {freq[key]}}}", end=" ")
        
    separator()
    
def program_4():
    
    # Program 4: Write a Python program to check if a list is a palindrome.
    # Input: [1, 2, 3, 2, 1]
    # Output: True
    # Input: [1, 2, 3, 2, 2] 
    # Output: False
    
    # nums = input("Enter all the integers: ")
    # nums_arr = list(map(int, nums.split()))
    
    nums_arr = [1, 2, 3, 2, 1]
    # nums_arr = [1, 2, 3, 2, 2] 

    l, r = 0, len(nums_arr)-1

    while l < r:
        if nums_arr[l] != nums_arr[r]:
            print("False")
            break
        l = l+1
        r = r-1

    print("True", end=" ")
    separator()

def program_5():
    
    # Program 5:  Given a list numbers that contains integers, write a Python program to separate out even and odd number:
    # Input: [54, 43, 2, 5, 14, 17, 18, 9]
    # Output: Even: 54 2 14 18, Odd: 43 5 17 19
    
    # nums = input("Enter all the integers: ")
    # nums_arr = list(map(int, nums.split()))
    
    nums_arr = [54, 43, 2, 5, 14, 17, 18, 9]
    
    even = []
    odd = []
    
    for i in nums_arr:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
            
            
    print("Output: Even: ", end=" ")
    for i in even:
        print(i, end=" ")
    
    print(", Odd:", end=" ")
    for i in odd:
        print(i, end=" ")
    
    separator()
        
def program_6():
    
    # Program 6: Given an array of integers, split the array into 3 equal parts
    # Input: [1, 3, 4, 0, 4]
    # Output: [1,3], [4], [0,4] -- Sum of each sub-array here is 4. 
    
    # nums = input("Enter all the integers: ")
    # nums_arr = list(map(int, nums.split()))
    
    nums_arr = [54, 43, 2, 5, 14, 17, 18, 9]
    n = len(nums_arr)
    sum = 0
    temp_sum = 0
    sub_arr = []
    temp_list = []
    
    for i in nums_arr:
        sum += i
    
    div = sum/3
    
    for i in range(0, n):

        if temp_sum >= div:
            sub_arr.append(temp_list)
            temp_list = []
            temp_sum = 0
        
        temp_sum += nums_arr[i]
        temp_list.append(nums_arr[i])
        
    
    print("Output:", end=" ")
    for i in sub_arr:
        print(i, end=" ")
    
    separator()

def program_7():
    
    # Program 7: Given an array of integers, write a Python program to count of distint integers in the list
    # Input: arr = [4, 4, 5, 4, 3, 8, 4, 2, 4, 8, 1, 7]
    # Output: 7
    
    # nums = input("Enter all the integers: ")
    # nums_arr = list(map(int, nums.split()))
    
    nums_arr = [4, 4, 5, 4, 3, 8, 4, 2, 4, 8, 1, 7]
    
    map = set()
    
    for i in nums_arr:
        map.add(i)
    
    print(f"Number of distinct elements: {len(map)}", end=" ")
    
    separator()
    
def program_8():
    
    # Program 8: Write a Python program to convert a given list of strings and characters to a single list of characters.
    # Original list:
    # ['red', 'white', 'a', 'b', 'black', 'f']
    # Convert the said list of strings and characters to a single list of characters:
    # ['r', 'e', 'd', 'w', 'h', 'i', 't', 'e', 'a', 'b', 'b', 'l', 'a', 'c', 'k', 'f']
    
    # string = input()
    # string = list(map(str, string.split()))
    
    string = ['red', 'white', 'a', 'b', 'black', 'f']
    characters = []
    
    for word in string:
        n = len(word)
        for i in range(0, n):
            characters.append(word[i])
    
    print("Characters:", end=" ")
    for i in characters:
        print(i, end=" ")
    
    separator()

def cp2():
    
    npStr_ascii = np.array([('Alice'), ('Bob')], dtype=[('name', 'S10')])
    npStr_unicode = np.array([('Alice'), ('Bob')], dtype=[('name', 'U10')])
    print(npStr_ascii.itemsize, npStr_ascii.nbytes)
    print(npStr_unicode.itemsize, npStr_unicode.nbytes)
    
    nums = [1,2,3,4,5]
    arr = [x*2 for x in nums]
    print(arr)

program_1()
program_2()
program_3()
program_4()
program_5()
program_6()
program_7()
program_8()

# cp2()