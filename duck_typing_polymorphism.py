class pycharm:
    def execute(self):
        print("compiling")
        print("running")

class my_editor:
    def execute(self):
        print("spell check")
        print("compiling")
        print("running")

class laptop:
    def code(self,ide):
        ide.execute()
        
#ide = pycharm()
ide = my_editor()
lap = laptop()
lap.code(ide)
