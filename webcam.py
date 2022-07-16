from flask import Flask, Response
import cv2

# Webcam server
app = Flask(__name__)
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)


def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route("/video_feed")
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# ngrok.exe http 8888
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8888", threaded=True)
