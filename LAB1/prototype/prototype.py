from copy import deepcopy


class Prototype:
    def clone(self):
        return deepcopy(self)


if __name__ == "__main__":
    a = Prototype()
    a.x = 5
    b = a.clone()
    b.x = 4
    print(a.x, b.x)
