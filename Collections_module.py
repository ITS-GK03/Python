# COLLECTIONS MODULES:

import collections

# 1.COUNTER:

# mylist= ("K", "G", "A","D", "K", "K", "G", "A")
# res=collections.Counter(mylist)
# print(res)



# 2.ORDERDICT:

# mylist=collections.OrderedDict()

# mylist["k"]=3
# mylist["g"]=18
# mylist["gk"]=21

# for i, j in mylist.items():
#     print(i,j)

# mylist.pop("k")
# print("\n" )
# for i, j in mylist.items():
#     print(i,j)

# mylist["k"]=3
# print("\n" )
# for i, j in mylist.items():
#     print(i,j)



# 3.DEFAULT DICT:

# mylist=collections.defaultdict(int)

# list=[1,2,3,4,7,8,9,28, 7, 3, 28]

# for i in list:
#     mylist[i]+=1

# print(mylist)



# 4.CHAINMAP:

# mylist={
#     "name":"nayeem"
# }

# mylist1={
#     "son of ": "saleem"
# }

# res=collections.ChainMap(mylist, mylist1)
# print(res)



# 5. NAMEDTUPLE:

# mylist=collections.namedtuple("Friends",["name", "age", "sonof"])
# mylis=mylist("nayeem", 18, "saleem")

# print(mylis.sonof)



# 6. DEQUE:

# mylist=collections.deque(["bat", "ball", "stump", "gloves", "helmet"])
# print(mylist)

# mylist.append("gaude")
# print(mylist)

# mylist.appendleft("players")
# print(mylist)