class GameData:

   props = {}

   def __init__(self):
       pass

   def set(self, name, obj):
       self.props[name] = obj

   def get(self, name):
       return self.props.get(name)
