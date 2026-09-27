# ==============================================================================
# SPACE SHOOTER ARCADE - WEB RUNNER (PYGBAG / GITHUB PAGES)
# ==============================================================================
# Author      : Muhammed Emin Korkunç (Student ID: 2021221054)
# Institution : Fatih Sultan Mehmet Vakıf Üniversitesi - Bilgisayar Mühendisliği
# GitHub      : https://github.com/muhammedkorkunc
# License     : Proprietary - All Rights Reserved (c) 2026
# ==============================================================================

import asyncio
import sys
import os

# Görseller ve seslerin bulunduğu klasörü yola ekle
sys.path.insert(0, os.path.abspath("pythonProject"))

# Mevcut oyun dosyanızı import edin
try:
    import Oyun2 as game
except ImportError:
    try:
        import FOR as game
    except ImportError:
        pass

async def main():
    # Eğer Oyun2.py doğrudan çalıştırılabilir durumdaysa
    # Standart Pygame döngüsünü webasync ile sürdürür
    if hasattr(game, "main"):
        await game.main()
    else:
        # Kodun içindeki while döngüsünün WebAssembly üzerinde akıcı çalışmasını sağlar
        while True:
            await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())
