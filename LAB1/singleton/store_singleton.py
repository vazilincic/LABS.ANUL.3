class StoreSingleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance') or not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance


store = StoreSingleton()
store.name = 'Super Computers'
store.fiscal_code = id(store)
    

