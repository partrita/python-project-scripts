## PyDiff
*동적 프로그래밍* 기반 알고리즘을 사용하여 두 파일을 비교하는 간단한 파이썬 스크립트입니다.

사용법:
```sh
py pydiff.py file1.txt file2.txt
```

출력:
```sh
file1.txt | - 13 | mattis justo quis porta porttitor.
file2.txt | + 13 | Aenean mattis justo quis porta porttitor.
file1.txt | - 10 | Nullam elementum nunc in massa fringilla, sit amet iaculis elit blandit.
file2.txt | + 10 | elementum nunc in massa fringilla, sit amet iaculis elit blandit.
```
