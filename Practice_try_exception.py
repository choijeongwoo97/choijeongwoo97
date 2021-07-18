#try, Exeption

try:
    a = 10/0
except ZeroDivisionError:#에러를 발생시키는 코드 뒤에 매우 중요한 코드가 있을 수 있으므로 잘 활용!
    print("에러 발생!")

class Naver:
    def crawl(self):
        print("네이버 크롤링")

class Twitter:
    def crawl(self):
        print("트위터 크롤링")

class Yahoo:
    def crawl(self):
        print("야후 크롤링")

crawl_target_list = {
    Naver(),
    Twitter(),
    Yahoo()
}

result_list = []
for site in crawl_target_list:
    try:
        result = site.crawl()
    except Exception:
        print("오류가 발생했다!")
    else:
        result_list.append(result) #에러가 없을때만 실행

#result_list를 하나로 연겨래서 이메일을 나한테 보낸다.
#이 때, 사이트들 중 하나라도 오류가 발생하면 다음으로 진행이 안된다.
#따라서 try, except를 활용해서 에러를 처리한다.