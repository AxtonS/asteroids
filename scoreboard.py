import pygame

from constants import SCORE_BOARD_LIVES, SCORE_BOARD_SCORE


class ScoreBoard(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]
    
    def __init__(self) -> None:
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()
        self.font = pygame.font.Font(None, 36)
        self.score = SCORE_BOARD_SCORE
        self.lives = SCORE_BOARD_LIVES
        self.position = pygame.Vector2(10, 10)


    def draw(self, screen: pygame.Surface) -> None:
        score_text = self.font.render(f"Score: {self.score} Lives: {self.lives}", True, (0, 255, 0))
        screen.blit(score_text, self.position)


    def modify_score(self, amount: int) -> None:
        self.score += amount


    def modify_lives(self, amount: int) -> None:
        self.lives += amount
        