# Stack Implementation
class empty(Exception):
    def __init__(self,e):
        pass
class ArrayStack:
    def __init__(self):
        self.items=[]
    def IsEmpty(self):
        self.items==[]
    def Push(self,data):
        self.items.append(data)
    def pop(self):
        try :
            self.IsEmpty()
            raise empty('Stack Is Empty')
            return self.items.pop()
        except empty as e:
            print(e)
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
while(True):
    print('1. Create_Stack \n 2. Push \n 3. Pop \n 4. Size \n 5.Peek \n 6.Quit')
    s=int(input('Enter Choice '))
    if s==1:
        S=ArrayStack()
    elif s==2:
        S.Push(int(input()))
    elif s==3:
        print(S.Pop())
    elif s==4:
        print(S.size())
    elif s==5:
        print(S.peek())
    elif s==6:
        break
    else:
        print('Try Again')
