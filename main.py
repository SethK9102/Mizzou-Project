import random
import pygame

from turtle_object import Turtle_object
from saving import Database_manager
from game_physics import GamePhysics

pygame.init()

trtl = Turtle_object()
db = Database_manager()
db.create()

info = pygame.display.Info()
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h - 85
BACKROUND_COLOR = (14, 135, 204)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

TURTLE_SIZE = 32
physics = GamePhysics(SCREEN_WIDTH, SCREEN_HEIGHT, turtle_size=TURTLE_SIZE)


def main():
    turtle_x = SCREEN_WIDTH // 2 - TURTLE_SIZE // 2
    turtle_y = SCREEN_HEIGHT // 2 - TURTLE_SIZE // 2
    turtle_rect = pygame.Rect(turtle_x, turtle_y, TURTLE_SIZE, TURTLE_SIZE)

    food_rects = []
    for _ in range(5):
        fx = random.randint(-300, -10)
        fy = random.randint(0, SCREEN_HEIGHT - 12)
        food_rects.append({"rect": pygame.Rect(fx, fy, 12, 12), "speed": random.randint(1, 3)})

    obstacles = []
    for _ in range(3):
        ox = random.randint(0, SCREEN_WIDTH - 30)
        oy = random.randint(0, SCREEN_HEIGHT - 30)
        ob_rect = pygame.Rect(ox, oy, 28, 28)
        plastic_list = ["Images/Bottle.png", "Images/Plastic_Bag.png", "Images/Straw.png"]
        obstacles.append({
            "rect": ob_rect,
            "dir_x": random.choice([-1, 1]),
            "dir_y": random.choice([-1, 1]),
            "speed": random.randint(1, 3),
            "image": pygame.image.load(random.choice(plastic_list))
        })

    running = True
    font = pygame.font.Font(None, 28)

    invuln_until = 0
    invuln_ms = 1500

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        turtle_x, turtle_y = physics.turtle_movement(turtle_x, turtle_y, keys)
        turtle_rect.topleft = (turtle_x, turtle_y)

        # move trash left->right; respawn on left when off-screen
        for ob in obstacles:
            ob["rect"].x += ob["speed"]
            if ob["rect"].left > SCREEN_WIDTH:
                ob["rect"].x = -ob["rect"].width
                ob["rect"].y = random.randint(0, SCREEN_HEIGHT - ob["rect"].height)
                ob["speed"] = 1 + min(32, 1 + trtl.score // 50 + random.randint(0, 2))

        # move food left->right and handle collisions
        for f in food_rects:
            f["rect"].x += f["speed"]
            if f["rect"].left > SCREEN_WIDTH:
                f["rect"].x = -f["rect"].width
                f["rect"].y = random.randint(0, SCREEN_HEIGHT - f["rect"].height)
                f["speed"] = 1 + min(16, 1 + trtl.score // 50 + random.randint(0, 2))

        food_rect_list = [f["rect"] for f in food_rects]
        collided_indices = physics.check_food_collision(turtle_rect, food_rect_list)
        for index in sorted(collided_indices, reverse=True):
            food_rects.pop(index)
            trtl.gain_score(10)

        obstacle_rects = [ob["rect"] for ob in obstacles]
        now = pygame.time.get_ticks()
        if now >= invuln_until and physics.check_obstacle_collision(turtle_rect, obstacle_rects):
            trtl.lives -= 1
            if trtl.lives <= 0:
                running = False
            else:
                invuln_until = now + invuln_ms
                turtle_x = SCREEN_WIDTH // 2 - TURTLE_SIZE // 2
                turtle_y = SCREEN_HEIGHT // 2 - TURTLE_SIZE // 2
                turtle_rect.topleft = (turtle_x, turtle_y)

        while len(food_rects) < 5:
            fx = random.randint(-300, -10)
            fy = random.randint(0, SCREEN_HEIGHT - 12)
            food_rects.append({"rect": pygame.Rect(fx, fy, 12, 12), "speed": random.randint(1, 3)})

        # increase trash count as score increases
        desired_trash = 3 + (trtl.score // 50)
        while len(obstacles) < desired_trash:
            ox = random.randint(-300, -30)
            oy = random.randint(0, SCREEN_HEIGHT - 30)
            ob_rect = pygame.Rect(ox, oy, 28, 28)
            obstacles.append({
                "rect": ob_rect,
                "speed": 1 + min(6, 1 + trtl.score // 50 + random.randint(0, 2)),
            })

        screen.fill((14, 135, 204))
        if now < invuln_until and (now // 200) % 2 == 0:
            pass
        else:
            image = pygame.image.load("Images/Turtle.png")
            pygame.draw.rect(screen, BACKROUND_COLOR, turtle_rect)
            turtle_image_rect = image.get_rect(center=turtle_rect.center) 
            screen.blit(image, turtle_image_rect)

        for f in food_rects:
            pygame.draw.rect(screen, (255, 200, 0), f["rect"])
            image = pygame.image.load("Images/Shrimp.png")
            screen.blit(image, f["rect"])
        for ob in obstacles:
            pygame.draw.rect(screen, (150, 30, 30), ob["rect"])
            screen.blit(ob["image"], ob["rect"])

        score_surf = font.render(f"Score: {trtl.score}", True, (255, 255, 255))
        lives_surf = font.render(f"Lives: {trtl.lives}", True, (255, 255, 255))
        screen.blit(score_surf, (10, 10))
        screen.blit(lives_surf, (10, 40))

        pygame.display.flip()
        clock.tick(60)

    def prompt_player_name():
        name = ""
        pf = pygame.font.Font(None, 36)
        while True:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    return None
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_RETURN:
                        return name.strip() or None
                    if ev.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if ev.unicode and ev.unicode.isprintable() and len(name) < 16:
                            name += ev.unicode

            screen.fill((10, 10, 30))
            screen.blit(pf.render("Game Over - Enter your name:", True, (255, 255, 255)), (40, 40))
            screen.blit(pf.render(name, True, (255, 200, 0)), (40, 90))
            pygame.display.flip()
            clock.tick(30)

    def show_high_scores(high_scores):
        hf = pygame.font.Font(None, 32)
        items = sorted(high_scores.items(), key=lambda x: x[1], reverse=True)
        while True:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    return
                if ev.type == pygame.KEYDOWN:
                    return

            screen.fill((0, 0, 0))
            screen.blit(hf.render("High Scores:", True, (255, 255, 255)), (40, 20))
            for i, (n, s) in enumerate(items[:10]):
                screen.blit(hf.render(f"{i+1}. {n}: {s}", True, (200, 200, 200)), (40, 70 + i * 30))
            screen.blit(hf.render("Press any key or close to exit", True, (120, 120, 120)), (40, SCREEN_HEIGHT - 50))
            pygame.display.flip()
            clock.tick(30)

    if trtl.lives <= 0:
        player_name = prompt_player_name()

        try:
            latest = db.read()
        except Exception:
            latest = None

        if latest and isinstance(latest, list) and len(latest) >= 2:
            row_id = latest[0]
            high_scores = latest[1] if isinstance(latest[1], dict) else {}
            db.id = row_id
        else:
            row_id = 0
            high_scores = {}

        if player_name:
            high_scores[player_name] = max(high_scores.get(player_name, 0), trtl.score)

        sorted_items = sorted(high_scores.items(), key=lambda x: x[1], reverse=True)[:10]
        new_scores = dict(sorted_items)

        if row_id == 0:
            db.add(new_scores)
        else:
            db.update(new_scores)

        show_high_scores(high_scores)
    else:
        try:
            latest = db.read()
        except Exception:
            latest = None

        if latest and isinstance(latest, list) and len(latest) >= 2:
            row_id = latest[0]
            high_scores = latest[1] if isinstance(latest[1], dict) else {}
            db.id = row_id
        else:
            row_id = 0
            high_scores = {}

        player_name = "Player"
        high_scores[player_name] = max(high_scores.get(player_name, 0), trtl.score)
        sorted_items = sorted(high_scores.items(), key=lambda x: x[1], reverse=True)[:10]
        new_scores = dict(sorted_items)
        if row_id == 0:
            db.add(new_scores)
        else:
            db.update(new_scores)

    pygame.quit()


if __name__ == "__main__":
    main()
