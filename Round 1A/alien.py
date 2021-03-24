


def suffix(list):
    pass


def main():
    t = int(input())
    for i in range(t):
        w = []
        n = int(input())
        temp = n
        while n > 0:
            w.append(input())
            n-=1
        possible = suffix(w)
        #print("Case #",i+1,": ",pair_find(possible,temp), sep = '')
main()