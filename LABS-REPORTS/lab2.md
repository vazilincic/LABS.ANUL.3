# Design Patterns

In this project I implemented 5 creational design patterns

- Abstract Factory - Creates families of related dependent objects
- Factory - Creates objects of several related classes without specifying the exact object to be created
- Builder -  Constructs objects using step-by-step approach
- Singleton - A class should have only one instance at a time
- Prototype - Makes copies of existing objects without making the code dependent on their classes.

## Abstract Factory
The Abstract Factory pattern is also called a factory of factories.

With the Factory pattern, previously seen, you produce instances of a class via a factory method. With the Abstract Factory pattern, you provide a way for anyone to provide their own factory.

My example example is based upon two factories that manufacture gpus. This is the NvidiaFactory class and the AmdFactory class. 

```
class AmdFactory:
    def get_gpu(self, gpu_type):
        if gpu_type == "old":
            return AmdGPUOld()
        if gpu_type == "new":
            return AmdGPUNew()
```
```
class NvidiaFactory:
    def get_gpu(self, gpu_type):
        if gpu_type == "old":
            return NvidiaGPUOld()
        if gpu_type == "new":
            return NvidiaGPUNew()
```

In the GPUShop class is implemented the Abstract Factory.

```
class GPUShop:
    def __init__(self, gpu_factory):
        self._gpu_factory = gpu_factory

    def buy_gpu(self, gpu_type):
        gpu = self._gpu_factory.get_gpu(gpu_type)
        return gpu
```
Example:
```
nvidia_factory = NvidiaFactory()
gpu_shop = GPUShop(nvidia_factory)
gpu_shop.buy_gpu('new')
```

## Factory
The Factory pattern is a design pattern that allows you to use a function or method (known as the factory method) to handle the creation of objects without specifying their concrete classes.

In my example below, we can see that the method get_storage is our factory method. Therefore we only need to interact with the factory method for the creation of our classes.

```
class StorageFactory:
    def get_storage(self, storage_type):
        if storage_type == "fast":
            return SSD()
        if storage_type == "big":
            return HDD()
```
Example:
```
factory = StorageFactory()
a = factory.get_storage("fast")
b = factory.get_storage("big")
```
## Builder
The main advantages of the Builder pattern are that it provides a clear separation between the construction and representation of an object, and in turn, provides better control over the construction process.

The pattern consists of two main participants: the builder and the director. The builder is responsible for creating the various parts of the complex object. In my case, the ComputerBuilder class can build three parts, ram, storage, gpu. The storage part is generated from the StorageFactory class, and the gpu from the GPUShop class. 
```
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def configure_ram(self, amount):
        self.computer.ram = amount
        self.computer.ram_price = 10 * amount

    def configure_storage(self, type):
        factory = StorageFactory()
        self.computer.storage = factory.get_storage(type)

    def configure_gpu(self, gpu_model):
        if gpu_model.startswith('Nvidia'):
            factory = NvidiaFactory()

        else:
            factory = AmdFactory()

        gpu_shop = GPUShop(factory)
        self.computer.gpu = gpu_shop.buy_gpu(gpu_model.split()[1])
```

The director controls the building process using a builder instance.
```
class HardwareEngineer:
    def __init__(self):
        self.builder = ComputerBuilder()

    def build_computer(self, ram, storage, gpu):
        self.builder.configure_ram(ram),
        self.builder.configure_storage(storage),
        self.builder.configure_gpu(gpu)

        return self.builder.computer
```
Example:
```
consultant = HardwareEngineer()
computer = consultant.build_computer(ram=8, storage='fast',  gpu='Nvidia new')
```
## Singleton

Singleton ensure a class has only one instance, and provide a global point of access to it.
```
class StoreSingleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance


store = StoreSingleton()
store.name = 'Super Computers'
store.fiscal_code = id(store)
```
A new instanciation of the StoreSingleton will call the same instance as in the example above.

## Prototype
Prototype specifies the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

```
class Prototype:
    def clone(self):
        return deepcopy(self)
```
Example:
```
    a = Prototype()
    a.x = 5
    b = a.clone()
    print(b.x)
```
## Results, Conclusions
An example of how all five patterns were used can be seen in [main.py](../lab2/main.py) (The factory and abstract factory patterns were used inside the builder)