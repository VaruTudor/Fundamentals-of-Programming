# The sequence a = 𝑎1, …, 𝑎𝑛 with distinct integer numbers is given. Determine all subsets of
# elements having the sum divisible by a given n


### Recursive Version ###

def subsets(numbers, target):
    res = []
    backtrack(res, [], numbers, 0, target)
    res.remove([])
    return res

def backtrack(res, temp, numbers, start, target):
    '''
    generates subsets and checks posible solutions 
    target - (int) the number which must divide the sum
    res - (list) the list of solutions
    numbers - (list) the list of numbers
    start - (int) starting position for searching for next candidates
    temp - (list) the current subset
    '''
    if sum(temp) % target == 0:
        res.append(temp[:])
    for i in range(start, len(numbers)):
        temp.append(numbers[i])
        backtrack(res, temp, numbers, i + 1, target)
        temp.pop() # Backtrack

print(subsets([1, 2, 5, 6, 8],3))

### Iterative Version ###

def iSubsets(numbers, target):
    res = []
    numbers.sort()
    iBacktracking(res, [], numbers, 0, target)
    return res

def last_el(seq):
    if seq != []:
        return seq[len(seq)-1]

def iBacktracking(res, temp, numbers, start, target):
    pos = 0 #position in numbers
    while temp != numbers[-1:]:
        if last_el(temp) != last_el(numbers):
            temp.append(numbers[pos])
            if sum(temp) % target == 0:
                res.append(temp[:])
            pos += 1
        else:
            temp.pop()
            pos = numbers.index(last_el(temp)) + 1
            temp[len(temp)-1] = (numbers[pos])
            if sum(temp) % target == 0:
                res.append(temp[:])
            pos += 1

print(iSubsets([1, 2, 5, 6, 8],4))

### THE END ###
  ### :) ###