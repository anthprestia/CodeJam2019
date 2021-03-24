
from dataclasses import dataclass

@dataclass
class people:
    x: int
    y: int
    direct: str
    best: list

def find_cart(list,max):
    final = [None,None]
    moving_x = {}
    moving_y = {}
    for person in list:
        best_x = person.x
        best_y = person.y
        if person.direct == 'N':
            if person.y != max:
                best_y = person.y + 1
            best_x = 0
        elif person.direct == 'E':
            if person.x != max:
                best_x = person.x + 1
            best_y = 0
        elif person.direct == 'W':
            best_x = 0
        elif person.direct == 'S':
            best_y = 0
        person.best = [best_x,best_y]

        if best_x not in moving_x:
            moving_x[best_x] = 1
        else:
            moving_x[best_x] += 1
        if best_y not in moving_y:
            moving_y[best_y] = 1
        else:
            moving_y[best_y] += 1

    return final

def main():
    t = int(input())
    for i in range(t):
        list = []
        temp1 = input()
        temp2 =temp1.split()
        P = int(temp2[0])
        Q = int(temp2[1])
        for j in range(P):
            temp3 = input()
            temp4 = temp3.split()
            x = int(temp4[0])
            y = int(temp4[1])
            direc = temp4[2]
            list.append(people(x,y,direc,None))
        result = find_cart(list,Q)
        print(result)


main()
