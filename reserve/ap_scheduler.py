from datetime import datetime, date
from apscheduler.schedulers.background import BackgroundScheduler
from models import usertime


def delete_reservation():# 任意の関数名
    # ここに定期実行したい処理を記述する
    reserve = usertime.objects.all()
    reserve.delete()

def start():
  scheduler = BackgroundScheduler()
  scheduler.add_job(delete_reservation, 'cron', hour=0, minute=0)# 毎日0時0分に実行
  scheduler.start()