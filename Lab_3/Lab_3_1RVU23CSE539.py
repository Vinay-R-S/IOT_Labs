# Vinay Saunshi | 1RVU23CSE539 | IOT LAB 3

"""
import os
print(os.environ)
path = os.environ.get('PATH')

os.environ['USERNAME']="Vinay"
print(os.environ.get('USERNAME'))

%env
%env USERNAME
%env MY_VAR= 'Hello from Vinay'

print(os.environ.get('MY_VAR'))
%env USERNAME
"""

# Exercise 1
def foo(num):
    print('foo is called with num = ',num)

def callFnFromList(myList):
  for i in range(len(myList)):
    if myList[i] is foo:
      foo(myList[i-1])

myList = [10,11,12,foo,14,15,foo,17,foo]
callFnFromList(myList)

# Exercise 1 with Error Check
def foo1(num):
  print('foo1() is called with num = ',num)

def callFnFromListWithErrChk(myList):
  if myList[0] is foo:
    for i in range(len(myList)):
      if myList[i] is foo:
        if type(myList[i-1]) is int:
          foo(myList[i-1])
      if myList[i] is foo1:
          if type(myList[i-1]) is int:
              foo1(myList[i-1])

myList=[foo,10,1,12,foo,14,15,foo,17,foo]
callFnFromListWithErrChk(myList)
myList = [foo, 10, 11, 'string', foo, 14, 15, foo, 17, foo]
callFnFromListWithErrChk(myList)
myList = [foo, 10, 11, 'string', foo, 14, 15, foo, 17, foo1]
callFnFromListWithErrChk(myList)

# Exercise 2
def fillMyMatrixInt(myMatrix):
    counter = 1

    for i in range(len(myMatrix)):
        row = myMatrix[i]

        if isinstance(row, list) and all(isinstance(x, list) for x in row):

            for j in range(len(row)):
                row[j] = [counter, counter + 1]
                counter += 2
        elif isinstance(row, list):

            myMatrix[i] = [counter, counter + 1]
            counter += 2

    return myMatrix

myMatrix1 = [[[], []],
             [[]],
             [[], [], []],
             []]
print(fillMyMatrixInt(myMatrix1))

myMatrix2 = [[[], []],
             [[]],
             [[], [], []],
             [[]],
             [[], [], []],
             []]

print(fillMyMatrixInt(myMatrix2))

# Exercise 3: Problem 1, Filling in Lists - recursive
def fillMyMatrixIntRecursive(myMatrix, counter=[1]):
    if isinstance(myMatrix, list):
        if len(myMatrix) == 0:
            start = counter[0]
            counter[0] += 2
            return [start, start + 1]
        else:
            return [fillMyMatrixIntRecursive(sub, counter) for sub in myMatrix]
    return myMatrix

myMatrix7 = [
    [ [[[]]], [[[]]], [[[]]] ],
    [ [] ],
    [ [], [], [[[], []]], [] ],
    [ [] ],
    [ [], [], [] ],
    [[]],
    []
]

print(fillMyMatrixIntRecursive(myMatrix7, [1]))

myMatrix8 = [
    [ [[[]]], [[[]]], [[[]]] ],
    [ [] ],
    [ [], [], [[[], []]], [] ],
    [ [] ],
    [ [], [], [] ],
    [[[[[[[[[[[[]]]]]]]]]]]],
    [[[[]]]], [[]], []
]

print(fillMyMatrixIntRecursive(myMatrix8, [1]))

# Exercise 3: Problem 2, Odd and Even Lists
def countEmptyLists(structure):
    if isinstance(structure, list):
        if len(structure) == 0:
            return 1
        return sum(countEmptyLists(sub) for sub in structure)
    return 0


def fillList(structure, counter, step):
    if isinstance(structure, list):
        if len(structure) == 0:
            start = counter[0]
            counter[0] += 2
            return [start, start + step]
        else:
            return [fillList(sub, counter, step) for sub in structure]
    return structure


def fillMyMatrixOddEven(myMatrix):
    total_empty = countEmptyLists(myMatrix)


    start = 1 if total_empty % 2 == 1 else 2

    return fillList(myMatrix, [start], 2)

myMatrix8 = [
    [ [[[]]], [[[]]], [[[]]] ],
    [ [] ],
    [ [], [], [[[], []]], [] ],
    [ [] ],
    [ [], [], [] ],
    [[[[[[[[[[[[]]]]]]]]]]]],
    [[[[]]]], [[]], []
]

result = fillMyMatrixOddEven(myMatrix8)
print(result)
