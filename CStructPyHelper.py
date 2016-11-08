class CStructPyHelper(object):
    def __init__(self,data):
        self._raw_data = data
    def name(self):
        return self._raw_data.strip().split('\n')[0]