from flask import Flask,redirect,url_for,render_template,request,Response
import cv2 

app=Flask(__name__)
camera = cv2.VideoCapture(0)

def cctc_live():
    while True:
        success,frame = camera.read()
        if not success:
            break
        else:
            ret,buffer = cv2.imencode('.jpg',frame)
            frame = buffer.tobytes()

            yield(b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n'+ frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(cctc_live(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)