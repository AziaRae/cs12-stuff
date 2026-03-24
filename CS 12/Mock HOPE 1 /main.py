from model_part1 import Model
from controller import Controller
from view import View
from common_types import *


def main():
    model: Model = Model(AnimalCrossing(), SteelCan())

    view: View = View()

    controller: Controller = Controller(model, view)
    
    controller.run()


if __name__ == "__main__":
    main()
