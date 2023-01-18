# Design Patterns

In this project I implemented 5 structural design patterns

- Adapter - Allows objects with incompatible interfaces to collaborate.
- Composite - Lets you compose objects into tree structures and then work with these structures as if they were individual objects.
- Decorator - ets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.
- Facade - Provides a simplified interface to a library, a framework, or any other complex set of classes.
- Proxy - Lets you provide a substitute or placeholder for another object. 

## Adapter
The adapter pattern is useful when you want to use a class that does not fit the design of your existing solution. This is often the case when using legacy or external code. The adapter pattern allows you to define a wrapper which executes the desired behaviour, but exposes it through a method which your solution expects.

So, today we've been transported to a post-meteor world...

And in this world, in the age of mammals, we have a child_creator that expects things to work in a certain way:

The give_birth method produces an child, which has a single method, cry
```
class Child:
    def cry(self):
        pass
```
However, though the world has moved on, we have a few legacy reptile hanging around, that are just trying to get along in an unfamiliar place... Unfortunately reptile works somewhat differently to the majority of mammals, possessing a lay_egg method:
```
class TriceratopsEgg():
    def hatch(self):
        return TriceratopsChild()
```
We need a way that our child_creator can work with the Reptile to produce a child.

If we define a ReptileToMammalAdapter, which implements the mammal class, and wraps an internal Reptile:
```
class TriceratopsToMammalAdapter(Mammal):
    def __init__(self, triceratops):
        self.triceratops = triceratops

    def give_birth(self):
        egg = self.triceratops.lay_egg()
        child = egg.hatch()

        return child
```

Then the give_birth method can call the LayEgg method of the internal Reptile, and then Hatch that egg to produce a child
```
triceratops = Triceratops()
child = child_creator().create_child(TriceratopsToMammalAdapter(triceratops))
child.cry()
```
## Composite

We use this design pattern to create a plant. A plant can have branches, branches can have leaves

Component part (Plant):
```
class Plant:
    def eat(self):
        pass

```
Component part (Branch):
```
class Branch (Plant):
    def __init__(self, children):
        self.children = children

    def eat(self):
        for child in self.children:
            child.eat()
```
Leaf class:
```
class Leaf(Plant):
    def __init__(self):
        self.IsEaten = False

    def eat(self):
        self.IsEaten = True
        print("Leaf eaten!")
```
Implementation:
```
plants = []
branch = Branch([Leaf(), Leaf()])
another_branch = Branch([Leaf(), Leaf(), Leaf()])
plants.append(Branch([branch, another_branch]))
plants.append(Leaf())

for plant in plants:
    plant.eat()
```
## Decorator
To use the decorator pattern, you wrap an object in another object in order to extend behaviour. The objects all implement the same interface, so the decorators can stack on top of one another, extendng the behaviour further.

we implement that AbstractGigantosaurus interface with a class:
```
class Gigantosaurus(AbstractGigantosaurus):
    def roar(self):
        return "ROAR"
```
Wrap the initial gigantosaurus object in a Decorator:
```
class SilentGigantosaurusDecorator (AbstractGigantosaurus):
    def __init__(self, gigantosaurus):
        self.gigantosaurus = gigantosaurus

    def roar(self):
        return ""
```
We have a second Decorator which extends the behaviour further:
```
class LoudGigantosarusDecorator (AbstractGigantosaurus):
    def __init__(self, gigantosaurus):
        self.gigantosaurus = gigantosaurus

    def roar(self):
        return f'{self.gigantosaurus.roar()} loudly'
```
We build up our wrapped object as follows:
```
gigantosaurus = Gigantosaurus()
print(gigantosaurus.roar())

loud_gigantosaurus = LoudGigantosarusDecorator(gigantosaurus)
extra_loud_gigantosaurus = ExtraLoudGigantosaurusDecorator(loud_gigantosaurus)
print(extra_loud_gigantosaurus.roar())
```
## Facade
The facade pattern is a useful for providing a simple interface into a complex system. It doesn't provide access to all parts of the system, it provides a limited set of functionality and hides any underlying complexity.

We have a complex ecosystem, everything starts with the nutrients in the soil:
```
class Soil:
    def __init__(self, nutrient_count):
        self.nutrient_count = nutrient_count
        print(f"The soil has {self.nutrient_count} nutrient(s)")

    def add_nutrient(self, edible):
        print("The soil gains nutrients")
        edible.eat()
        self.nutrient_count += 1
        print(f"Nutrient count: {self.nutrient_count}")

    def use_nutrient(self):
        if (self.nutrient_count <= 0):
            print("No nutrients left!")
        self.nutrient_count -= 1
        print(f"Nutrient count: {self.nutrient_count}")
```
We then have Plants, which use the nutrients in order to grow:
```
class Plant (Edible):
    def __init__(self, soil):
        print("A new plant grows")
        soil.use_nutrient()
        self.is_eaten = False
```
Plants are then eaten by Herbivores
```
class Herbivore (Edible):
    def __init__(self, plant):
        print("The herbivore eats a plant.")
        plant.eat()
        self.is_eaten = False
```
And in turn these Herbivores are eaten by Carnivores:
```
class Carnivore (Edible):
    def __init__(self, herbivore):
        print("The carnivore eats the herbivore")
        herbivore.eat()
        self.is_eaten = False

    def die(self, soil):
        print("The carnivore dies")
        soil.add_nutrient(self)
```
Eventually the Carnivores die, and return the nutrients to the soil.

```
class DinoEcosystemFacade:
    def __init__(self, soil):
        self.soil = soil

    def run_a_generation(self):
        plant = Plant(self.soil)
        herbivore = Herbivore(plant)
        carnivore = Carnivore(herbivore)
        carnivore.die(self.soil)
```
Implementation:
```
dino_ecosystem_facade = DinoEcosystemFacade(Soil(1))
dino_ecosystem_facade.run_a_generation()
```
## Proxy
The proxy pattern is used to provide access to an object. It is often used to enable this access over some distance - this could be providing remote access, or adding an extra level of protection around the object. The crucial thing is that the proxy pattern offers a way to indirectly provide (and control) access.

The proxy pattern can be used to restrict access to an object, to provide a simpler or lightweight interface, or to allow the client to communicate with a remote object via a local representation.

Nest is implemented by a RealNest:
```
class RealNest (Nest):
    def access(self, name):
        print(f"{name} has access to the nest")
```
Now, we don't want just anyone to be able to access our Nest. We need to be able to restrict access to only those that aren't going to cause harm. To do this, we can implement a SecureNestProxy:
```
class SecureNestProxy (Nest):
    def __init__(self, nest):
        self.nest = nest

    def access(self, name):
        if (name == "TRex" or name == "Gigantosaurus"):
            print(f"{name} is not allowed to access the nest.")
        else:
            self.nest.access(name)
```
This Proxy will reject access for TRex and Gigantosaurus

Implementation:
```
secure_nest_proxy = SecureNestProxy(RealNest())
secure_nest_proxy.access("Stegosaurus")
secure_nest_proxy.access("TRex")
```
## Conclusion
In this project I implemented 5 Structural design patterns