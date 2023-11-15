class progressBar():
    def __init__(self, name):
        self.progress = 0
        self.completion = 0
        self.name = name

    def printProgress(self):
        print(f"{self.name}: [{'+'*self.progress}{'-'*(10-self.progress)}]")
        #print(self.name, ": ", end = "")
        '''print("[", end = "")
        print("+" * self.progress, end="")
        print("-" * (10 - self.progress), end ="")
        print("]", end = "")
        print(" ", self.completion, "%")'''

    def setProgress(self, value):
        self.progress = value

    def calcCompletion(self):
        self.completion = self.progress / 8

