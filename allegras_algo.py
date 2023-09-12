#part A
#number of queries allegra's algorithm makes on a set(list) of booleans.
#return the index of the first False found in the "x" list of booleans
def query_complexity(x):
    n_query = 0
    if False not in x:
        n_query = len(x)
    else:
        n_query = x.index(False) + 1
    return n_query

list_of_booleans = [True, True, True, True, True, True, True, True]
print("query complexity: " + str(query_complexity(list_of_booleans)))

#part B
#total_qc: total number of queries for ALL possible sets(lists) of booleans
#using math is harder but will not take as much memory n time as making all the possible sets of "n" booleans n then using the query_complexity(x) function on ALL of the possible sets, then take each query value n add them all up
#using math also allows us to not require part A to get part B n part C to work
#there is a pattern in which sets of booleans which require "n" n "n-1" (for input sizes equal to or bigger than 2) will always happen twice (2^1) - therefore we add both of them as (n*2) + ((n-1) *2)
#afterwards from cases that require "n-2" queries to 1 query goes as follows: ((n-2) * (2^2)) + ((n-3) * (2^3)) + ... + ((1) * (2^n-1))
#adding both of these we get the below algorithm
#arbitrary size of input = 7
n = 5
def total_qc(n):
    sum = 0
    sum = sum + (n * 2) + ((n-1) * 2)
    for i in range(2, n):
        sum = sum + ((n-i) * (2**i))
    return sum
print(f"total queries of all possible sets of {n} booleans: " + str(total_qc(n)))

#part C
#average_qc(n) = total_qc(n) / 2**n - total number of queries over all the possible sets(lists) of booleans
#average number of queries over the number of possible inputs from the discription of the 
#number of possible inputs = 2*n cos there are 2 options(true/false) n the input size is "n" - product rule 
#for example input size ("n") is 3: a, b, c - a:t/f, b:t/f, c:t/f  -> 2*3
def average_qc(n):
    return total_qc(n) / (2**n)

print(f"average-case complexity for allegra's algorithm for input size {n}: " + str(average_qc(n)))
