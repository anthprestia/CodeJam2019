"""
file: ForegoneSolution.py

"""
def not_math(number):
    first = 0
    second = 0
    positives = True
    for digit in range(len(number)):
        num_place = 10**((len(number)-digit)-1)
        if number[digit] == '9':
            positives = False
            first = first + num_place * 1
            second = second + num_place * 8
        elif number[digit] == '8':
            positives = False
            first = first + num_place*1
            second = second + num_place*7
        elif number[digit] == '7':
            positives = False
            first = first + num_place*1
            second = second + num_place*6
        elif number[digit] == '6':
            positives = False
            first = first + num_place*1
            second = second + num_place*5
        elif number[digit] == '5':
            positives = False
            first = first + num_place*2
            second = second + num_place*3
        elif number[digit] == '4':
            positives = False
            first = first + num_place*2
            second = second + num_place*2
        elif number[digit] == '3':
            positives = False
            first = first + num_place*1
            second = second + num_place*2
        elif number[digit] == '2':
            positives = False
            first = first + num_place*1
            second = second + num_place*1
        elif positives == True:
            positives = False
            if number[digit] == '1' or number[digit] == '0':
                temp2 = int(number[digit]+number[digit]) // 2
                if temp2 == 4:
                    first += (num_place // 10) * temp2-1
                    second += (num_place // 10) * (int(number[digit]) + temp2 +1)
                else:
                    first += (num_place // 10) * temp2
                    second += (num_place // 10) * (int(number[digit]) + temp2 - 1)
            else:
                temp = int(number[digit]) // 2
                first += num_place*temp
                second += num_place*(int(number[digit])-temp)
        else:
            first = first + num_place*int(number[digit])
    return first,second

def main():
    t = int(input())
    for i in range(t):
        n = input()
        one,two = not_math(n)
        print("Case #",i+1,": ",one,' ',two,sep='')
main()