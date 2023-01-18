from lab3.adapter.child_creator import ChildCreator
from lab3.adapter.triceratops import Triceratops
from lab3.adapter.triceratops_to_mammal_adapter import TriceratopsToMammalAdapter
from lab3.composite.branch import Branch
from lab3.composite.leaf import Leaf
from lab3.decorator.gigantosaurus import Gigantosaurus
from lab3.decorator.extra_loud_gigantosaurus_decorator import ExtraLoudGigantosaurusDecorator
from lab3.decorator.loud_gigantosarus_decorator import LoudGigantosarusDecorator
from lab3.facade.dino_ecosystem_facade import DinoEcosystemFacade
from lab3.facade.soil import Soil
from lab3.proxy.secure_nest_proxy import SecureNestProxy
from lab3.proxy.real_nest import RealNest


class Program:
    def main(self):
        self.proxy_example()
        self.facade_example()

    def proxy_example(self):
        self.adapter_example()
        self.composite_example()

        secure_nest_proxy = SecureNestProxy(RealNest())
        secure_nest_proxy.access("Stegosaurus")
        secure_nest_proxy.access("TRex")

    def facade_example(self):
        self.meteor = False
        soil = Soil(10)
        dino_ecosystem_facade = DinoEcosystemFacade(soil)
        while not self.meteor:
            dino_ecosystem_facade.run_a_generation()
            self.decorator_example()
            print("Has a meteor hit? (Y/N)")
            response = input()
            if (response == "Y"):
                self.meteor = True
        self.decorator_example()
        print("A meteor has hit and destroyed the ecosystem!")

    def adapter_example(self):
        triceratops = Triceratops()
        child = ChildCreator().create_child(
            TriceratopsToMammalAdapter(triceratops))
        child.cry()

    def decorator_example(self):
        gigantosaurus = Gigantosaurus()
        loud_gigantosaurus = LoudGigantosarusDecorator(gigantosaurus)
        extra_loud_gigantosaurus = ExtraLoudGigantosaurusDecorator(
            loud_gigantosaurus)
        if self.meteor:
            print(extra_loud_gigantosaurus.roar())
        else:
            print(gigantosaurus.roar())

    def composite_example(self):
        plants = []
        branch = Branch([Leaf(), Leaf()])
        another_branch = Branch([Leaf(), Leaf(), Leaf()])
        plants.append(Branch([branch, another_branch]))
        plants.append(Leaf())

        for plant in plants:
            plant.eat()


if __name__ == '__main__':
    Program().main()
