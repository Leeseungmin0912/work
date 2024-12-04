import datetime
import requests


#웹 후크(web hook)할 때 복사한 url을 붙여넣어 줍니다.
discord_url = '복사한 url'

#디스코드 채널로 메세지 전송
def discord_send_message(text):
    now = datetime.datetime.now()
    message = {"content": f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {str(text)}"}
    requests.post(discord_url, data=message)
    print(message)
    
    
for i in range(0,10):
    discord_send_message(f"{i} 테스트 입니다.")