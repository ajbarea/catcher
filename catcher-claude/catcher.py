import pygame
import random
import sys
import math

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
YELLOW = (255, 255, 0)
PURPLE = (150, 50, 255)
ORANGE = (255, 150, 0)

class Catcher:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 80
        self.height = 20
        self.speed = 8
        self.color = BLUE
    
    def move_left(self):
        if self.x > 0:
            self.x -= self.speed
    
    def move_right(self):
        if self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed
    
    def set_x(self, mouse_x):
        self.x = max(0, min(mouse_x - self.width // 2, SCREEN_WIDTH - self.width))
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height), 2)
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class FallingObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(15, 25)
        self.speed = random.uniform(2, 5)
        self.color = random.choice([RED, GREEN, YELLOW, PURPLE, ORANGE])
        self.points = 10 if self.color != PURPLE else 25
        self.caught = False
    
    def update(self):
        self.y += self.speed
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
        pygame.draw.circle(screen, BLACK, (int(self.x), int(self.y)), self.size, 2)
    
    def get_rect(self):
        return pygame.Rect(self.x - self.size, self.y - self.size, self.size * 2, self.size * 2)
    
    def is_off_screen(self):
        return self.y > SCREEN_HEIGHT + self.size

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Catcher Game")
        self.clock = pygame.time.Clock()
        
        self.catcher = Catcher(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        self.falling_objects = []
        self.score = 0
        self.missed_objects = 0
        self.max_misses = 3
        self.game_over = False
        self.paused = False
        
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)
        
        self.spawn_timer = 0
        self.spawn_rate = 60
        self.combo_multiplier = 1
        self.combo_timer = 0
        
    def spawn_object(self):
        x = random.randint(20, SCREEN_WIDTH - 20)
        self.falling_objects.append(FallingObject(x, -20))
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return False
                elif event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused
                elif event.key == pygame.K_SPACE and self.game_over:
                    self.restart_game()
        
        if not self.paused and not self.game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.catcher.move_left()
            if keys[pygame.K_d]:
                self.catcher.move_right()
            
            mouse_x, _ = pygame.mouse.get_pos()
            if not (keys[pygame.K_a] or keys[pygame.K_d]):
                self.catcher.set_x(mouse_x)
        
        return True
    
    def update(self):
        if self.paused or self.game_over:
            return
        
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_rate:
            self.spawn_object()
            self.spawn_timer = 0
            self.spawn_rate = max(20, self.spawn_rate - 0.5)
        
        catcher_rect = self.catcher.get_rect()
        
        for obj in self.falling_objects[:]:
            obj.update()
            
            if obj.get_rect().colliderect(catcher_rect) and not obj.caught:
                obj.caught = True
                points = obj.points * self.combo_multiplier
                self.score += points
                self.combo_multiplier = min(5, self.combo_multiplier + 0.2)
                self.combo_timer = 60
                self.falling_objects.remove(obj)
            
            elif obj.is_off_screen():
                if not obj.caught:
                    self.missed_objects += 1
                    if self.missed_objects >= self.max_misses:
                        self.game_over = True
                self.falling_objects.remove(obj)
        
        if self.combo_timer > 0:
            self.combo_timer -= 1
        else:
            self.combo_multiplier = max(1, self.combo_multiplier - 0.1)
    
    def draw(self):
        self.screen.fill(WHITE)
        
        if not self.game_over:
            self.catcher.draw(self.screen)
            
            for obj in self.falling_objects:
                obj.draw(self.screen)
        
        score_text = self.font.render(f"Score: {int(self.score)}", True, BLACK)
        self.screen.blit(score_text, (10, 10))
        
        multiplier_text = self.font.render(f"Multiplier: {self.combo_multiplier:.1f}x", True, BLACK)
        self.screen.blit(multiplier_text, (10, 50))
        
        misses_text = self.font.render(f"Misses: {self.missed_objects}/{self.max_misses}", True, BLACK)
        self.screen.blit(misses_text, (10, 90))
        
        if self.paused:
            pause_text = self.big_font.render("PAUSED", True, BLACK)
            text_rect = pause_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            self.screen.blit(pause_text, text_rect)
            
            resume_text = self.font.render("Press ESC to resume", True, BLACK)
            resume_rect = resume_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 60))
            self.screen.blit(resume_text, resume_rect)
        
        if self.game_over:
            game_over_text = self.big_font.render("GAME OVER", True, RED)
            text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
            self.screen.blit(game_over_text, text_rect)
            
            final_score_text = self.font.render(f"Final Score: {int(self.score)}", True, BLACK)
            score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            self.screen.blit(final_score_text, score_rect)
            
            restart_text = self.font.render("Press SPACE to restart or Q to quit", True, BLACK)
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50))
            self.screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
    
    def restart_game(self):
        self.catcher = Catcher(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        self.falling_objects = []
        self.score = 0
        self.missed_objects = 0
        self.game_over = False
        self.spawn_timer = 0
        self.spawn_rate = 60
        self.combo_multiplier = 1
        self.combo_timer = 0
    
    def run(self):
        running = True
        
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()