from Rectangle import Rectangle

class Surface: 

    def __init__(self, filename, x, y, h, w):
        ''' 
        Establishes self attributes in the Surface class 
        args: self: (Surface_object), filename: (String) filename of the an image, x: (int) x coordinate,
        y: (int) y coordinate, h: (int) height of the object, w: (int) width of the object
        returns: None
        '''
        self.image = filename
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.rect = Rectangle(x, y, h, w)



    def getRect(self):
        '''
        Returns the Surface object as a rectangle
        args: self: (Surface object)
        returns: (Surface object) surface object as a rectangle
        '''
        return self.rect 



