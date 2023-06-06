import asyncio
import time


async def count(id: int):
    print(f"{id}: Uno")
    await asyncio.sleep(1)
    print(f"{id}: Dos")


async def main():
    await asyncio.gather(count(1), count(2), count(3))


if __name__ == "__main__":
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {fin - inicio} segundos")

