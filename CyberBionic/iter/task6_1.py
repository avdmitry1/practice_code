class MyIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.lst):
            result = self.lst[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
        

iter_lst = [4, 4, 6, 7, 8, 9, 10,]

my_iterator = MyIterator(iter_lst)
for i in my_iterator:
    print(i)