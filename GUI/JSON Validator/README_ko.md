# GUI JSON 유효성 검사기

## 설명

GUI JSON 유효성 검사기는 그래픽 사용자 인터페이스를 사용하여 JSON 문자열의 유효성을 검사할 수 있는 간단한 도구입니다. JSON 렉서 및 파서와 사용자 상호 작용을 위한 그래픽 인터페이스의 두 가지 구성 요소로 구성됩니다.

## 스크린샷

**유효한 JSON 스크린샷**\
[![Valid-JSON.png](https://i.postimg.cc/y8ngKCYZ/Valid-JSON.png)](https://postimg.cc/qNhMcYKJ)

**잘못된 JSON 스크린샷**\
[![Invalid-JSON.png](https://i.postimg.cc/9fM4FgrN/Invalid-JSON.png)](https://postimg.cc/XrRNs8Kw)

## 사용 방법

1.  **JSON 렉서 및 파서:**
    *   `json_parser` 모듈은 JSON 렉서 및 파서를 제공합니다.
    *   프로그래밍 방식의 JSON 유효성 검사에 독립적으로 사용할 수 있습니다.

2.  **GUI JSON 유효성 검사기:**
    *   `JSONValidator` 클래스는 JSON 유효성 검사를 위한 그래픽 사용자 인터페이스를 제공합니다.
    *   GUI를 시작하려면 제공된 스크립트에서 `JSONValidator` 클래스를 실행하십시오.
    *   텍스트 상자에 JSON 문자열을 입력하고 "유효성 검사" 버튼을 클릭합니다.
    *   결과는 정보 레이블에 표시됩니다.

## 종속성

*   JSON 구문 분석에는 `json_parser` 모듈이 필요합니다.
