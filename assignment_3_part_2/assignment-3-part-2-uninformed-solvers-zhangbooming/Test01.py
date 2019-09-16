from queue import Queue
tup3 = "a", "b", "c", "d"
print(type(tup3))
print(tup3)
print(tup3[2])
tup4 = (tup3, (1, 2, 3, 4))
print(tup4[1][1])

print(('1', '1', '1') == (1, 1, 1))
print("----------------------")

stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print("stack", stack)
print("stack[0]::", stack[0])
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("stack[0]:::", stack[0])
print(stack.__sizeof__() == 0)
print("stack.__sizeof__()::", stack.__len__())

dict = dict()
dict[1] = 3
dict[2] = 4
dict[3] = 5
print(dict[3])
print(dict.__contains__(4))

q = Queue()
for i in range(5):
    q.put(i)
print(q.get())
print(q.get())
print(q.get())
print(q.queue)
print(q.empty())

list = [1,2,3,4]
print("list.size", list.__len__())
print(list[3])

print("*****************")
list = [3, 2, 1, 0, -9, 100]
list.sort()
tup5 = tuple(list)
print("tup5::", tup5)
print("list.sort:::", list)
print("null:::", tuple([]))


str = "tile5667"
print("strr::", str[-1])
print("type::", type(int(str[-1])))