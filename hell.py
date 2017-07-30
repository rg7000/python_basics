def hello_world1():
    def hello_world2():
        print("Hello World 2")
    print("Hello World 1")
    hello_world2()

hello_world1()
hello_world2() #not accessible from outside
