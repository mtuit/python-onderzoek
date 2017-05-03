from factory.shape_factory import ShapeFactory


def main():
    circle = ShapeFactory.create_shape("Circle")
    square = ShapeFactory.create_shape("Square")

    circle.set_diameter(5)
    square.set_width(5)

    print(circle.calculate_surface())
    print(square.calculate_surface())

if __name__ == '__main__':
    main()