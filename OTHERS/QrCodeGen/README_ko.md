파이썬을 사용하여 QR 생성.

필요한 것은 IDE(pycharm)뿐입니다.
pip install qrcode
그리고 [qr.py](https://github.com/larymak/Python-project-Scripts/blob/main/QrCodeGen/qr.py)에 코드를 붙여넣으세요.

이 코드를 사용하면 URL용 QR 코드를 생성할 수 있습니다.
예시:
```python
code = qrcode.make("여기에 URL 붙여넣기")
```

자신만의 메시지를 입력해도 생성됩니다.
예시:
```python
image = qrcode.make(input("메시지를 작성하세요: "))
```

생성된 qrcode는 다음과 같습니다.

![image](https://github.com/larymak/Python-project-Scripts/blob/main/QrCodeGen/clock.jpg)

비디오 링크: https://www.youtube.com/watch?v=QemlQBeIxWI
[![Python을 사용한 QR 코드 생성](http://i3.ytimg.com/vi/QemlQBeIxWI/maxresdefault.jpg)](https://www.youtube.com/watch?v=QemlQBeIxWI)
