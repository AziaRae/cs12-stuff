# pyright: strict

from abc import ABC

class Gallade(ABC):
    def get_ability_set(self) -> set[str]:
        # get all function names and return as a string
        ...
        
    
class GalladeGenerationIV(Gallade):
    def Steadfast(self):
        ...
        
class GalladeGenerationV(GalladeGenerationIV):
    def justified(self):
        ...
        
class GalladeGenerationVI(GalladeGenerationV):
    ...
    
class GalladeGenerationVII(GalladeGenerationVI):
    ...
    
class GalladeGenerationVIII(GalladeGenerationVII):
    ...
    
class GalladeGenerationIX(GalladeGenerationVIII):
    def Sharpness(self):
        ...