from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
import requests
import time


# Create your views here.
def index(request):

#    print('called index')
#    return render(request, 'ipcamera_for_baby/video_feed.html')

    return render(request, 'ipcamera_for_baby/video_feed.html')

    frame = get_frame_from_motioneye()

    value = HttpResponse(frame, content_type="image/jpeg")
#    print('****', value)
    return value
#    return HttpResponse(frame, content_type="image/jpeg")

def gen():

    testc = 0

    while True:

        # read the frames !!!!
        # frame =
        frame = get_frame_from_motioneye()
        print('type of frame=', type(frame))

        frame = bytes(frame.text, 'utf-8')
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

#        time.sleep(1)
#        yield(HttpResponse(frame, content_type="image/jpeg"))
#        return (HttpResponse(frame, content_type="image/jpeg"))


def for_video_feed(request):


#    return render(request, 'ipcamera_for_baby/video_feed.html')
    
#    while True:

#        frame = get_frame_from_motioneye()
#        frame = bytes(frame.text, 'utf-8')
#        frame = get_frame().tobytes()
#        yield(HttpResponse(frame, content_type="image/jpeg"))
#        return (HttpResponse(frame, content_type="image/jpeg"))

    return StreamingHttpResponse(gen(),
            content_type='multipart/x-mixed-replace; boundary=frame')

def video_feed(request):

    frame = get_frame_from_motioneye()

    return HttpResponse(frame, content_type="image/jpeg")
 
    return StreamingHttpResponse(gen(),
            content_type='multipart/x-mixed-replace; boundary=frame')   

def get_frame_from_motioneye():

    print('called get_streaming_from_motioneye')

    url = 'http://localhost:8765/picture/1/current'
    response = requests.get(url)
#    status = response.status_code
#    text = response.text

    print('response=', response)

    return response
#    return bytes(response.text, 'utf-8')
