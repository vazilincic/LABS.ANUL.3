from lab2.builder.hardware_engineer import HardwareEngineer
from lab2.singleton.store_singleton import StoreSingleton
from lab2.factory.storage_factory import StorageFactory


def main():
    store = StoreSingleton()
    consultant = HardwareEngineer()
    computer1 = consultant.build_computer(
        ram=8, storage='big',  gpu='Amd old')
    computer2 = computer1.clone()
    computer2.storage = StorageFactory().get_storage('fast')

    print(f'Welcome to: {store.name}\n')
    print('Order Details:')
    print(f'Computer1 \n{computer1} \n')
    print(f'Computer2 \n{computer2} \n')
    print(f'Transfer money to: {store.fiscal_code}')


if __name__ == "__main__":
    main()
