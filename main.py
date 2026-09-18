# This file is used to run the game safely (and needed for github pages)
import asyncio
from src.main import main

if __name__ == "__main__":
    asyncio.run(main())