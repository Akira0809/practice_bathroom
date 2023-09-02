from django.shortcuts import render
from .models import usertime
from django.middleware.csrf import get_token
from django.http import JsonResponse, HttpResponse

# Create your views here.

def csrf_token(request):
    return JsonResponse({"token": get_token(request)})

def index(request):
    time_arr = {"16:00": 0, "16:30": 1, "17:00": 2, "17:30": 3, "18:00": 4, "18:30": 5, "19:00": 6, "19:30": 7, "20:00": 8, "20:30": 9, "21:00": 10, "21:30": 11, "22:00": 12, "22:30": 13}
    time_member = []
    time_arr_keys = list(time_arr.keys())
    for i in range(14):
        arr = [i, time_arr_keys[i]]
        for _ in range(2):
            arr.append(0)
        time_member.append(arr)
    my_time = None
    my_bath = None
    users = usertime.objects.all()
    session_id = None
    for user in users:
        if user.username == str(request.user):
            session_id = user.id
            my_time = user.reserve_time
            my_bath = user.bath_type
        time_member[int(user.reserve_time)][int(user.bath_type) + 1] += 1
    if my_time != None:
        my_time = int(my_time)
        my_bath = int(my_bath)
    # 予約済みのユーザー情報を取得
    if request.method == "GET":
        print(time_member)
        return render(request, "index.html", {
            "username": request.user,
            "time_member": time_member,
            "my_time": my_time,
            "my_bath": my_bath
        })
    elif request.method == "POST":
        detail = request.POST["reserve"].split('-')
        username = request.user
        reserve_time = int(time_arr[detail[0]])
        bath_type = int(detail[1])
        allow_req = 0
        if bath_type == 1:
            if time_member[reserve_time][2] >= 4:
                allow_req = -1
        elif bath_type == 2:
            if time_member[reserve_time][3] >= 9:
                allow_req = -1
        if session_id != None:
            user = usertime.objects.get(id = session_id)
            user.reserve_time = reserve_time
            user.bath_type = bath_type
            allow_req = 1
        if allow_req == 0:
            usertime.objects.create(username=username, reserve_time=reserve_time, bath_type=bath_type)
            return HttpResponse("Successful")
        elif allow_req == 1:
            user.save()
            return HttpResponse("Successful")
        else:
            return HttpResponse("Request Failed.\nPlease try again.")

def delete_all(request):
    users = usertime.objects.all()
    for user in users:
        user.delete()
    return HttpResponse("Successful")