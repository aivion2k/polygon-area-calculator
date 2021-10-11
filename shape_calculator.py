class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def set_width(self,width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.height*self.width

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            picture = ''
        for i in range(self.height):
            for j in range(self.width):
                picture += '*'
            picture += '\n'
        return picture
    
    def get_amount_inside(self,rect):
        x = self.width
        y = self.height
        l=0
        p=0
        #print(rect.width, rect.height)
        #print(self)
        if self.width < rect.width or self.height < rect.height:
          return 0
        else:         
            while x-rect.width >= 0:
                if x < 0:
                  break
                l+=1
                x-=rect.width
                print(x)

          
            while y-rect.height>=0:
                if y < 0:
                  break
                p+=1            
                y-=rect.height
                print(y) 
  
            return l*p
          
        


       


    def __str__(self):
        return 'Rectangle(width={}, height={})'.format(self.width,self.height)


class Square(Rectangle):
    def __init__(self,side):
        self.height = side
        self.width = side
        self.side = side

    def set_width(self,width):
        self.side = width

    def set_height(self,height):
        self.side = height
    
    def get_amount_inside(self, rect):
        return super().get_amount_inside(rect)

    def get_area(self):
        return super().get_area()
    
    def get_perimeter(self):
        return super().get_perimeter()

    def get_diagonal(self):
        return super().get_diagonal()

    def get_picture(self):
        return super().get_picture()

    def set_side(self,side):
        self.side = side
        self.width = side
        self.height = side
    
    def __str__(self):
        return 'Square(side={})'.format(self.side)
