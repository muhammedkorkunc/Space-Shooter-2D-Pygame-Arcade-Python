import asyncio
import os
import sys
import pygame

# Varlık yollarını ayarla
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Oyun modülünü başlat
try:
    import Oyun2 as game_app
except ImportError:
    import FOR as game_app

async def main():
    pygame.init()
    if hasattr(game_app, "main"):
        await game_app.main()
    else:
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            await asyncio.sleep(0)
            clock.tick(60)

if __name__ == "__main__":
    asyncio.run(main())
