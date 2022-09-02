import asyncio
from websockets import connect

async def hello(uri):
    async with connect(uri) as websocket:
        await websocket.send("Hello world!")
        temp = await websocket.recv()
        print(temp)

def main():
    asyncio.run(hello("ws://localhost:8765"))

if __name__ == '__main__':
    main()