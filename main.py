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
    def __int__(self):
        pass
    def BuildClass(self, student_number ,Lage, Lheight, Lweight ):
        self.number = student_number
        self.l_age , self.l_height , self.l_weight= Lage , Lheight ,Lweight
        classs = [Student(a, h, w) for a, h, w in zip(l_age, l_hieght, l_weight)]
        return classs

    def avg(self):
        pass

n = int(input())
"""
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
A = ClassRoom()
cr = A.BuildClass(n, l_age,l_hieght,l_hieght)
print( list(i.age for i in cr))


