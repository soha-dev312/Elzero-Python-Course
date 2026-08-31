class walker:
    def move(self):
        print("Walking on the ground....")
class Swimmer:
    def move(self):
        print("Swimming in the water....")
class Amphibian(walker,Swimmer):
    pass
frog = Amphibian()
frog.move()
print(Amphibian.mro())