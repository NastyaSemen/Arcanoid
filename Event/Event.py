class Event:

    name = ''
    obj = None

    def __init__(self, name, obj):
        self.name = name
        self.obj = obj

    def get_name(self):
        return self.name

    def get_obj(self):
        return self.obj
