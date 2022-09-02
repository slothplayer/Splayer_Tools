import asyncio
from websockets import serve

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def temp():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

def main():
    asyncio.run(temp())

if __name__ == '__main__':
    main()