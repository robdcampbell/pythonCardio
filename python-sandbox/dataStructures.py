# DATA STRUCTURES 

# DS are: lists, sets, touples, dictionaries


# ///////////////////////////////////////
#LISTS

# methods: 
# list()
# example.sort()
# example.append()
# len(listEx)
# max(listEx)
# min(listEx)
# sum(listEx)

      # example = list()
      # example.append('first')
      # example.append('second')
      # example.append('third')
      # example.insert(0,'zero')
      # print(example)


      # print(range(4))
      # friends = ['Joseph', "Glenn", "Sally"]
      # nums = [12,23,44,5,64564565,8,0,-23]
      #         # for i in range(len(friends)):
      #         #     friend = friends[i]
      #         #     print("Happy New Year: ", friend)
      # sortedNums = nums.sort()
      # print(sortedNums)
      # friends.sort()
      # print(friends)

      # import math

      # print(math.floor(232.443))


# ///////////////////////////////////////
# DICTIONARIES - Collection of data (similar to an Object in JavaScript)

#Dictionary methods
# list(dictEx)
# dictEx.keys()
# dictEx.values()
# dictEx.items() - will return a tuple




# Counting in dictionaries (making histograms)

# the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car

# text = input("Enter Words:")
# words = text.split()
# word_counts = dict()
# for word in words:
#   word_counts[word ] = word_counts.get(word, 0) +1
# print(word_counts)


        # fname = input("Enter File: ")
        # if len(fname) < 1: fname = 'clown.txt'

        # hand = open(fname)

        # di = dict()
        # for line in hand:
        #   line = line.rstrip()
        #   # print(line)
        #   wds = line.split()
        #   # print(wds)
        #   for w in wds:
            
        #     if w in di:
        #       di[w] = di[w]+1
        #     else:
        #       di[w] = 1
        #       # print("***NEW***")
        #     print(w, di[w])
        # print(di)

# 5:23:07 - TUPLES

#cop ok ok ok

                # fname = input("Enter File: ")
                # if len(fname) < 1: fname = 'clown.txt'

                # hand = open(fname)

                # di = dict()
                # for line in hand:
                # line = line.rstrip()
                # # print(line)
                # wds = line.split()
                # # print(wds)
                # for w in wds:
                
                # if w in di:
                # di[w] = di[w]+1
                # else:
                # di[w] = 1
                # # print("***NEW***")
                # print(w, di[w])
                # print(di)

# /////////////////////////////////////
# 5:23:07 - TUPLES.   Like lists, but they are immutable 

                # x = (1,2,3,4,5)
                # print(x)

# /////////////////////////////////////
# SORTING TUPLES.   Like lists, but they are immutable 

# Sort by values 
    # c = {"a":10, "b":1, "c":22}
    # tmp = list()
    # for k,v in c.items():
    #         tmp.append((v,k))

    # tmp = sorted(tmp,reverse=True)
    # print(tmp)
    # tmp = sorted(tmp)
    # print(tmp)


# 5:39:00
# >>>>>>> 804ce503d9c0124fe9f1b3d32a139718c412f746


# TOP 10 most common words example 2 ways:
fhand = open("clown.txt")
counts = dict()
for line in fhand:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word,0) + 1

lst = list()
for key, val in counts.items():
  newtup = (val,key)
  lst.append(newtup)

lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
  print(key, val)

# SHORTER / LAMBDA Version - LIST COMPREHENSION
c = {"a":10, "b":1, "c":22}
print(sorted([ (v,k) for k,v in c.items() ] ) )

# 1 - prints the list 
# 2 - sorts the list (in default, ascending order)
# 3a - implicitly creates a tuple of reversed key + value pairs
# 3b - loops through each "item" in the "c" dictionary


