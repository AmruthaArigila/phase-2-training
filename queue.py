# queue implementation #
def enqueue(q,ele):
    q.append(ele)
    print(ele,"inserted to q")
def dequeue(q):
    if len(q)==0:
        print("q is empty")
        return
    print(q[0],"delete")
    q.pop(0)
q=[]
enqueue(q,10)
enqueue(q,20)
enqueue(q,30)
enqueue(q,40)
enqueue(q,50)

dequeue(q)
dequeue(q)
dequeue(q)
dequeue(q)
dequeue(q)
