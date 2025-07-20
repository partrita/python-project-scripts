# 소개

이 Python 프로그램은 특정 웹사이트에서 그래픽 카드에 대한 데이터를 추출하는 웹 스크레이퍼입니다. BeautifulSoup 라이브러리를 사용하여 웹사이트의 HTML 콘텐츠를 구문 분석하고 requests 라이브러리를 사용하여 웹 페이지를 가져옵니다.

## 요구 사항

- Python 3.x
- BeautifulSoup 라이브러리 (`beautifulsoup4`)
- Requests 라이브러리 (`requests`)
- Openpyxl 라이브러리 (`openpyxl`)

pip를 사용하여 필요한 라이브러리를 설치할 수 있습니다.

```
pip install beautifulsoup4 requests openpyxl
```

## 사용 방법

1. 이 저장소를 복제하거나 파일을 다운로드합니다.

2. 터미널 또는 명령 프롬프트를 열고 프로젝트 디렉토리로 이동합니다.

3. Python 스크립트 `app.py`를 실행합니다.

```
app.py
```

4. 프로그램은 웹사이트에서 데이터 스크래핑을 시작하고 각 그래픽 카드의 브랜드, 이름 및 가격을 콘솔에 표시합니다.

5. 스크래핑이 완료되면 프로그램은 데이터를 `Graphics Card.xlsx`라는 Excel 파일에 저장합니다.

## 구성

`app.py` 파일 내의 `scrape_graphics_cards_data()` 함수에서 URL을 수정하여 다른 웹사이트에서 데이터를 스크래핑하거나 필요에 따라 매개변수를 조정할 수 있습니다.

## 출력

프로그램은 스크래핑된 데이터가 포함된 Excel 파일 `Graphics Card.xlsx`를 생성합니다. Excel 파일의 각 행은 그래픽 카드를 나타내며 `Brand`, `Name` 및 `Price` 열을 포함합니다.

## 면책 조항

이 웹 스크레이퍼는 교육 및 정보 제공 목적으로만 제공됩니다. 웹사이트의 서비스 약관 및 스크래핑 정책을 존중하십시오. 웹사이트를 스크래핑하기 전에 항상 적절한 승인을 받고 스크레이퍼를 책임감 있고 윤리적으로 사용하십시오.
