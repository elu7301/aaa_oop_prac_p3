class Color:
    """
    Represents a color with red, green, and blue channels.
    """

    def __init__(self, red: int, green: int, blue: int) -> None:
        """
        Initializes a Color object with the specified RGB values.

        Args:
            red (int): The red channel value (0-255).
            green (int): The green channel value (0-255).
            blue (int): The blue channel value (0-255).
        """
        self.red = red
        self.green = green
        self.blue = blue

    def __eq__(self, other: object) -> bool:
        """
        Checks if two Color objects are equal.

        Args:
            other (object): The other object to compare.

        Returns:
            bool: True if the two Color objects are equal, False otherwise.
        """
        if isinstance(other, Color):
            return (
                    self.red == other.red
                    and self.green == other.green
                    and self.blue == other.blue
            )
        return False

    def __hash__(self) -> int:
        """
        Calculates the hash value of the Color object.

        Returns:
            int: The hash value.
        """
        return hash((self.red, self.green, self.blue))

    def __str__(self) -> str:
        """
        Returns a string representation of the Color object.

        Returns:
            str: The string representation.
        """
        return "\033[38;2;{};{};{}m●\033[0m".format(self.red, self.green, self.blue)

    def __add__(self, other: "Color") -> "Color":
        """
        Adds two Color objects.

        Args:
            other (Color): The other Color object to add.

        Returns:
            Color: The sum of the two Color objects.
        """
        if isinstance(other, Color):
            new_red = min(self.red + other.red, 255)
            new_green = min(self.green + other.green, 255)
            new_blue = min(self.blue + other.blue, 255)
            return Color(new_red, new_green, new_blue)
        return None

    def __mul__(self, other: float) -> "Color":
        """
        Multiplies a Color object by a scalar.

        Args:
            other (float): The scalar value to multiply the Color object by.

        Returns:
            Color: The Color object multiplied by the scalar.

        Raises:
            ValueError: If the contrast value is not between 0 and 1.
        """
        if isinstance(other, (int, float)):
            if 0 <= other <= 1:
                cl = -256 * (1 - other)
                f = (259 * (cl + 255)) / (255 * (259 - cl))
                new_red = min(int(f * (self.red - 128) + 128), 255)
                new_green = min(int(f * (self.green - 128) + 128), 255)
                new_blue = min(int(f * (self.blue - 128) + 128), 255)
                return Color(new_red, new_green, new_blue)
            else:
                raise ValueError("The contrast value must be between 0 and 1.")
        return None

    def __rmul__(self, other: float) -> "Color":
        """
        Multiplies a Color object by a scalar (right multiplication).

        Args:
            other (float): The scalar value to multiply the Color object by.

        Returns:
            Color: The Color object multiplied by the scalar.

        Raises:
            ValueError: If the contrast value is not between 0 and 1.
        """
        return self.__mul__(other)


if __name__ == "__main__":
    # t1
    red = Color(255, 0, 0)
    print(red)
    # t2
    green = Color(0, 255, 0)
    print(red == green)
    print(red == Color(255, 0, 0))
    # t3
    print(red + green)
    # t4
    orange1 = Color(255, 165, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    print(len(set(color_list)))
    # t5
    print(0.5 * red)
