# pyright: strict

from copy import deepcopy

from common_types import *
from model_part1 import *
from view import *


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self._model: Model = model
        self._view: View = view

    def prompt_action(self, model: Model, view: View) -> tuple[Model, View]:
        while True:
            action = view.prompt_action()

            match action:
                case "p":
                    crop = view.prompt_crop(model.seed_packet_mode)
                    if crop is None:
                        continue

                    coordinate = view.prompt_coordinate(model.m, model.n)
                    if coordinate is None:
                        continue

                    plant_this_crop: CropType = model.seed_packet_mode.crop_to_plant(crop)
                    model.seed_packet_mode.plant_crop(*coordinate, plant_this_crop)
                    print("Success!")

                case "w":
                    coordinate = view.prompt_coordinate(model.m, model.n)
                    if coordinate is None:
                        print("Failed.")
                        continue

                    model.watering_can_type.water_target(*coordinate)
                    print("Success!")

                case "h":
                    old_grid: list[list[CropType]] = deepcopy(model.grid)
                    model.seed_packet_mode.harvest()
                    new_grid: list[list[CropType]] = deepcopy(model.grid)
                    
                    if old_grid == new_grid:
                        print("Failed.")
                        continue
                    
                    print("Success.")
                case "n":
                    for row in model.grid:
                        for crop in row:
                            crop.go_to_next_day()
                    model.go_to_next_day()
                    print("Day ended.")
                    
                case "g":
                    view.display_pesos(model.pesos)

                case _:
                    print("Failed.")
                    continue

            return (model, view)

    def run(self):
        model: Model = self._model
        view: View = self._view

        model.initialize_grid()
        model.watering_can_type.get_grid(model.seed_packet_mode.grid)

        while model.continue_game:
            view.display_day(model.current_day)
            view.display_pesos(model.pesos)
            view.display_grid(model.grid)
            model, view = self.prompt_action(model, view)
            
