class SingletonMeta(type):
    _instances = {}

    # runs whenever you try to instantiate a class
    def __call__(cls, *args, **kwargs):
        # If the class has no instance in _instances, create one
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        # Return the stored instance.
        return cls._instances[cls]

# Instead of using the default type metaclass, it uses SingletonMeta
# The metaclass controls how the class itself behaves when instantiated.
class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        define some business logic, which can be executed on the singleton instance        
        """
        print("Some business logic can be executed here.")