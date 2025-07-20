# 이차 방정식 해결사

![image](img.png)

## 요구 사항
```powershell
numpy : 1.24.2
matplotlib : 3.6.3
ttkbootstrap : 1.10.1
tkinter: "내장", 8.6
```

ttkbootstrap을 GUI로 사용하는 간단한 이차 방정식 해결사

- GUI 사용을 용이하게 하기 위해 Quadratic 클래스를 만들었습니다.

## `Quadratic 클래스`
이차 클래스는 ax² + bx + c에 따라 3개의 인수(a, b, c)를 받습니다.
```python
q1 = Quadratic(a = 2, b = 4, c = 5)
```
## 메서드
### solve quad 메서드는 식이 0과 같다고 가정하고 이차 표현식을 풉니다.
 > 두 숫자의 튜플을 반환합니다.
 ```python
 q1 = Quadratic(a = 1, b = 8, c = 16)
 print(q1.solveQuad())

 # 4, 4를 반환합니다.
 ```
 > 판별식이 0보다 작은 경우 복소수 해가 반환됩니다. `python3은 복소수를 지원합니다`

### evaluate 메서드는 ax² + bx + c의 x를 정수 또는 부동 소수점으로 바꾸고 계산된 값을 반환합니다.
 ```python
 q1 = Quadratic(a = 1, b = 8, c = 16)
 print(q1.evaluate(value = 2))

 # 36을 반환합니다.
 ```
### draw figure 메서드는 numpy와 matplotlib를 사용하여 이차 방정식 그래프를 그립니다.
 > `numpy와 matplotlib가 필요합니다` 위의 요구 사항 섹션을 참조하십시오.
 ```python
 q1 = Quadratic(a = 1, b = 8, c = 16)
 print(q1.drawFigure())

 # 4, 4를 반환합니다.
 ```
 > matplotlib 그림이 반환되고 matplotlib 그래프에 추가할 수 있습니다.
