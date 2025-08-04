from settings import *
from sprites import *
from support import *
from random import choice,shuffle


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Bird Sorting Game')
        self.clock = pygame.time.Clock()
        self.running = True 
        
        #groups
        self.all_sprites = pygame.sprite.Group()
        
        self.chick_surf = import_image('images','PNG','Round','chick')
        self.duck_surf = import_image('images','PNG','Round','duck')
        self.chicken_surf = import_image('images','PNG','Round','chicken')
        self.owl_surf = import_image('images','PNG','Round','owl')
        
    
        # Bird Generation 
        
        amount_of_birds = 5
        amount_of_branches= 3
        
        x_coord,y_coord = 100,200
        
        sprite_width =self.chick_surf.get_width() + 10

        bird_names = ['chick','owl','duck','chicken']
        
        # generate the names depending on how many branches are available
        bird_names = bird_names[0:amount_of_branches] * amount_of_birds        
        
        shuffle(bird_names)
        
        #create a list of all the location depending on the amount of branches
        all_birds_locations = [] 
        
        for _ in range(amount_of_branches):
            for _ in range(amount_of_birds):
                all_birds_locations.append((x_coord,y_coord))
                x_coord +=sprite_width
                
            y_coord +=sprite_width
            x_coord=100
            
        #zip the list the list together
        
        full_list = zip(all_birds_locations,bird_names)
        
        #display the birds
        for coord,b_name in full_list:
            Bird((coord),import_image('images','PNG','Round',b_name),self.all_sprites)


        
        


    def run(self):
        while self.running:
            dt =self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            #update
            self.all_sprites.update(dt)

            #draw 
            
            self.display_surface.fill(COLORS['white'])
            self.all_sprites.draw(self.display_surface)
            
            
            pygame.display.update()

        pygame.quit()
        
if __name__ == '__main__':
    game = Game()
    game.run()