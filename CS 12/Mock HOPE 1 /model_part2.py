from common_types import CropType, SeedPacketMode, WateringCanType, VacantCrop

### CROP TYPE ###


class Parsnip:
    def __init__(self) -> None:
        self._cost: int = 100
        self._days_to_grow: int = 1
        self._harvest_value: int = 200
        self._watered_today = False

    def __str__(self) -> str:
        if self._days_to_grow:
            return "p"
        else:
            return "P"

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


class SweetGemBerry:
    def __init__(self) -> None:
        self._cost: int = 300
        self._days_to_grow: int = 3
        self._harvest_value: int = 1000
        self._watered_today = False
        self._watered_days_cont: int = 0

    def __str__(self) -> str:
        if self._days_to_grow:
            return "g"
        else:
            return "G"

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
        if not self._watered_today:
            self._watered_days_cont += 1
        self._watered_today = True

    def go_to_next_day(self) -> None:
        self._days_to_grow = (
            max(0, self._days_to_grow - 1)
            if self._watered_days_cont >= 2
            else self._days_to_grow
        )

        if self._watered_today:
            self._watered_today = False
        else:
            self._watered_days_cont = 0


class AncientFruit:
    def __init__(self) -> None:
        self._cost: int = 1000
        self._days_to_grow: int = 14
        self._harvest_value: int = 6700
        self._watered_today = False
        self._watered_days_cont: int = 0

    def __str__(self) -> str:
        if self._days_to_grow:
            return "a"
        else:
            return "A"

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
        if not self._watered_today:
            self._watered_days_cont += 1
        self._watered_today = True

    def go_to_next_day(self) -> None:
        self._days_to_grow = (
            max(0, self._days_to_grow - self._watered_days_cont)
            if self._watered_today
            else self._days_to_grow
        )

        if self._watered_today:
            self._watered_today = False
        else:
            self._watered_days_cont = 0


### SEED PACKET MODE ###


class StardewValley(SeedPacketMode):
    def __init__(self) -> None:
        super().__init__(
            pesos=400,
            m=9,
            n=9,
            available_crops=[Parsnip(), SweetGemBerry(), AncientFruit()],
        )

    def crop_to_plant(self, crop_input: str) -> CropType:
        match crop_input:
            case "parsnip":
                return Parsnip()

            case "sweetgemberry":
                return SweetGemBerry()

            case "ancientfruit":
                return AncientFruit()

            case _:
                return Parsnip()

    def available_crops(self) -> set[str]:
        return {"parsnip", "sweetgemberry", "ancientfruit"}


### WATERING CAN TYPE ###


class KoyukiAndCans(WateringCanType):
    def __init__(self) -> None:
        super().__init__()
        self._visited: set[tuple[int, int]] = set()

    def is_inside(self, i: int, j: int):
        m: int = len(self._grid)
        n: int = len(self._grid[0])
        return 0 <= i < m and 0 <= j < n

    def manhattan_distance(self, i: int, j: int, center: tuple[int, int]) -> int:
        dy, dx = center
        return abs(i - dy) + abs(j - dx)

    def bfs(self, i: int, j: int, center: tuple[int, int]) -> None:
        grid: list[list[CropType]] = self._grid
        directions: dict[str, tuple[int, int]] = {
            "up": (-1, 0),
            "down": (1, 0),
            "right": (0, 1),
            "left": (0, -1),
        }

        if self.manhattan_distance(i, j, center) > 3:
            return

        original_i, original_j = i, j

        for direction in directions:
            i, j = original_i, original_j

            dy, dx = directions[direction]

            i += dy
            j += dx

            if (i, j) in self._visited:
                return

            self._visited.add((i, j))

            grid[i][j].water()

            self.bfs(i, j, center)

    def water_target(self, i: int, j: int) -> None:
        center: tuple[int, int] = (i, j)

        self._grid[i][j].water()

        self.bfs(i, j, center)

class WaterBucket(WateringCanType):
    def __init__(self) -> None:
        super().__init__()
        self._visited: set[tuple[int, int]] = set()

    def is_inside(self, i: int, j: int):
        m: int = len(self._grid)
        n: int = len(self._grid[0])
        
        return 0 <= i < m and 0 <= j < n

    def bfs(self, i: int, j: int) -> None:
        grid: list[list[CropType]] = self._grid
        directions: dict[str, tuple[int, int]] = {
            "up": (-1, 0),
            "down": (1, 0),
            "right": (0, 1),
            "left": (0, -1),
        }
        
        original_i, original_j = i, j

        for direction in directions:
            i, j = original_i, original_j

            dy, dx = directions[direction]

            i += dy
            j += dx

            if not self.is_inside(i, j):
                return

            if (i, j) in self._visited:
                return

            self._visited.add((i, j))

            grid[i][j].water()

            self.bfs(i, j)

    def water_target(self, i: int, j: int) -> None:
        self._grid[i][j].water()
        crop: CropType = self._grid[i][j]
        
        if not isinstance(crop, VacantCrop):
            self.bfs(i, j)
            
        self._visited.clear()