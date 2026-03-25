# pyright: strict

from common_types import CropType, SeedPacketMode, WateringCanType

class Model:
    def __init__(self, seed_packet_mode: SeedPacketMode, watering_can_type: WateringCanType) -> None:
        self._seed_packet_mode: SeedPacketMode = seed_packet_mode
        self._watering_can_type: WateringCanType = watering_can_type
        self._grid: list[list[CropType]] = self._seed_packet_mode.grid
        self._m = self._seed_packet_mode.m
        self._n = self._seed_packet_mode.n
        self._current_day: int = 1
        self._continue_game: bool = True
        
    @property
    def m(self):
        return self._m
    
    @property
    def n(self):
        return self._n
        
    @property
    def continue_game(self):
        return self._continue_game
        
    @property
    def current_day(self):
        return self._current_day
    
    @property
    def seed_packet_mode(self):
        return self._seed_packet_mode
    
    @property 
    def watering_can_type(self):
        return self._watering_can_type
    
    def go_to_next_day(self):
        self._current_day += 1
        
    @property
    def pesos(self):
        return self.seed_packet_mode.pesos
    
    @property
    def grid(self):
        return self._grid
    
    def stop_game(self):
        self._continue_game = False
        
    def initialize_grid(self):
        self._grid = self._seed_packet_mode.initialize_grid()
        
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


# ###############################################


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


# ################################################


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
