class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return "Rectangle(width=" + str(self.width)  + ", height=" + str(self.height) + ")"

  def set_width(self, width):
    self.width= width
    
  def set_height(self, height):
    self.height = height
     
  #Returns area (width * height)    
  def get_area(self): 
    return self.width * self.height
    
  #Returns perimeter (2 * width + 2 * height)
  def get_perimeter(self): 
    return 2 * self.width + 2 * self.height
  
  #Returns diagonal ((width ** 2 + height ** 2) ** .5)
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)
    
  # Returns a string that represents the shape using lines of "*". 
  def get_picture(self):  
    if self.width<50 and self.height<50:
      picture=''
      for h in range(0, self.height):
        for w in range(0, self.width):
          picture=picture+'*'
        picture=picture+'\n'
      return picture
    else:
      return "Too big for picture."

  #  Takes another shape (square or rectangle) as an argument. 
  def get_amount_inside(self, rectangle):
    horizontal = self.width // rectangle.width
    vertical = self.height // rectangle.height
    return horizontal * vertical



class Square (Rectangle):
  
  def __init__(self, length):
    self.width = length
    self.height = length 

  def __str__(self):
    return "Square(side=" + str(self.width) + ")"
    
  def set_side(self, side):
    self.width = side
    self.height = side
    