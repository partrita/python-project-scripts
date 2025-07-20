# 운전자 졸음 감지

운전자가 졸음운전을 시작하는 즉시 경고하여 사고를 예방하는 시스템입니다.



## 빠른 시작 🚀

### 저장소 복제

```sh
git clone https://github.com/adityajai25/driver-drowsiness-detection.git
```
그런 다음

```sh
cd driver-drowsiness-detection
```


## 데이터 세트

Kaggle에서 다운로드한 데이터 세트를 사용했습니다.
## 가상 환경 만들기

가상 환경을 사용하면 종속성을 격리하고, 라이브러리 버전을 관리하며, 전역 Python 환경을 깨끗하게 유지하고, 일관된 설정을 보장합니다.

### Windows에서

#### 가상 환경 만들기:

명령 프롬프트를 열고 프로젝트 디렉토리로 이동합니다.

```sh
cd project/directory/

```
가상 환경 만들기:
```sh
python -m venv env
```
가상 환경 활성화:

```sh
.\env\Scripts\activate
```

### mac/Linux에서

#### 가상 환경 만들기:
터미널을 열고 프로젝트 디렉토리로 이동합니다.

```sh
cd project/directory/

```
가상 환경 만들기:
```sh
python -m venv env
```
가상 환경 활성화:

```sh
source env/bin/activate
```


## 필수 패키지 설치

가상 환경이 활성화되면 다음 명령을 사용하여 필수 패키지를 설치합니다.

#### 1. pygame 설치

```sh
pip install pygame==2.4.0
```
#### 2. openCV-Python 설치

```sh
pip install opencv-python==4.6.0.66
```
#### 3. numpy 설치

```sh
pip install numpy==1.23.0
```
#### 4. keras 설치

```sh
pip install keras==2.12.0
```
#### 5. tensorflow 설치

```sh
pip install tensorflow==2.13.0
```


## 실행
필수 패키지를 설치한 후 다음 명령을 사용하여 프로젝트를 실행할 수 있습니다.

```sh
python main.py
```

그러면 응용 프로그램이 시작되고 웹캠을 활성화하고 감지를 시작하는 데 몇 분 정도 걸릴 수 있습니다.
