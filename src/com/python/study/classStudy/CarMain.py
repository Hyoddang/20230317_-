from src.com.python.study.classStudy.Car import Car
if __name__ == '__main__':

    carList = list()
    car = Car('현대자동차', '펠리세이드', '화이트')
    # car.carInfo()
    car2 = Car('현대자동차', '쏘나타', '블랙')
    # car2.carInfo()

    carList.append(car)
    carList.append(car2)
    # print(carList)

    for carObj in carList:
        print(carObj)











