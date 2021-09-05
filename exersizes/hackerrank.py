'''
if __name__ == '__main__':
    n = int(input())
    [print(i, end="") for i in range(1, n + 1)]

n = int(input())
arr = map(int, input().split())
print(sorted(list(set(arr)))[-2])

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        print(name, score)
'''
studentList= []

for i in range(int(input())):
    name = input()
    score = float(input())
    studentList.append([name, score])

# for each nest in studentList
# sort via the score in ascending
# with {} within sorted[] it creates a "set"
# output is [37.2, 37.21, 39, 41] - sets remove additonal same numbers
scoreSort = sorted({s[1] for s in studentList})

# for each nest in studentList (s)
# return a sorted list (sorted by their names (s[0])) of students whos score (s[1]) is equal to s[1] in scoreSort
# nameSort = ["Berry", "Harry"]
nameSort = sorted(s[0] for s in studentList if s[1] == scoreSort[1])

#.join(nameSort) takes each element in the nameSort list
# so ["Berry", "Harry"]
# "\n" seperates using a newline BETWEEN each element
# output is "Berry\nHarry"
print('\n'.join(nameSort))