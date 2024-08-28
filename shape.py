from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Shape:
    def area(self):
        pass

class ColoredShape(Shape):
    def __init__(self, color):
 
        if not isinstance(color, Color):
            raise ValueError("Color must be an instance of Color enum")
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if not isinstance(value, Color):
            raise ValueError("Color must be an instance of Color enum")
        self._color = value

    def __str__(self):
        return f"Shape with color {self.color.name}"



# 定义具体的带颜色的圆形类 Circle，继承自 ColoredShape
class Circle(ColoredShape):
    def __init__(self, radius, color):
        self.radius = radius
        super().__init__(color)

    # 计算圆形面积的方法
    @property
    def area(self):
        return 3.14 * self.radius ** 2

    # 自定义 __str__ 方法，输出圆形的描述
    def __str__(self):
        return f"Circle with color {self.color.name}"

# 创建 Circle 对象，设置半径和颜色
c = Circle(5, Color.RED)
print(c.area)  # 输出 78.5
print(c)       # 输出 "Circle with color RED"

# 修改颜色
c.color = Color.GREEN
print(c)       # 输出 "Circle with color GREEN"
