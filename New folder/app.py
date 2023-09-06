import cv2
import numpy as np
import urllib.request
from flask import Flask, render_template, Response, request

app = Flask(__name__)

# Function to capture frames from an IP camera
def get_frame_from_ip_camera(url):
    while True:
        img_arr = np.array(bytearray(urllib.request.urlopen(url).read()), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Function to capture frames from the system camera
def get_frame_from_system_camera():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        camera_choice = request.form['camera_choice']
        if camera_choice == 'ip':
            return render_template('enter_ip.html')
        elif camera_choice == 'system':
            return render_template('system_camera.html')
        else:
            return "Invalid camera choice"
    return render_template('index.html')

# Route to display the form for entering IP source
@app.route('/video_feed/ip', methods=['GET', 'POST'])
def video_feed_ip():
    if request.method == 'POST':
        ip_source = request.form['ip_source']
        url = f"http://{ip_source}:8080/shot.jpg"
        return Response(get_frame_from_ip_camera(url), mimetype='multipart/x-mixed-replace; boundary=frame')
    return render_template('enter_ip.html')


# Route to display the camera view from system camera
@app.route('/video_feed/system')
def video_feed_system():
    return Response(get_frame_from_system_camera(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
