from django.shortcuts import render
from .models import usertime

# Create your views here.
def index(request):
    # 予約済みのユーザー情報を取得
    if request.method == "GET":
        time_member = []
        time_arr = {"16:00": 0, "16:30": 1, "17:00": 2, "17:30": 3, "18:00": 4, "18:30": 5, "19:00": 6, "19:30": 7, "20:00": 8, "20:30": 9, "21:00": 10, "21:30": 11, "22:00": 12, "22:30": 13}
        time_arr_keys = list(time_arr.keys())
        for i in range(14):
            arr = [time_arr_keys[i]]
            for _ in range(2):
                arr.append(0)
            time_member.append(arr)
        users = usertime.objects.all()
        for user in users:
            time_member[time_arr[user.reserve_time]][user.bath_type] += 1
        print(request.user)
        return render(request, "index.html", {
            "username": request.user,
            "time_member": time_member
        })
#    elif request.method == "POST":
#        username
#        name
#        reserve_time
#        bath_type
#        usertime.objects.create(username=username, name=name, reserve_time=reserve_time, bath_type=bath_type)
