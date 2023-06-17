
# interface for codable properties and classes
class ipcCodable:

    # return a string of name
    def encodeName():
        return ""
    
    # return bytes of parameters
    def encodeParameters():
        return
    
    # update parameters from recieved bytes
    def decodeParameters(parameters):
        return