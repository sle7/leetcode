class RotationSymmetry():

    def __init__(self):
        self.rotation = {'1': '1',
                         '0': '0',
                         '8': '8',
                         '6': '9',
                         '9': '6'}

        self.totalList = [[], ['0', '1', '8', '6', '9']]
        self.generated = 1

    def num_rotation(self, str):
        start = 0
        end = len(str)-1

        while start <= end:
            if str[start] != self.rotation.get(str[end]):
                return False
            start += 1
            end -= 1

        return True

    def gen_rotation_sym(self, num):
        start = ['0', '1', '8', '6', '9']
        totalList = start

        if num == 0:
            return False

        if num <= self.generated:
            for i in self.totalList[num]:
                if self.num_rotation(i):
                    print(i)
            return True
        else:
            for i in range(self.generated+1, num+1):
                self.totalList.append([])
                for j in self.totalList[self.generated]:
                    for k in start:
                        self.totalList[self.generated+1].append(j+k)
                self.generated += 1

        for i in self.totalList[num]:
            if self.num_rotation(i):
                print(i)

        return True


test = RotationSymmetry()

print(test.num_rotation('6'))
print(test.num_rotation('1010'))
print(test.num_rotation('1881'))
print(test.num_rotation('6969'))
test.gen_rotation_sym(4)
test.gen_rotation_sym(2)
