'''
    클래스명: Car
    인스턴스 변수
        company
        model
        color
    인스턴스 메소드
        carInfo()
            회사명: 현대자동차
            모델명: 펠리세이드
            색상: 화이트
'''

class Car:
    def __init__(self, company, model, color):
        self.company = company
        self.model = model
        self.color = color

    # def carInfo(self):
    #     print(f'회사명: {self.company}')
    #     print(f'모델명: {self.model}')
    #     print(f'색상: {self.color}')

    def __str__(self):
        return f'''회사명: {self.company}
모델명: {self.model}
색상: {self.color}
'''
