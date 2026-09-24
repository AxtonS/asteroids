import pygame


class ScoreBoard(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]
    
    def __init__(self) -> None:
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        self.position = pygame.Vector2(10, 10)


    def draw(self, screen: pygame.Surface) -> None:
        score_text = self.font.render(f"Score: {self.score}", True, (0, 255, 0))
        screen.blit(score_text, self.position)


    def increase(self) -> None:
        self.score += 1
        