# pyright: strict

from abc import ABC, abstractmethod
from typing import Protocol


class CropType(Protocol):
    def __init__(self) -> None: ...

    def __str__(self) -> str: ...

    @property
    def cost(self) -> int: ...

    @property
    def days_to_grow(self) -> int: ...

    @property
    def harvest_value(self) -> int: ...

    def ready_to_harvest(self) -> bool: ...

    def water(self) -> None: ...

    def go_to_next_day(self) -> None: ...


class VacantCrop:
    def __init__(self) -> None: ...

    def __str__(self) -> str:
        return "."

    @property
    def cost(self) -> int: ...

    @property
    def days_to_grow(self) -> int: ...

    @property
    def harvest_value(self) -> int: ...

    def ready_to_harvest(self) -> bool: ...

    def water(self) -> None: ...

    def go_to_next_day(self) -> None: ...


class Turnip:
    def __init__(self) -> None:
        self._cost: int = 300
        self._days_to_grow: int = 2
        self._harvest_value: int = 500
        self._watered_today = False

    def __str__(self) -> str:
        if self._days_to_grow:
            return "t"
        else:
            return "T"

    @property
    def cost(self) -> int:
        return self._cost

    @property
    def days_to_grow(self) -> int:
        return self._days_to_grow

    @property
    def harvest_value(self) -> int:
        return self._harvest_value

    def ready_to_harvest(self) -> bool:
        return self._days_to_grow == 0

    def water(self):
        self._watered_today = True

    def go_to_next_day(self) -> None:
        self._days_to_grow = (
            max(0, self._days_to_grow - 1)
            if self._watered_today
            else self._days_to_grow
        )
        self._watered_today = False


class Sunflower:
    def __init__(self) -> None:
        self._cost: int = 25
        self._days_to_grow: int = 1
        self._harvest_value: int = 500
        self._watered_today: bool = False

    def __str__(self) -> str:
        if self._days_to_grow:
            return "s"
        else:
            return "S"

    @property
    def cost(self) -> int:
        return self._cost

    @property
    def days_to_grow(self) -> int:
        return self._days_to_grow

    @property
    def harvest_value(self) -> int:
        return self._harvest_value

    def ready_to_harvest(self) -> bool:
        return self._days_to_grow == 0

    def water(self):
        self._watered_today = True

    def go_to_next_day(self) -> None:
        self._days_to_grow = (
            max(0, self._days_to_grow - 1)
            if self._watered_today
            else self._days_to_grow
        )
        self._watered_today = False


class Marigold:
    def __init__(self) -> None:
        self._cost: int = 50
        self._days_to_grow: int = 2
        self._harvest_value: int = 150
        self._watered_today = False

    def __str__(self) -> str:
        if self._days_to_grow:
            return "m"
        else:
            return "M"

    @property
    def cost(self) -> int:
        return self._cost

    @property
    def days_to_grow(self) -> int:
        return self._days_to_grow

    @property
    def harvest_value(self) -> int:
        return self._harvest_value

    def ready_to_harvest(self) -> bool:
        return self._days_to_grow == 0

    def water(self):
        self._watered_today = True

    def go_to_next_day(self) -> None:
        self._days_to_grow = (
            max(0, self._days_to_grow - 1)
            if self._watered_today
            else self._days_to_grow
        )
        self._watered_today = False


##################################


class SeedPacketMode(ABC):
    def __init__(
        self, pesos: int, m: int, n: int, available_crops: list[CropType]
    ) -> None:  
        self._pesos: int = pesos
        self._m: int = m
        self._n: int = n
        self._available_crops: list[CropType] = available_crops

        self._grid: list[list[CropType]] = []

        super().__init__()

    def initialize_grid(self) -> list[list[CropType]]:
        grid: list[list[CropType]] = [
            [VacantCrop() for _ in range(self._n)] for _ in range(self._m)
        ]
        self._grid = grid
        return grid

    def harvest(self) -> None:
        for i, row in enumerate(self._grid):
            for j, crop in enumerate(row):
                if isinstance(crop, VacantCrop):
                    continue

                if crop.ready_to_harvest():
                    self._pesos += crop.harvest_value
                    self._grid[i][j] = VacantCrop()

    def plant_crop(self, i: int, j: int, crop: CropType):
        self._grid[i][j] = crop

    def go_to_next_day(self) -> None:
        for row in self._grid:
            for crop in row:
                crop.go_to_next_day()

    @abstractmethod
    def crop_to_plant(self, crop_input: str) -> CropType: ...

    @abstractmethod
    def available_crops(self) -> set[str]: ...

    @property
    def m(self):
        return self._m

    @property
    def n(self):
        return self._n

    @property
    def pesos(self):
        return self._pesos

    @property
    def grid(self):
        return self._grid


class AnimalCrossing(SeedPacketMode):
    def __init__(self) -> None:
        super().__init__(pesos=1000, m=5, n=5, available_crops=[Turnip()])

    def crop_to_plant(self, crop_input: str) -> CropType:
        match crop_input:
            case "turnip":
                return Turnip()

            case _:
                return Turnip()

    def available_crops(self) -> set[str]:
        return {"turnip"}


class PvZ(SeedPacketMode):
    def __init__(self) -> None:
        super().__init__(pesos=100, m=5, n=9, available_crops=[Marigold(), Sunflower()])

    def crop_to_plant(self, crop_input: str) -> CropType:
        match crop_input:
            case "marigold":
                return Marigold()

            case "sunflower":
                return Sunflower()

            case _:
                return Marigold()

    def available_crops(self) -> set[str]:
        return {"marigold", "sunflower"}


##################################


class WateringCanType(ABC):
    def __init__(self) -> None:
        self._grid: list[list[CropType]] = []

    def get_grid(self, grid: list[list[CropType]]):
        self._grid = grid

    def water_target(self, i: int, j: int): ...


class BasicCan(WateringCanType):
    def __init__(self) -> None:
        super().__init__()

    def water_target(self, i: int, j: int) -> None:
        self._grid[i][j].water()


class SteelCan(WateringCanType):
    def __init__(self) -> None:
        super().__init__()

    def water_target(self, i: int, j: int):
        start_cell: tuple[int, int] = (i - 1, j - 1)
        end_cell: tuple[int, int] = (i + 1, j + 1)

        for dy in range(start_cell[0], end_cell[0] + 1):
            for dx in range(start_cell[1], end_cell[1] + 1):

                if not self.is_inside(i, j, self._grid):
                    continue

                self._grid[dy][dx].water()

    @staticmethod
    def is_inside(i: int, j: int, grid: list[list[CropType]]):
        height: int = len(grid)
        width: int = len(grid[0])

        return 0 <= i < height and 0 <= j < width
