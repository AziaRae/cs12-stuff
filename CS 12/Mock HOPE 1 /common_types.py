# pyright: strict

from __future__ import annotations
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


##################################


class WateringCanType(ABC):
    def __init__(self) -> None:
        self._grid: list[list[CropType]] = []

    def get_grid(self, grid: list[list[CropType]]):
        self._grid = grid

    @abstractmethod
    def water_target(self, i: int, j: int): ...
