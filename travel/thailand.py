class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행(야시장 투어) 50만원")

# if안의 내용은 모듈을 직접 실행할 때 동작함
# if문과 __name__ 을 이용해 모듈 자체적으로 테스트가 가능함
        
if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 샐행할 때만 샐행됨")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")