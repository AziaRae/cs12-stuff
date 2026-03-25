from model_part1 import *
from model_part2 import *
from controller import Controller
from view import View
from common_types import *
from argparse import ArgumentParser


def main():

    parser = ArgumentParser(
        prog="MOCK HOPE 1",
    )
    
    parser.add_argument("--mode", type=str)
    parser.add_argument("--water", type=str)
    
    args = parser.parse_args()
    
    mode: str = args.mode 
    water: str = args.water
    
    match mode:
        case "ac":
            seed_packet_mode: SeedPacketMode = AnimalCrossing()
            
        case "pvz":
            seed_packet_mode: SeedPacketMode = PvZ()
            
        case "sdv":
            seed_packet_mode: SeedPacketMode = StardewValley()
        
        case _: 
            print("INVALID MODE!!")
            raise ValueError
    
    match water:
        case "basic":
            watering_can_type: WateringCanType = BasicCan()
            
        case "steel":
            watering_can_type: WateringCanType = SteelCan()
            
        case "koyuki":
            watering_can_type: WateringCanType = KoyukiAndCans()
            
        case "bucket":
            watering_can_type: WateringCanType = WaterBucket()
        
        case _: 
            print("INVALID WATER")
            raise ValueError


    model: Model = Model(seed_packet_mode, watering_can_type)

    view: View = View()

    controller: Controller = Controller(model, view)

    controller.run()


if __name__ == "__main__":
    main()
