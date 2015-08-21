__author__ = 'Girish'




for j in range(int(input())):
    max_shy , peoples = input().split()
    max_shy = int(max_shy)
    pastvalue = int(peoples[0])

    su=0
    for i,val in enumerate(peoples[1:]):
        if pastvalue < i+1:
            su += i+1-pastvalue
            pastvalue =i+1
        pastvalue+=int(val)

    print("Case #{}: {}".format(j+1,su))











