from settings import *




class Sprite(pygame.sprite.Sprite):
    
    def __init__(self,pos,surf, groups):
        super().__init__(groups)
        self.image = surf   
        self.rect  = self.image.get_frect(center = pos)
        
        
        
class Bird(Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)
        
        
        
    # def update(self, *args, **kwargs):
    #     return super().update(*args, **kwargs)