import pygame 
pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT=500,500
display_surface=pygame.display.set_mode(SCREEN_WIDTH, SCREEN_HEIGHT)
pygame.display.set_caption("Adding image & backgrond image")
background_image=pygame.transform.scale(
    pygame.image.load('download(1).jpeg').convert(),(SCREEN_WIDTH,SCREEN_HEIGHT)
)
penguin_imasge=pygame.transform.scale(
    pygame.image.load('download(2).jpeg').convert_alpha(),(200,200)
)
penguin_rect=penguin_imasge.get_rect(center=(SCREEN_WIDTH//2,
                                             SCREEN_HEIGHT//2-30))
text=pygame.font.Font(None,36).render('Hello world',True,
                                      pygame.Color('black'))
text_rect=text.get_rect(center=(SCREEN_WIDTH//2,
                                             SCREEN_HEIGHT//2+110))  
def game_loop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.grt():
            if event.type==pygame.QUIT:
            running=False
        display_surface.blit(background_image,(0,0))
        display_surface.blit(penguin_image,penguin_rect)
        display_surface.blit(text,text_rect)

        Pygame.display.flip()
        clock.tick(30)
    pygame.quit    
if __name__=="__main__":
    game_loop()