log_callback = None

def set_logger(callback):
    global log_callback
    log_callback = callback

def _log(msg):
    if log_callback:
        log_callback(msg)
    else:
        print(msg)


def drive(x, y):
    """
    x: 좌우 조향 (-1.0 ~ 1.0)
    y: 전후 스로틀 (-1.0 ~ 1.0)
    """

    if abs(x) < 0.05:
        x = 0
    if abs(y) < 0.05:
        y = 0

    # 서보 각도 (0~180도, 90이 중앙)
    steering_angle = int(90 + x * 45)  # 좌우 ±45도
    _log(f"[서보] 조향 각도 설정 → {steering_angle}도 (x={x:.2f})")

    # 모터 스로틀 (0~180, 90이 중립)
    throttle = int(90 + y * 45)  # 전진/후진
    _log(f"[모터] 스로틀 설정 → {throttle} (y={y:.2f})")

def stop():
    _log("[STOP] 서보=90도 (직진), 모터=90 (중립)")

