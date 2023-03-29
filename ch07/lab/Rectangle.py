

class Rectangle: 

    def __init__(self, x, y , h, w):
        '''
        Establishes self attributes in the Rectangle class 
        args: self: (Rectangle object), x: (int) x coordinate, y: (int) y coordinate, 
        h: (int) height of the object, w: (int) width of the object
        returns: None
        ''' 
        self.x = abs(x)
        self.y = abs(y)
        self.h = abs(h)
        self.w = abs(w)


    def __str__(self):
        '''
        Returns a string with the x,y, height and width of the rectangle
        args: (Rectangle object) 
        return: (str) The x, y coordinates and the height and width of the object
        '''
        return "(x:" + str(self.x) + ", y:" + str(self.y) + ") width:" + str(self.w) + "height:" + str(self.h)
    
