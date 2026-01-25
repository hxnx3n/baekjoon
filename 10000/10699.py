from datetime import datetime, timedelta

now_utc = datetime.utcnow()

kst = now_utc + timedelta(hours=9)

print(kst.strftime("%Y-%m-%d"))
