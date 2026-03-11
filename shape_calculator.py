import math


class Rectangle:
    def __init__(self, width: int | float, height: int | float) -> None:
        self.width = width
        self.height = height

    def set_width(self, width: int | float) -> None:
        self.width = width

    def set_height(self, height: int | float) -> None:
        self.height = height

    def get_area(self) -> int | float:
        return self.width * self.height

    def get_perimeter(self) -> int | float:
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> float:
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape: "Rectangle") -> int:
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side: int | float) -> None:
        super().__init__(side, side)

    @property
    def side(self) -> int | float:
        return self.width

    def set_side(self, side: int | float) -> None:
        self.width = side
        self.height = side

    def set_width(self, width: int | float) -> None:
        self.set_side(width)

    def set_height(self, height: int | float) -> None:
        self.set_side(height)

    def __str__(self) -> str:
        return f"Square(side={self.side})"
