import asyncio
import json
import serial
from fastapi import FastAPI, WebSocket
from fastapi.responses import FilleResponse
from fastapi.staticfiles import StaticFiles
from starlette.websockets import WebSocketDisconnect

arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
print("Arduino connectsd")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.websocket("/ws/joystick")
async def joystick_endpoint(websocket.receive_text()
    await websocket.accept()
    await websocket.send_text("app joystick connect")

    try:
        while True:
            data = await websocket.receive_text()
            payload = json.loads(data)
            x = float(payload.get("x", 0))
	    y = float(payload.get("y", 0))

            cmd = ca;c_command(x, y)
            if cmd:
                arduino.write(cmd.encode())
                await websocket.send_text(f"Send a command: {cmd}")
    except WebSocketDisconnect:
        arduino.write(b'S')
        print("joystick connect finish, Moter stop")

def calc_command(x, y):
    if abs(x) < 0.2 and abs(y) < 0.2:
        return 'S'

    if y > 0.4:
        if abs(x) < 0.3:
            return 'F'
        elif x > 0.3:
            return 'R'
        elif x < -0.3:
            return 'L'
    elif y < -0.4:
        return 'B'

    return 'S'

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
