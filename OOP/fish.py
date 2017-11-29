class Fish:

    __counter = 0


    __fin = 4

    #__slots__ = ['val']

    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"
        type(self).__counter += 1


    @staticmethod
    def FishInstances():
        return Fish.__counter

    def __repr__(self):
            return "Robot('" + self.__priv + "', " +  self.pub +  ")"


    def __del__(self):
            print ("fish has been destroyed")


    @classmethod
    def countfish(cls,num):
        cls.__counter = num



    # Fish.__fin is the class variable

    @property
    def finNo(self):
        return Fish.__fin

    @finNo.setter
    def finNo(self,value):
        Fish.__fin = value

    @finNo.deleter
    def finNo(self):
        print('Deleted')
        Fish.__fin = None




    def swim(self):
        print("swim")

    def swim_backwards(self):
        print("back")

    def skeleton(self):
        print("skl")

'''
    #self.__fin is the instance variable

    @property
    def finNo(self):
        return self.__fin

    @finNo.setter
    def finNo(self,value):
        self.__fin = value

    @finNo.deleter
    def finNo(self):
        print('Deleted')
        self.__fin = None
'''



class Shark(Fish):

    def __init__(self,teeth):
        super().__init__()
        self.teeth = teeth

    def swim_backwards(self):
        super().swim()
        print("The shark cannot swim backwards, but can sink backwards.")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")


class Clownfish(Fish):
    def swim(self):
        super().swim()
        print("The clownfish is swimming.")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")


print(Fish.FishInstances())
clownfish = Clownfish()

print(Fish.FishInstances())
f=Fish()
f2=Fish()
print(f.FishInstances())
print(f2.finNo)

f2.finNo = 6

print(f2.finNo)
print(f.finNo)

del f2.finNo
print('hi',f2.finNo)

clownfish.swim()
print(f.pub)
print(f._prot)
#print(f.__priv)
#f.swim()

print(f.FishInstances())

shark = Shark(72)
print(shark.teeth)
shark.swim_backwards()
shark.skeleton()


print(shark.FishInstances())


print(issubclass(Clownfish,Fish))
print(isinstance(f,Fish))

del shark
'''
for fish in (shark, clownfish, f):
    fish.swim()
    fish.swim_backwards()
    fish.skeleton()
'''
