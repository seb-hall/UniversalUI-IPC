import platform

# ipcNode represents an available communcation endpoint.
class ipcNode:

    # init function
    def __init__(self):

        # check system
        if (platform.system == 'Linux'):
            print("Running on Linux")
        elif (platform.system == 'Darwin'):
            print("Running on MacOS or iOS")
        elif (platform.system == 'Windows'):
            print("Running on Windows")
        else:
            print("Unknown System!")

    def assignToSystemServer(self):
        return
    
    def assignToSystemModule(self):
        return
    
    def assignToLocalServer(self):
        return
    
    def assignToLocalModule(self):
        return