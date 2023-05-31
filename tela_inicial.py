import pygame

GAME = 1
QUIT = 0

def tela_inicial(janela):
    clock = pygame.time.Clock()

    rodando = True
    while rodando:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = QUIT
                rodando = False
            
            if event.type == pygame.KEYUP:
                state = GAME
                rodando = False
        
        janela.fill((0,0,0))

        fonte = pygame.font.SysFont(None,32)
        prescione = fonte.render('Prescione espaço para iniciar', False, (255,255,255))
        prescione_rect = prescione.get_rect()
        prescione_rect.midbottom = (200, 200)
        janela.blit(prescione,prescione_rect)

        pygame.display.flip()
    return state