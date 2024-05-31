class Sun:
    _instance = None

    @classmethod
    def inst(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


p = Sun.inst()
f = Sun.inst()

print(p is f)
