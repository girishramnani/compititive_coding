__author__ = 'Girish'

def finder(let,li):
    if let in li:
        index = li.index(let)
    else:
        index=-1
    return index

def recoverSecret(triplets):
    li =[]
    li.extend(triplets.pop(0))
    while triplets:
        t = triplets.pop(0)
        left =[]
        count=0
        for i,let in enumerate(t):
            index = finder(let,li)
            if index != -1:
                if i==0:
                    for t2,w in enumerate([1,2]):
                        in2 = finder(t[w],li[index+1:])
                        if in2 !=-1:
                            if t2+index+1 == 2:
                                pass
                            else:
                                li.insert(in2+t2+1,t[w])
                        else:
                            li.insert(index+1,t[w])
            else:
                count+=1
        if count==3:
            triplets.append(t)



'w h a t i s u p'
secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

assert(recoverSecret(triplets), secret)