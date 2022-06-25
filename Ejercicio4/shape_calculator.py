from calendar import c
from tkinter.simpledialog import SimpleDialog
from turtle import width


class rectangle:

    def __init__(self, width, height):
        self.height = height
        self.width = width

    # Ingresan los valores que permiten calcular el área del rectangulo, width el ancho y height el alto
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self, area):
        self.area = self.width * self.height
        return self.area
    
    #Calculo con los mismos datos el perimetro, diagonal y un picture que me muestre "*" según el ancho y alto
    def get_perimeter(self, perimeter):
        self.perimeter = 2 * width + 2 * height
        return self.perimeter
    
    def et_diagonal(self, diagonal):
        self.diagonal = (width ** 2 + height ** 2) ** .5
        return self.diagonal

    def get_picture(self, picture):
        if self.widht > 50 or self.height > 50:
            print("Too big for picture.")
        else:
            for x in range(self.width):
               for i in range(self.height):
                    print("*", end = "") 
                    return picture

    #Me indica cauntas veces entra otra forma dentro de la forma ingresada
    def get_amount_inside(self, ):
        c

    #Si una de las instancias es un str debe verse así 
    def __str__(self) -> str:
        return f"Rectangle(widht={self.width}, height={self.height})"

#El square class es una subclase del rectangle class

class square(rectangle):
    def __init__(self, side):
        super().__init__(width, height)
        self.side = side 
        self.height = side
        self.width = side

    def set_side(self, side):
        self.height = side
        self.width = side
        return self.height or self.width
        
    def __str__(self) -> str:
        return f"Square(side={self.side})"
    