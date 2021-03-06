import requests
import datetime
import jandiurl

today = datetime.date.today()
wolgeupnal = datetime.date(1, 1, 1)
if today.day <= 26:
    wolgeupnal = datetime.date(today.year, today.month, 26)
else:
    if today.month < 12:
        wolgeupnal = datetime.date(today.year, today.month + 1, 26)
    else:
        wolgeupnal = datetime.date(today.year + 1, 1, 26)

headers = {'Accept': 'application/vnd.tosslab.jandi-v2+json',
           'Content-Type': 'application/json; charset=utf-8'}
data = '''
{
    "body" : "퇴근하세요!",
    "connectColor" : "#e91e63",
    "connectInfo": [{
        "title" : "월급날까지",
        "description" : "**%d**일 남았습니다."
    }]
}
''' % (wolgeupnal - today).days

if (wolgeupnal - today).days == 0:
    data = '''
{
    "body" : "퇴근하세요!",
    "connectColor" : "#e91e63",
    "connectInfo": [{
        "title" : "월급날",
        "description" : "대신귀\\n여운월\\n급님을\\n드리겠\\n습니다"
    }]
}
'''

r = requests.post(jandiurl.url, data=data.encode('utf-8'), headers=headers)
