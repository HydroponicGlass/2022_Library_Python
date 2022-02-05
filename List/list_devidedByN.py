def ChunkList(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

list = []
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)

list = ChunkList(list, 2)
print(list) # output : [[1, 2], [3, 4], [5]]