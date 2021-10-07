class human:
    def __init__(self,name):
        self.name=name
        self.head=self.Head()
    def display(self):
        self.head.info()
        self.head.brain.think()
    class Head:
        def __init__(self):
            self.brain=self.Brain()
        def info(self):
            print("Loki is good at Talking")
        class Brain:
            def think(self):
                print("I am grate at thinking but doing nothing")

h=human("pratik")
h.display()