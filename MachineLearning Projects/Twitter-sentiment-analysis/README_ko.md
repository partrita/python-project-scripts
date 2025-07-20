## 시작하기

Tweepy:
Tweepy는 공식 트위터 API를 위한 파이썬 클라이언트입니다. 다음 pip 명령을 사용하여 설치하십시오.

```bash
            pip install tweepy
```

TextBlob: textblob은 텍스트 데이터를 처리하기 위한 파이썬 라이브러리입니다. 다음 pip 명령을 사용하여 설치하십시오.

```bash
            pip install textblob
```

다음 명령을 사용하여 일부 NLTK 코퍼스를 설치하십시오.

```bash
            python -m textblob.download_corpora
```
## 인증:
트위터 API를 통해 트윗을 가져오려면 트위터 계정을 통해 앱을 등록해야 합니다. 동일한 작업을 위해 다음 단계를 따르십시오.

1. developer.twitter.com/apps를 열고 '새 앱 만들기' 버튼을 클릭합니다.
2. 애플리케이션 세부 정보를 입력합니다. 콜백 URL 필드는 비워 둘 수 있습니다.
3. 앱이 생성되면 앱 페이지로 리디렉션됩니다.
4. '키 및 액세스 토큰' 탭을 엽니다.
5. '소비자 키', '소비자 비밀', '액세스 토큰' 및 '액세스 토큰 비밀'을 복사합니다.
