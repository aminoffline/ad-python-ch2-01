class Student:
    count = 0

    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight
        Student.count += 1

    def __str__(self):
        return f'(age :{self.age},Height :{self.height},Weight:{self.weight})'

class ClassRoom:
    cc = 0
    def __int__(self):
        ClassRoom.cc =+ 1
    def buildclass(self,student_number,Lage,Lheight,Lweight):
        self.number = student_number
        #self.l_age , self.l_height , self.l_weight = Lage , Lheight ,Lweight
        self.l_age = Lage
        self.l_height = Lheight
        self.l_weight = Lweight

        classs =[Student(a, h, w) for a, h, w in zip(self.l_age, self.l_height, self.l_weight)]
        return classs

    def avg(self):
        sum_a , sum_h,sum_w = [] ,[], []
        avg = {}
        for i in self:
            sum_a.append(i.age)
            sum_h.append(i.height)
            sum_w.append((i.weight))
        avg['avg_a'] = sum(sum_a)/len(sum_a)
        avg['avg_h'] = sum(sum_h)/len(sum_h)
        avg['avg_w'] = sum(sum_w)/len(sum_w)
        return avg
        #return f'{sum_a}\n{sum_h}\n{sum_w}'

    def h_comper(self,other):
        if ClassRoom.avg(self)['avg_h'] > ClassRoom.avg(other)['avg_h']:
            print(self)
        elif ClassRoom.avg(self)['avg_h'] == ClassRoom.avg(other)['avg_h']:
            if ClassRoom.avg(self)['avg_w'] >= ClassRoom.avg(other)['avg_w']:
                print(f"{self}")
            else:
                print(f'{other}')
        else:
            print(f'{other}')


"""
n = int(input())

l_age = input().split(' ')
l_hieght = input().split(' ')
l_weight = input().split(' ')
l_age = [float(i) for i in l_age]
l_hieght = [float(i) for i in l_hieght]
l_weight = [float(i) for i in l_weight]
"""
l_age = [16,17, 15, 16, 17]
l_hieght = [180,175,172,170,165]
l_weight =  [67,72,59,62,55]

CA = ClassRoom()
CB = ClassRoom()
A = CA.buildclass(5, l_age,l_hieght,l_weight)
l_age = [15,16, 15, 16, 17]
l_hieght = [160,175,162,170,165]
l_weight =  [57,72,55,62,55]
B = CB.buildclass(5, l_age,l_hieght,l_weight)
#print(ClassRoom.avg(cr))
for i,j in ClassRoom.avg(A).items():
    print(j ,sep="\n")
for i,j in ClassRoom.avg(B).items():
    print(j ,sep="\n")

ClassRoom.h_comper(A,B)


#print( list(i.age for i in cr))


