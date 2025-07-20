# 다중 프로세스를 위한 Python 로깅 도우미

## 설명
이것은 Python 개발자가 여러 프로세스에서 단일 로그 파일에 쉽게 로그를 기록할 수 있도록 하는 도우미 클래스입니다.

## 예제
다음은 두 가지 모드를 제공하는 **main.py**의 예제 코드 스니펫입니다.

1. 멀티프로세싱 풀에서 실행:
```python
python3 main.py --is_pool yes
```

1. 일반 멀티프로세싱에서 실행:
```python
python3 main.py --is_pool no
```

로그 파일은 로그 디렉토리에 생성되며 이름은 mulp.log입니다.

* 로그 파일 내용
```
06-17 13:41:13 | sub | INFO | /projects/OTHERS/MultiprocessingLogger/main.py:19 | 26802 | c
06-17 13:41:13 | sub | INFO | /projects/OTHERS/MultiprocessingLogger/main.py:19 | 26803 | d
06-17 13:41:13 | sub | INFO | /projects/OTHERS/MultiprocessingLogger/main.py:19 | 26799 | a
06-17 13:41:13 | sub | INFO | /projects/OTHERS/MultiprocessingLogger/main.py:19 | 26804 | e
06-17 13:41:13 | sub | INFO | /projects/OTHERS/MultiprocessingLogger/main.py:19 | 26801 | b
```
