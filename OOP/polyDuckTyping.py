class pycharm:
    def execute(self):
        print("Compile")
        print("Running")

class myEditor:
    def execute(self):
        print("Spell Check")
        print("Auto Correction")
        print("Compile")
        print("Running")

class laptop: #in java it called Interface where from two diffrent classes on class can handel it with the help of execute function.
    def code(self,ide):
        ide.execute()

ide = myEditor() #it creating object to parse the variable in code class
ide1 = pycharm()
a = laptop()
b = laptop()
a.code(ide) #ide variable are pass in code.
b.code(ide1)

#this whole process called ducktyping