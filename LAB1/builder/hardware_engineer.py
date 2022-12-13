from lab2.builder.computer_builder import ComputerBuilder


class HardwareEngineer:
    def __init__(self):
        self.builder = ComputerBuilder()

    def build_computer(self, ram, storage, gpu):
        self.builder.configure_ram(ram),
        self.builder.configure_storage(storage),
        self.builder.configure_gpu(gpu)

        return self.builder.computer


if __name__ == "__main__":
    consultant = HardwareEngineer()
    computer = consultant.build_computer(
        ram=8, storage='fast',  gpu='Nvidia new')
    print(computer)
