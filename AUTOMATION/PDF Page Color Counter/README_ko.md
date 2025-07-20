<!--이 부분을 제거하지 마십시오-->
![Star Badge](https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)

# PDF 페이지 색상 카운터

## 🛠️ 설명
이 Python 프로젝트는 PDF 문서를 분석하고 흑백 및 컬러 페이지 수를 계산하는 간단하면서도 강력한 도구를 제공합니다. 문서 분석, 품질 관리 작업을 하거나 PDF 파일의 구성에 대해 궁금한 경우 이 코드는 문서의 시각적 특성에 대한 통찰력을 얻는 데 도움이 됩니다.

**주요 특징:**

* 손쉬운 통합: 몇 줄의 코드로 이 기능을 Python 응용 프로그램이나 워크플로에 통합할 수 있습니다.

* PDF 전문 지식: PyMuPDF(MuPDF) 라이브러리를 활용하여 이 프로젝트는 PDF 파일을 효율적으로 처리하므로 광범위한 응용 프로그램에 적합합니다.

* 컬러 페이지 감지: PDF 문서 내에서 컬러 및 흑백 페이지를 정확하게 식별하여 귀중한 통계를 제공합니다.

* 사용 사례: 이 코드는 문서 보관, 인쇄 최적화 또는 콘텐츠 분석과 같은 다양한 시나리오에서 사용할 수 있습니다.

## ⚙️ 사용된 언어 또는 프레임워크
- **Python**: 프로젝트에 사용된 기본 프로그래밍 언어입니다.
- **FastAPI**: Python으로 API를 구축하기 위한 현대적이고 빠른(고성능) 웹 프레임워크입니다.
- **PyMuPDF(MuPDF)**: Python용 경량 및 효율적인 PDF 처리 라이브러리입니다.
- **OpenCV**: 이미지 분석 및 처리에 사용됩니다.
- **Pillow(PIL)**: 이미지 작업을 위한 Python 이미징 라이브러리입니다.

## 🌟 실행 방법
 - ### 모든 요구 사항 설치
    `pip install -r requirements.txt`를 실행하여 모든 요구 사항을 설치합니다.
 - ### 가상 환경 설정

   - 터미널에서 `python -m venv myenv` 명령을 실행합니다.
   - Windows인 경우 `cd myenv/Scripts`로 디렉토리를 변경합니다.
   - `source activate` 명령을 실행하여 가상 환경을 활성화합니다.
   - `cd..`를 사용하여 가상 환경에서 **프로젝트 디렉토리**로 이동합니다.
   - 패키지가 없는 경우 `uvicorn`, `fastapi`, `fitz`, `frontend`, `tools`, `opencv-python`, `pillow`, `python-multipart`, `PyMuPDF`를 설치합니다.
   ```
   pip install uvicorn fastapi fitz frontend tools opencv-python pillow python-multipart PyMuPDF
   ```

- ###  이제 프로젝트를 실행하기만 하면 됩니다.

   -이제 `uvicorn main:app --reload` 명령을 실행합니다.
   -브라우저에서 localhost 링크를 열고 엔드포인트에 `/docs`를 입력하여 fastapi docs UI를 확인합니다.
   ![Screenshot 2023-10-25 134746](https://github.com/Om25091210/Count-Color-Black-Pages-PDF/assets/74484315/2b5b64a2-1c00-4a5a-ab7c-99fb30e7aba6)

   -이제 **POST**를 클릭한 다음 **Try it out**을 클릭합니다.
   -**파일 선택**을 클릭하여 흑백 및 컬러 페이지 수를 계산할 pdf를 선택합니다.
   -**실행**을 클릭합니다.


## 📺 데모
![Screenshot 2023-10-25 133406](https://github.com/Om25091210/Count-Color-Black-Pages-PDF/assets/74484315/a84def7c-7db4-4ab5-bf0b-f8cfe5ded66b)


## 🤖 저자

Github - [OM YADAV](https://github.com/Om25091210)
LinkedIn - [OM YADAV](www.linkedin.com/in/omyadav)
