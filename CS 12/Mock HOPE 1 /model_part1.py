# pyright: strict

from common_types import *

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
        
        