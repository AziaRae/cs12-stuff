# pyright: strict

from common_types import *

class View:
    
    def display_pesos(self, pesos: int):
        print(f"Pesos: {pesos}")
    
    def display_day(self, day: int):
        print(f"Day {day}")
        
    def display_grid(self, grid: list[list[CropType]]) -> None:
        print("\n".join("".join(str(crop) for crop in row) for row in grid))
        
    def is_inside(self, i: int, j: int, m: int, n: int) -> bool:
        return 0 <= i < m and 0 <= j < n
    
    def prompt_coordinate(self, m: int, n: int) -> tuple[int, int] | None:
        i = int(input(f"Enter row (0-{m - 1}): "))
        j = int(input(f"Enter column (0-{n - 1}): "))
        
        if not self.is_inside(i, j, m, n):
            print("Failed!")
            return
        
        return (i, j)
    
    def prompt_crop(self, seed_packet_mode: SeedPacketMode) -> str | None:
        avilable_crops: set[str] = seed_packet_mode.available_crops()
        
        print("List of available crops: ", end="")
        print(*avilable_crops, sep=" | ")
        
        crop = input(f"Enter a crop: ")
        
        if crop not in avilable_crops:
            print("Failed")
            return
            
        return crop
    
    def prompt_action(self) -> str:
        action: str = input("- ")
        
        return action