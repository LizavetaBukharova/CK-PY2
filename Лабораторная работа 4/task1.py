class Cloches:
    """Базовый класс - одежда"""
    def __init__(self, material: str, color: str, size: int):
        self.material = material
        self.color = color
        self.size = size

    def __eq__(self: "Cloches", other: "Cloches"):
        return self.size == other.size

    @staticmethod
    def determine_size(size: int, body_data: list) -> int:
        """
        Метод проверяет какой размер нужен пользователю
        :param size: размер
        :param body_data : мерки пользователя
        return: size"""
        ...

    def __str__(self):
        return f"Одежда из материала -{self.material}. Цвет {self.color}. Размер {self.size}."

    def __repr__(self):
        return f"{self.__class__.__name__}(material={self.material}, color={self.color}, size={self.size})"

    @property
    def material(self) -> str:
        return self._material

    @material.setter
    def material(self, material: str) -> None:
        if not isinstance(material, str):
            raise TypeError
        self._material = material

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, color: str) -> None:
        if not isinstance(color, str):
            raise TypeError
        self._color = color

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, size: int) -> None:
        if not isinstance(size, int):
            raise TypeError
        if not (28 <= size <= 56):
            raise ValueError
        if not (size % 2 == 0):
            raise ValueError
        self._size = size


class Coat(Cloches):
    """Дочерний класс - пальто"""
    def __init__(self, material : str, color: str, size: int, season: str):
        super().__init__(material, color, size)
        if not isinstance(season, str):
            raise TypeError
        self.season = season

    def determine_coat(self, season: str, data: list) -> bool:
        """Функция проверяет подходит ли это пальто в данный сезон
         :param season: сезон пальто
         :param data: дата
         :return подходит ли это пальто данному сезону"""
        ...

    def __str__(self):
        return f"Пальто из {self.material}. Цвет {self.color}. Размер {self.size}. Сезон {self.season}"

    def __repr__(self):
        return f"{self.__class__.__name__}(material={self.material}, color={self.color}, size={self.size}, season={self.season})"


class Skirt(Cloches):
    """Дочерний класс - юбка"""
    def __init__(self, material: str, color: str, size: int, style: str):
        super().__init__(material, color, size)
        if not isinstance(style, str):
            raise TypeError
        self.style = style

    def determine_skirt(self, style: str, event: str) -> bool:
        """Функция проверяет подходит ли эта юбка на данное мероприятие
         :param style: стиль юбки
         :param event: мероприятие
         :return подходит ли эта юбка"""
        ...

    def __str__(self):
        return f"Юбка из {self.material}. Цвет {self.color}. Размер {self.size}. Стиль {self.style}"

    def __repr__(self):
        return f"{self.__class__.__name__}(material={self.material}, color={self.color}, size={self.size}, style={self.style})"


if __name__ == "__main__":
    cloches = Coat(material="wool", color="pink", size=30, season="winter")
    print(cloches)
    print(Cloches("wool", "blue", 40))
    print(repr(Skirt("wool", "blue", 28, "casual")))
    cloches = Coat(material="wool", color="pink", size=30, season="autumn")
    cloches_1 = Skirt(material="wool", color=",blue", size=30, style="high fashion")
    print(cloches == cloches_1)

