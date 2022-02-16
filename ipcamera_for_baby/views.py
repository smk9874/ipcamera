from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import StreamingHttpResponse
from django.db.models import Q
import requests
import time

from .models import User, AlarmSetting


def index(request):

    return render(request, 'ipcamera_for_baby/video_feed.html')

def index_mac(request, mac_addr):

    #1. find mac_addr from userlist
    user = User.objects.filter(Q(mac_address=mac_addr))

    if request.method == 'GET':

        count = user.count()
        if count == 0:
            print('create user')
            new_user = User(mac_address=mac_addr)
            new_user.save()

            alarm_setting = AlarmSetting(user=new_user)
            alarm_setting.save()

        else:
            print('This mac address is registered already', user)

    elif request.method == 'POST':

        user = User.objects.get(mac_address=mac_addr)
 
        #2. get and save checkbox value to db
        alarm = AlarmSetting.objects.get(user=user.id)
        check_status = request.POST.getlist('alarms')
        print('check_status=', check_status)
        if 'motion' in check_status:
            alarm.motion_alarm = True
        else:
            alarm.motion_alarm = False
        if 'sound' in check_status:
            alarm.sound_alarm = True
        else:
            alarm.sound_alarm = False
        alarm.save()       

    #2. show user's alarm settings to web page
    user = User.objects.get(mac_address=mac_addr)
    alarm = AlarmSetting.objects.get(user=user.id)

    context = {
                'user_id': user.id,
                'motion_alarm': alarm.motion_alarm,
                'sound_alarm': alarm.sound_alarm,
               }

    return render(request, 'ipcamera_for_baby/video_feed.html', context)

def set_alarm(request, mac_addr, user_id):

    print('called set_alarm')

    #1. find user id from db
    if User.objects.all():
        user = User.objects.get(id=user_id) 
        print(user)

        #2. get and save checkbox value to db
        alarm = AlarmSetting.objects.get(user=user.id)
        check_status = request.POST.getlist('alarms')
        print('check_status=', check_status)
        if 'motion' in check_status:
            alarm.motion_alarm = True
        else:
            alarm.motion_alarm = False
        if 'sound' in check_status:
            alarm.sound_alarm = True
        else:
            alarm.sound_alarm = False
        alarm.save()
    else:
        print('cannot find user id ', user_id)

    context = {
                'user_id': user.id,
                'motion_alarm': alarm.motion_alarm,
                'sound_alarm': alarm.sound_alarm,
               }

    return index_mac(request, mac_addr)
#    return render(request, 'ipcamera_for_baby/video_feed.html', context)

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

    url = 'http://localhost:8765/picture/1/current'
    response = requests.get(url)
#    status = response.status_code
#    text = response.text

    print('response=', response)

    return response
#    return bytes(response.text, 'utf-8')

def recv_mac_addr(request, mac_addr):

    print('recv_mac_addr', mac_addr)

    #1. find mac_addr from userlist
    filter_result = User.objects.filter(Q(mac_address=mac_addr)).count()

    if filter_result == 0:
        print('create user')
        user = User(mac_address=mac_addr, name='')
        user.save()
    else:
        print('This mac address is registered already')
        
    return HttpResponse('HttpResponse!!')
