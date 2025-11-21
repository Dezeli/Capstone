<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Raccoon Car Controller</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/nipplejs/0.9.0/nipplejs.min.js"></script>
  <style>
    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      padding: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: #ffffff;
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
    }

    header {
      width: 100%;
      text-align: center;
      padding: 20px 0;
      background: #ff5e91; /* 분홍 계열 */
      color: white;
      font-size: 22px;
      font-weight: 700;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
      position: relative;
    }

    #log {
      width: calc(100% - 40px);
      height: 500px;
      padding: 12px;
      border-radius: 10px;
      background: #f8f9fa;
      box-shadow: inset 0 2px 6px rgba(0,0,0,0.1);
      font-family: monospace;
      font-size: 13px;
      overflow-y: auto;
      line-height: 1.5;
      border: 1px solid #ddd;
      color: #333;
    }

    #log::-webkit-scrollbar {
      width: 4px;
    }

    #log::-webkit-scrollbar-thumb {
      background: #ff5e91;
      border-radius: 2px;
    }

    #joystick-container {
      flex: 1;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 20px;
    }

    #joystick {
      width: 220px;
      height: 220px;
      border-radius: 50%;
      background: #e0e0e0; /* 흑백 계열 */
      position: relative;
      /* 네오모피즘 스타일 */
      box-shadow: 
        -8px -8px 16px #ffffff,
        8px 8px 16px rgba(0,0,0,0.15);<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Raccoon Car Controller</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/nipplejs/0.9.0/nipplejs.min.js"></script>
  <style>
    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      padding: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: #ffffff;
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
    }

    header {
      width: 100%;
      text-align: center;
      padding: 20px 0;
      background: #ff5e91; /* 분홍 계열 */
      color: white;<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Raccoon Car Controller</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/nipplejs/0.9.0/nipplejs.min.js"></script>
  <style>
    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      padding: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Ve<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Raccoon Car Controller</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/nipplejs/0.9.0/nipplejs.min.js"></script>
  <style>
    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      padding: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: #ffffff;
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
    }

    header {
      width: 100%;
      text-align: center;
      padding: 20px 0;
      background: #ff5e91; /* 분홍 계열 */
      color: white;
      font-size: 22px;
      font-weight: 700;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
      position: relative;
    }

    #log {
      width: calc(100% - 40px);
      height: 500px;
      padding: 12px;
      border-radius: 10px;
      background: #f8f9fa;
      box-shadow: inset 0 2px 6px rgba(0,0,0,0.1);
      font-family: monospace;
      font-size: 13px;
      overflow-y: auto;
      line-height: 1.5;
      border: 1px solid #ddd;
      color: #333;
    }

    #log::-webkit-scrollbar {
      width: 4px;
    }

    #log::-webkit-scrollbar-thumb {
      background: #ff5e91;
      border-radius: 2px;
    }

    #joystick-container {
      flex: 1;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 20px;
    }

    #joystick {
      width: 220px;
      height: 220px;
      border-radius: 50%;
      background: #e0e0e0; /* 흑백 계열 */
      position: relative;
      /* 네오모피즘 스타일 */
      box-shadow: 
        -8px -8px 16px #ffffff,
        8px 8px 16px rgba(0,0,0,0.15);
      border: 2px solid #ccc;
    }

    /* 연결 상태 표시 (우측 상단 작은 점) */
    .status-indicator {
      position: absolute;
      top: 10px;
      right: 20px;
      width: 12px;
      height: 12px;<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Raccoon Car Controller</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/nipplejs/0.9.0/nipplejs.min.js"></script>
  <style>
    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      padding: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: #ffffff;
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
    }

    header {
      width: 100%;
      text-align: center;
      padding: 20px 0;
      background: #ff5e91; /* 분홍 계열 */
      color: white;
      font-size: 22px;
      font-weight: 700;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
      position: relative;
    }

    #log {
      width: calc(100% - 40px);
      height: 500px;
      padding: 12px;
      border-radius: 10px;
      background: #f8f9fa;
      box-shadow: inset 0 2px 6px rgba(0,0,0,0.1);
      font-family: monospace;
      font-size: 13px;
      overflow-y: auto;
      line-height: 1.5;
      border: 1px solid #ddd;
      color: #333;
    }

    #log::-webkit-scrollbar {
      width: 4px;
    }

    #log::-webkit-scrollbar-thumb {
      background: #ff5e91;
      border-radius: 2px;
    }

    #joystick-container {
      flex: 1;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 20px;
    }

    #joystick {
      width: 220px;
      height: 220px;
      border-radius: 50%;
      background: #e0e0e0; /* 흑백 계열 */
      position: relative;
      /* 네오모피즘 스타일 */
      box-shadow: 
        -8px -8px 16px #ffffff,
        8px 8px 16px rgba(0,0,0,0.15);
      border: 2px solid #ccc;
    }

    /* 연결 상태 표시 (우측 상단 작은 점) */
    .status-indicator {
      position: absolute;
      top: 10px;
      right: 20px;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: #28a745;
      box-shadow: 0 0 10px rgba(40, 167, 69, 0.5);
      animation: pulse 2s infinite;
    }

    .status-indicator.disconnected {
      background: #dc3545;
      box-shadow: 0 0 12px rgba(220, 53, 69, 0.6);
    }

    @keyframes pulse {
      0% { opacity: 1; }
      50% { opacity: 0.5; }
      100% { opacity: 1; }
    }

    /* 모바일 최적화 */
    @media (max-height: 600px) {
      #joystick {
        width: 180px;
        height: 180px;
      }
      #log {
        height: 140px;
        margin: 15px;
      }
    }
  </style>
</head>
<body>
  <header>
    Raccoon Car Controller
    <div class="status-indicator" id="status"></div>
  </header>

  <div id="log"></div>

  <div id="joystick-container">
    <div id="joystick"></div>
  </div>

  <script>
    const logBox = document.getElementById("log");
    const statusIndicator = document.getElementById("status");
    
    function addLog(msg) {
      logBox.innerHTML += msg + "<br>";
      logBox.scrollTop = logBox.scrollHeight;
    }

    const socket = new WebSocket("ws://" + window.location.hostname + ":8000/ws/joystick");

    socket.onopen = () => {
      addLog("✅ 서버 연결됨");
      statusIndicator.classList.remove('disconnected');
    };
    
    socket.onclose = () => {
      addLog("❌ 서버 연결 끊김");
      statusIndicator.classList.add('disconnected');
    };
    
    socket.onmessage = (event) => addLog(event.data);

    const joystick = nipplejs.create({
      zone: document.getElementById('joystick'),
      mode: 'static',
      position: { left: '50%', top: '50%' },
      color: '#111', /* 핸들 색상 → 더 진한 블랙 */
      size: 180
    });

    joystick.on('move', (evt, data) => {
      let x = data.vector.x.toFixed(2);
      let y = data.vector.y.toFixed(2);
      socket.send(JSON.stringify({x, y}));
    });

    joystick.on('end', () => {
      socket.send(JSON.stringify({x:0, y:0}));
    });
  </script>
</body>
</html>
      border-radius: 50%;
      background: #28a745;
      box-shadow: 0 0 10px rgba(40, 167, 69, 0.5);
      animation: pulse 2s infinite;
    }

    .status-indicator.disconnected {
      background: #dc3545;
      box-shadow: 0 0 12px rgba(220, 53, 69, 0.6);
    }

    @keyframes pulse {
      0% { opacity: 1; }
      50% { opacity: 0.5; }
      100% { opacity: 1; }
    }

    /* 모바일 최적화 */
    @media (max-height: 600px) {
      #joystick {
        width: 180px;
        height: 180px;
      }
      #log {
        height: 140px;
        margin: 15px;
      }
    }
  </style>
</head>
<body>
  <header>
    Raccoon Car Controller
    <div class="status-indicator" id="status"></div>
  </header>

  <div id="log"></div>

  <div id="joystick-container">
    <div id="joystick"></div>
  </div>

  <script>
    const logBox = document.getElementById("log");
    const statusIndicator = document.getElementById("status");
    
    function addLog(msg) {
      logBox.innerHTML += msg + "<br>";
      logBox.scrollTop = logBox.scrollHeight;
    }

    const socket = new WebSocket("ws://" + window.location.hostname + ":8000/ws/joystick");

    socket.onopen = () => {
      addLog("✅ 서버 연결됨");
      statusIndicator.classList.remove('disconnected');
    };
    
    socket.onclose = () => {
      addLog("❌ 서버 연결 끊김");
      statusIndicator.classList.add('disconnected');
    };
    
    socket.onmessage = (event) => addLog(event.data);

    const joystick = nipplejs.create({
      zone: document.getElementById('joystick'),
      mode: 'static',
      position: { left: '50%', top: '50%' },
      color: '#111', /* 핸들 색상 → 더 진한 블랙 */
      size: 180
    });

    joystick.on('move', (evt, data) => {
      let x = data.vector.x.toFixed(2);
      let y = data.vector.y.toFixed(2);
      socket.send(JSON.stringify({x, y}));
    });

    joystick.on('end', () => {
      socket.send(JSON.stringify({x:0, y:0}));
    });
  </script>
</body>
</html>rdana, sans-serif;
      background: #ffffff;
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
    }

    header {
      width: 100%;
      text-align: center;
      padding: 20px 0;
      background: #ff5e91; /* 분홍 계열 */
      color: white;
      font-size: 22px;
      font-weight: 700;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
      position: relative;
    }

    #log {
      width: calc(100% - 40px);
      height: 500px;
      padding: 12px;
      border-radius: 10px;
      background: #f8f9fa;
      box-shadow: inset 0 2px 6px rgba(0,0,0,0.1);
      font-family: monospace;
      font-size: 13px;
      overflow-y: auto;
      line-height: 1.5;
      border: 1px solid #ddd;
      color: #333;
    }

    #log::-webkit-scrollbar {
      width: 4px;
    }

    #log::-webkit-scrollbar-thumb {
      background: #ff5e91;
      border-radius: 2px;
    }

    #joystick-container {
      flex: 1;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 20px;
    }

    #joystick {
      width: 220px;
      height: 220px;
      border-radius: 50%;
      background: #e0e0e0; /* 흑백 계열 */
      position: relative;
      /* 네오모피즘 스타일 */
      box-shadow: 
        -8px -8px 16px #ffffff,
        8px 8px 16px rgba(0,0,0,0.15);
      border: 2px solid #ccc;
    }

    /* 연결 상태 표시 (우측 상단 작은 점) */
    .status-indicator {
      position: absolute;
      top: 10px;
      right: 20px;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: #28a745;
      box-shadow: 0 0 10px rgba(40, 167, 69, 0.5);
      animation: pulse 2s infinite;
    }

    .status-indicator.disconnected {
      background: #dc3545;
      box-shadow: 0 0 12px rgba(220, 53, 69, 0.6);
    }

    @keyframes pulse {
      0% { opacity: 1; }
      50% { opacity: 0.5; }
      100% { opacity: 1; }
    }

    /* 모바일 최적화 */
    @media (max-height: 600px) {
      #joystick {
        width: 180px;
        height: 180px;
      }
      #log {
        height: 140px;
        margin: 15px;
      }
    }
  </style>
</head>
<body>
  <header>
    Raccoon Car Controller
    <div class="status-indicator" id="status"></div>
  </header>

  <div id="log"></div>

  <div id="joystick-container">
    <div id="joystick"></div>
  </div>

  <script>
    const logBox = document.getElementById("log");
    const statusIndicator = document.getElementById("status");
    
    function addLog(msg) {
      logBox.innerHTML += msg + "<br>";
      logBox.scrollTop = logBox.scrollHeight;
    }

    const socket = new WebSocket("ws://" + window.location.hostname + ":8000/ws/joystick");

    socket.onopen = () => {
      addLog("✅ 서버 연결됨");
      statusIndicator.classList.remove('disconnected');
    };
    
    socket.onclose = () => {
      addLog("❌ 서버 연결 끊김");
      statusIndicator.classList.add('disconnected');
    };
    
    socket.onmessage = (event) => addLog(event.data);

    const joystick = nipplejs.create({
      zone: document.getElementById('joystick'),
      mode: 'static',
      position: { left: '50%', top: '50%' },
      color: '#111', /* 핸들 색상 → 더 진한 블랙 */
      size: 180
    });

    joystick.on('move', (evt, data) => {
      let x = data.vector.x.toFixed(2);
      let y = data.vector.y.toFixed(2);
      socket.send(JSON.stringify({x, y}));
    });

    joystick.on('end', () => {
      socket.send(JSON.stringify({x:0, y:0}));
    });
  </script>
</body>
</html>
      font-size: 22px;
      font-weight: 700;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
      position: relative;
    }

    #log {
      width: calc(100% - 40px);
      height: 500px;
      padding: 12px;
      border-radius: 10px;
      background: #f8f9fa;
      box-shadow: inset 0 2px 6px rgba(0,0,0,0.1);
      font-family: monospace;
      font-size: 13px;
      overflow-y: auto;
      line-height: 1.5;
      border: 1px solid #ddd;
      color: #333;
    }

    #log::-webkit-scrollbar {
      width: 4px;
    }

    #log::-webkit-scrollbar-thumb {
      background: #ff5e91;
      border-radius: 2px;
    }

    #joystick-container {
      flex: 1;
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 20px;
    }

    #joystick {
      width: 220px;
      height: 220px;
      border-radius: 50%;
      background: #e0e0e0; /* 흑백 계열 */
      position: relative;
      /* 네오모피즘 스타일 */
      box-shadow: 
        -8px -8px 16px #ffffff,
        8px 8px 16px rgba(0,0,0,0.15);
      border: 2px solid #ccc;
    }

    /* 연결 상태 표시 (우측 상단 작은 점) */
    .status-indicator {
      position: absolute;
      top: 10px;
      right: 20px;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: #28a745;
      box-shadow: 0 0 10px rgba(40, 167, 69, 0.5);
      animation: pulse 2s infinite;
    }

    .status-indicator.disconnected {
      background: #dc3545;
      box-shadow: 0 0 12px rgba(220, 53, 69, 0.6);
    }

    @keyframes pulse {
      0% { opacity: 1; }
      50% { opacity: 0.5; }
      100% { opacity: 1; }
    }

    /* 모바일 최적화 */
    @media (max-height: 600px) {
      #joystick {
        width: 180px;
        height: 180px;
      }
      #log {
        height: 140px;
        margin: 15px;
      }
    }
  </style>
</head>
<body>
  <header>
    Raccoon Car Controller
    <div class="status-indicator" id="status"></div>
  </header>

  <div id="log"></div>

  <div id="joystick-container">
    <div id="joystick"></div>
  </div>

  <script>
    const logBox = document.getElementById("log");
    const statusIndicator = document.getElementById("status");
    
    function addLog(msg) {
      logBox.innerHTML += msg + "<br>";
      logBox.scrollTop = logBox.scrollHeight;
    }

    const socket = new WebSocket("ws://" + window.location.hostname + ":8000/ws/joystick");

    socket.onopen = () => {
      addLog("✅ 서버 연결됨");
      statusIndicator.classList.remove('disconnected');
    };
    
    socket.onclose = () => {
      addLog("❌ 서버 연결 끊김");
      statusIndicator.classList.add('disconnected');
    };
    
    socket.onmessage = (event) => addLog(event.data);

    const joystick = nipplejs.create({
      zone: document.getElementById('joystick'),
      mode: 'static',
      position: { left: '50%', top: '50%' },
      color: '#111', /* 핸들 색상 → 더 진한 블랙 */
      size: 180
    });

    joystick.on('move', (evt, data) => {
      let x = data.vector.x.toFixed(2);
      let y = data.vector.y.toFixed(2);
      socket.send(JSON.stringify({x, y}));
    });

    joystick.on('end', () => {
      socket.send(JSON.stringify({x:0, y:0}));
    });
  </script>
</body>
</html>
      border: 2px solid #ccc;
    }

    /* 연결 상태 표시 (우측 상단 작은 점) */
    .status-indicator {
      position: absolute;
      top: 10px;
      right: 20px;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: #28a745;
      box-shadow: 0 0 10px rgba(40, 167, 69, 0.5);
      animation: pulse 2s infinite;
    }

    .status-indicator.disconnected {
      background: #dc3545;
      box-shadow: 0 0 12px rgba(220, 53, 69, 0.6);
    }

    @keyframes pulse {
      0% { opacity: 1; }
      50% { opacity: 0.5; }
      100% { opacity: 1; }
    }

    /* 모바일 최적화 */
    @media (max-height: 600px) {
      #joystick {
        width: 180px;
        height: 180px;
      }
      #log {
        height: 140px;
        margin: 15px;
      }
    }
  </style>
</head>
<body>
  <header>
    Raccoon Car Controller
    <div class="status-indicator" id="status"></div>
  </header>

  <div id="log"></div>

  <div id="joystick-container">
    <div id="joystick"></div>
  </div>

  <script>
    const logBox = document.getElementById("log");
    const statusIndicator = document.getElementById("status");
    
    function addLog(msg) {
      logBox.innerHTML += msg + "<br>";
      logBox.scrollTop = logBox.scrollHeight;
    }

    const socket = new WebSocket("ws://" + window.location.hostname + ":8000/ws/joystick");

    socket.onopen = () => {
      addLog("✅ 서버 연결됨");
      statusIndicator.classList.remove('disconnected');
    };
    
    socket.onclose = () => {
      addLog("❌ 서버 연결 끊김");
      statusIndicator.classList.add('disconnected');
    };
    
    socket.onmessage = (event) => addLog(event.data);

    const joystick = nipplejs.create({
      zone: document.getElementById('joystick'),
      mode: 'static',
      position: { left: '50%', top: '50%' },
      color: '#111', /* 핸들 색상 → 더 진한 블랙 */
      size: 180
    });

    joystick.on('move', (evt, data) => {
      let x = data.vector.x.toFixed(2);
      let y = data.vector.y.toFixed(2);
      socket.send(JSON.stringify({x, y}));
    });

    joystick.on('end', () => {
      socket.send(JSON.stringify({x:0, y:0}));
    });
  </script>
</body>
</html>