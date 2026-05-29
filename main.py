import sys
import pygame
import webbrowser

pygame.init()
screen = pygame.display.set_mode((430, 880))

icon = pygame.image.load('img/logo.png')
pygame.display.set_caption("BrightUp GenZ")
pygame.display.set_icon(icon)

home = pygame.image.load('img/home.png')
mucluc = pygame.image.load('img/mucluc.png')
ttth = pygame.image.load('img/Tiến trình thực hiện.png')
full_flashcard = pygame.image.load('img/full flashcard.png')

current_screen = "home"

# ================= HITBOX =================

# HOME
menu_rect_home = pygame.Rect(10, 10, 60, 60)
ttth_rect_home = pygame.Rect(80, 250, 270, 200)
flashcard_rect_home = pygame.Rect(60, 520, 310, 250)

# MỤC LỤC
close_rect_mucluc = pygame.Rect(280, 10, 60, 60)
ttth_rect_mucluc = pygame.Rect(20, 90, 300, 60)
flash_rect_mucluc = pygame.Rect(20, 120, 300, 60)
bot_rect_mucluc = pygame.Rect(20, 180, 300, 60)
news_rect_mucluc = pygame.Rect(20, 200, 300, 60)
support_rect_mucluc = pygame.Rect(20, 860, 300, 60)

# TIẾN TRÌNH
back_rect_ttth = pygame.Rect(10, 10, 60, 60)

# FLASHCARD
back_rect_flash = pygame.Rect(10, 10, 60, 60)

# ================= SCROLL =================

scroll_ttth = 0
scroll_flash = 0
scroll_speed = 30

screen_height = 880

ttth_height = ttth.get_height()
flash_height = full_flashcard.get_height()

min_scroll_ttth = -(ttth_height - screen_height)
min_scroll_flash = -(flash_height - screen_height)

if min_scroll_ttth > 0:
    min_scroll_ttth = 0

if min_scroll_flash > 0:
    min_scroll_flash = 0

# ==========================================

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ===== CLICK =====
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                # ===== HOME =====
                if current_screen == "home":
                    if menu_rect_home.collidepoint(event.pos):
                        current_screen = "mucluc"

                    elif ttth_rect_home.collidepoint(event.pos):
                        current_screen = "ttth"
                        scroll_ttth = 0

                    elif flashcard_rect_home.collidepoint(event.pos):
                        current_screen = "flashcard"
                        scroll_flash = 0

                # ===== MỤC LỤC =====
                elif current_screen == "mucluc":
                    if close_rect_mucluc.collidepoint(event.pos):
                        current_screen = "home"

                    elif ttth_rect_mucluc.collidepoint(event.pos):
                        current_screen = "ttth"
                        scroll_ttth = 0

                    elif flash_rect_mucluc.collidepoint(event.pos):
                        current_screen = "flashcard"
                        scroll_flash = 0

                    elif bot_rect_mucluc.collidepoint(event.pos):
                        webbrowser.open("https://chatgpt.com/g/g-68ebb31724f88191953cf12f08d5d819-brightupgenz")

                    elif news_rect_mucluc.collidepoint(event.pos):
                        webbrowser.open("https://zenodo.org/records/17556640")

                    elif support_rect_mucluc.collidepoint(event.pos):
                        webbrowser.open(
                            "https://mail.google.com/mail/?view=cm&fs=1"
                            "&to=minhquantran4312@gmail.com"
                            "&su=Hỗ trợ BrightUp GenZ"
                            "&body=Xin chào,%0A%0ATôi cần hỗ trợ về:%0A- "
                        )

                # ===== TIẾN TRÌNH =====
                elif current_screen == "ttth":
                    if back_rect_ttth.collidepoint(event.pos):
                        current_screen = "home"

                # ===== FLASHCARD =====
                elif current_screen == "flashcard":
                    if back_rect_flash.collidepoint(event.pos):
                        current_screen = "home"

        # ===== SCROLL =====
        if event.type == pygame.MOUSEWHEEL:

            if current_screen == "ttth":
                scroll_ttth += event.y * scroll_speed

                if scroll_ttth > 0:
                    scroll_ttth = 0
                if scroll_ttth < min_scroll_ttth:
                    scroll_ttth = min_scroll_ttth

            elif current_screen == "flashcard":
                scroll_flash += event.y * scroll_speed

                if scroll_flash > 0:
                    scroll_flash = 0
                if scroll_flash < min_scroll_flash:
                    scroll_flash = min_scroll_flash

    # ===== HIỂN THỊ =====
    if current_screen == "home":
        screen.blit(home, (0, -30))

    elif current_screen == "mucluc":
        screen.blit(mucluc, (0, -30))

    elif current_screen == "ttth":
        screen.blit(ttth, (0, -30 + scroll_ttth))

    elif current_screen == "flashcard":
        screen.blit(full_flashcard, (0, -30 + scroll_flash))

    pygame.display.update()
    clock.tick(60)