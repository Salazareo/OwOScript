import json


class ScopedMap():

    def __init__(self):
        self.scopes = [{}]

    def addScope(self, functionInfo=None):
        self.scopes.append({"-FUNCTION-": functionInfo})

    def currentlyInFunction(self):
        for i in range(len(self.scopes)-1, -1, -1):
            if self.scopes[i]['-FUNCTION-'] != None:
                return True
        return False

    def getFunctionInfo(self):
        for i in range(len(self.scopes)-1, -1, -1):
            if self.scopes[i]['-FUNCTION-'] != None:
                return self.scopes[i]['-FUNCTION-']
        return False

    def popScope(self):
        self.scopes.pop()

    def __contains__(self, key):
        for i in range(len(self.scopes)-1, -1, -1):
            if key in self.scopes[i]:
                return True
        return False

    def inCurrentScope(self, key):
        return key in self.scopes[-1]

    def __getitem__(self, key):
        for i in range(len(self.scopes)-1, -1, -1):
            if key in self.scopes[i]:
                return self.scopes[i][key]
        return None

    def __setitem__(self, key, val):
        for i in range(len(self.scopes)-1, -1, -1):
            if key in self.scopes[i]:
                self.scopes[i][key] = val
        self.scopes[-1][key] = val

    def getScopeIndex(self, key):
        for i in range(len(self.scopes)-1, -1, -1):
            if key in self.scopes[i]:
                return i
        return None

    def inScopeIndex(self, index, key):
        return key in self.scopes[index]

    def forceNew(self, key, val):
        self.scopes[-1][key] = val

    def __delitem__(self, key):
        for i in range(len(self.scopes)-1, -1, -1):
            if key in self.scopes[i]:
                del self.scopes[i][key]

    def __str__(self) -> str:
        return str(self.scopes)

    def toJSON(self):
        return json.dumps(self.scopes, indent=4)
