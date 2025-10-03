from singleton_class import Singleton

#!/usr/bin/env/python3

def main():
    s1 = Singleton()
    s2 = Singleton()
    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
        print(f"Different instances: {id(s1)} vs {id(s2)}")
        print("See other examples for usage.")
        
    s1.some_business_logic()    # call method on the singleton
    s2.some_business_logic()    # call method on the singleton

if __name__ == '__main__':
    main()
