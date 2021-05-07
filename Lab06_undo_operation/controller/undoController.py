class UndoController:
    def __init__(self):
        self._history = []
        self._index = 0
        self._duringUndo = False

    def recordOperation(self, operation):
        '''
        Record an operation in the history undo/redo
        Parameters:
            - operation - the operation that was carried out
        Return:
            - None
        '''
        if self._duringUndo is True:
            return
        self._history.append(operation)
        self._index += 1

    def undo(self):
        if self._index == 0:
            raise ValueError('no more undos!')
        self._duringUndo = True
        self._index -= 1
        self._history[self._index].undo()
        self._duringUndo = False

    def redo(self):
        if self._index == len(self._history):
            raise ValueError('no more redos!')
        self._duringUndo = True
        self._history[self._index].redo()
        self._index +=1
        self._duringUndo = False

class FunctionCall:
    def __init__(self, function, *parameters):
        self._function = function
        self._params = parameters

    def call(self):
        self._function(*self._params)

    def __call__(self):
        self.call()

class Operation:
    def __init__(self, undoFunction, redoFunction):
        self._undo = undoFunction
        self._redo = redoFunction

    def undo(self):
        self._undo()

    def redo(self):
        self._redo()

class CascadedOperation:
    def __init__(self, *operatios):
        self._oper = operatios

    def undo(self):
        for o in self._oper:
            o.undo()
    
    def redo(self):
        for o in self._oper:
            o.redo()
