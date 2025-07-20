# Python을 사용하여 이 KeyLogger 코드 실행하기

### **'pynput'을 설치해야 합니다.**

#### 'pynput' 설치 단계



**먼저 IDE에서 가상 환경을 만들고 주어진 명령을 사용하여 설정하십시오.**

##### macOS
```
python3 -m venv .venv
source .venv/bin/activate
```


##### Linux

```
sudo apt-get install python3-venv    #필요한 경우
python3 -m venv .venv
source .venv/bin/activate
```

##### Windows
```
py -3 -m venv .venv
.venv\scripts\activate
```

가상 환경에서 이 명령을 사용하여 pynput을 설치하십시오.

```
pip install pynput
```


-------
**이제 IDE에서 이것을 실행할 수 있습니다.**

###### **키 로그는 'log.txt' 파일에 저장됩니다.**
