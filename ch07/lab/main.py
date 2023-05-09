from Surface import Surface
from Rectangle import Rectangle

def rect():
    '''
    Tests to see if the rectangle class works properly 
    args: None 
    return: None
    ''' 
    r = Rectangle(10, 10, 10, 10) 
    assert ((r.x, r.y, r.h, r.w) == (10, 10, 10, 10,))
    r = Rectangle(-1, 1, 1, 1)
    assert ((r.x, r.y, r.h, r.w) == (1, 1, 1, 1))
    r = Rectangle(1, -5, 1, 1)
    assert ((r.x, r.y, r.h, r.w) == (1, 5, 1, 1))
    r = Rectangle(1, 1, 1, -1000)
    assert ((r.x, r.y, r.h, r.w) == (1, 1, 1, 1000))


def surf(): 
        '''
        Tests to see if the Surface class works properly 
        args: None 
        return: None 
        ''' 
        s = Surface("myimage.png", 10, 10, 10, 10)
        assert(s.rect.x, s.rect.y, s.rect.h, s.rect.w) == (10, 10, 10, 10) 
        srect = s.getRect()
        assert(srect.x, s.getRect().y, srect.h, srect.w) == (10, 10, 10, 10)
        assert s.image
        print("Test Complete!")


def main(): 
    rect()
    surf()


main() 
