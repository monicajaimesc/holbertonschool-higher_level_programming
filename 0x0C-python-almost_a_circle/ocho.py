
if args and len(args) > 0:
            for idx, arg in enumerate(args):
                if idx == 0:
                    super().__init__(arg)
                if idx == 1:
                    self.width = arg
                if idx == 2:
                    self.height = arg
                if idx == 3:
                     self.x = arg
                if idx == 4:
                    self.y = arg
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    super().__init__(value)
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value



attrs = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    super().__init__(args)
                if i == 1:
                    self.__setattr__(attrs[i], args)