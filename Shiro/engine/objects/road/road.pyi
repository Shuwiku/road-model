class Road:
    """Класс дороги.
    Дорога состоит из точек, по которым движется транспорт."""

    def __init__(self,
                 next_roads: list[str],
                 road_id: str,
                 road_points: list[list[int, int], list[int, int]]):
        """Инициализация нового объекта класса."""

    @property
    def next_roads(self) -> list[str]:
        """Свойство класса.
        Возвращает список с id следующих дорог."""

    @property
    def road_id(self) -> str:
        """Свойство класса.
        Возвращает id дороги."""

    @property
    def road_points(self) -> list[list[int, int], list[int, int]]:
        """Свойство класса.
        Возвращает точки дороги."""
