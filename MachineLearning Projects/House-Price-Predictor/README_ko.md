# 주택 가격/임대료 예측 웹사이트

사람들은 주택을 구매하거나 임대할 때 일반적으로 가격 범위를 알고 싶어합니다.

그래서 이 목적을 위해 우리는 사람들이 3BHK, 기차역 등과 같은 요구 사항에 따라 지불해야 할 대략적인 가격을 알 수 있도록 이 웹사이트를 만들었습니다.

이 웹사이트에는 사용자의 피드백을 위한 SQL 데이터베이스(sqlalchemy)도 있습니다.

## 스크린샷

홈페이지
![home](https://user-images.githubusercontent.com/78130964/149762241-462685ea-0c42-4e45-9699-c5331e1266a4.png)

소개 페이지
![about](https://user-images.githubusercontent.com/78130964/149762317-75833d93-63f3-4240-8b32-9e642e208458.png)

선택 양식
![uiform](https://user-images.githubusercontent.com/78130964/149762396-a1f4ab8d-d74b-4b74-933b-a30c315f1136.png)

주택 가격
![price_main](https://user-images.githubusercontent.com/78130964/149762464-3bdd9b69-0d47-4afd-96a0-7e0a3e541178.png)

임대료
![rent_main](https://user-images.githubusercontent.com/78130964/149762520-3d121b90-47b3-4ca8-878e-ad01efede04a.png)




## 기술 스택

**클라이언트:** HTML, CSS, Bootstrap

**서버:** Flask, Scikit, Sql-Alchemy


## 로컬에서 실행

Python 설치

프로젝트 복제

프로젝트 디렉토리로 이동

```bash
  cd House-Price-Predictor
```

종속성 설치

```bash
  pip install flask
  pip install SQLAlchemy
  pip install scikit-learn
```

서버 시작

```bash
  python main.py
```
