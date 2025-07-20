# 굵게, 밑줄, 기울임꼴 텍스트에 대한 `.docx` 파일 분석
이 프로그램은 워드 문서에서 모든 굵게, 밑줄, 기울임꼴 텍스트를 찾는 데 도움이 됩니다.

먼저 새 폴더를 만든 다음 그 안에 `extract.py`라는 파일을 만들고 코드를 복사하여 붙여넣습니다.
그런 다음 `python-docx`를 설치해야 합니다.
```bash
$ pip install python-docx
```
예를 들어 `process_design_notes.docx`와 같은 워드 문서를 현재 작업 디렉토리(CWD)에 복사합니다.

이제 CWD에는 **extract.py** 및 **process_design_notes.docx**라는 두 개의 파일이 있어야 합니다.

CWD에서 터미널 또는 명령 프롬프트를 열고 다음을 입력합니다.
```bash
#리눅스용
python3 extract.py process_design_notes.docx
#윈도우용
python extract.py process_design_notes.docx
```
위의 명령을 입력하면 프로그램이 워드 문서에서 실행되고 추출된 굵게, 기울임꼴, 밑줄 친 단어를 추가합니다.
