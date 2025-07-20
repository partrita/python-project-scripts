# 가상 마우스

가상 마우스는 사용자가 실제 마우스를 사용하지 않고도 시스템에 마우스 입력을 제공할 수 있도록 하는 소프트웨어입니다. 극단적으로는 일반 웹 카메라를 사용하기 때문에 하드웨어라고도 할 수 있습니다. 가상 마우스는 일반적으로 실제 마우스나 컴퓨터 키보드를 포함할 수 있는 여러 입력 장치로 작동할 수 있습니다. 웹 카메라를 사용하는 가상 마우스는 다양한 이미지 처리 기술의 도움으로 작동합니다.

# 프로젝트 데모 작동 여기 드라이브 링크가 있습니다.
# 이제 드라이브 링크에 액세스하여 단계와 작동 방식을 확인할 수 있습니다.

https://drive.google.com/drive/folders/1hq7jWKDqc4YjFsHC1KeHgGvzJGXp8lzK?usp=sharing



# 설정 및 실행 방법

  ### 사전 요구 사항

  Python: (3.6 - 3.8.5)<br>
  Anaconda 배포판: 다운로드하려면 [여기](https://www.anaconda.com/products/individual)를 클릭하십시오.

  프로젝트 폴더 이름 Virtual-Mouse를 다운로드하고 압축을 풉니다.<br>

  그런 다음 비디오에 표시된 대로 VsCode에서 Virtual-Mouse 폴더를 엽니다.

  1단계:
  ```bash
  conda create --name gest python=3.8.5
  ```

  2단계:
  ```bash
  conda activate gest
  ```

  3단계:
  ```bash
  pip install -r requirements.txt
  ```

  4단계:
  cd src를 사용하여 src로 cd합니다.
  ```bash
  python Virtual_Mouse.py
  ```
