class Audio:
    """
    power, volume을 가진 클래스
    power => True False
    volume => 정수

    switch() => 파워의 값을 변경

    tune() => power 켜있으면 음악 재생, 꺼진상태면 power 키라는 메시지
    volume() => volume 값을 변경
    """

    def __init__(self,power=False,volume=0):
        self.power = power
        self.volume = volume

    def switch(self):
        self.power = not (self.power)

    def tune(self):

        if(self.power):
            print("음악을 재생합니다.")
        
        else:
            print("power를 켜주십시오")        

    def set_volume(self, value):

        self.volume = value
        print("volume 값을 {}로 조정했습니다.".format(value))

myaudio = Audio()

myaudio.switch()
myaudio.tune()
myaudio.set_volume(10)