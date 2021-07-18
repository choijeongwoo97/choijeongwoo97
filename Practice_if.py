#if문

a = 10

if a < 5:
    print("야호")

else: #else문이 없으면 조건이 맞지않을 때 아무것도 하지말아라
    print("틀림")

title = "삼성전자 오늘 오를까요?"
if "삼성전자" in title:
    print("나한테 이메일을 보낸다.")
elif "내일" in title: #조건식끼리 조건이 겹치면 안된다.
        print("나한테 이메일을 보낸다. 222")
else:
    print("무시한다.")
    
