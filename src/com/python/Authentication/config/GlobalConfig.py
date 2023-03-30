class GlobalConfig:

    loopFlagList = list()

    @classmethod
    def addLoopFlagList(cls):
        cls.loopFlagList.append(True)
        return len(cls.loopFlagList) - 1

    @classmethod
    def stopLoop(cls):
        for index in range(0, len(cls.loopFlagList)):
            cls.loopFlagList[index] = False

    @classmethod
    def initLoopFlag(cls):
        cls.loopFlagList = list()
