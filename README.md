# Fairy_Tale

## Overview
동화 내용을 기반으로 프리 트레인된 Kcbert-beomi 모델을 호출해 korquad 1.0 규격에 맞춰 가공한 동화책 데이터를 기반으로 학습을 진행한 후, Flask로 질의응답 기능을 제공하는 웹 애플리케이션을 구동시키는 프로젝트.

## Tech Stack
- Language: Python 3.9 이상
- Framework: Flask 3.x
- ORM: SQLAlchemy, Flask-SQLAlchemy
- Form: WTForms, Flask-WTF
- DB: MySQL (mysql-connector-python, pymysql)
- Template: Jinja2
- Etc.: email_validator, blinker 등 

## Description
- 웹 서비스용 Python 프로젝트로, 동화 추천·생성 및 관련 기능 구현
- Flask 기반 구조 분리: 비즈니스 로직, 데이터 모델, 라우팅, 뷰 등 모듈화
- 실험 및 데이터 처리, 모델 학습 등은 Jupyter Notebook 파일로 별도 관리

## Directory
- `/src/` : 서비스 주요 소스코드  
  - `/lib/`      : 서비스 로직 및 공통 유틸  
  - `/models/`   : 데이터 및 ML 모델 클래스  
  - `/resources/`: 리소스(데이터, 설정 등)  
  - `/routes/`   : Flask 라우팅 처리  
  - `/utils/`    : 공통 유틸리티 함수  
  - `/views/`    : 템플릿/뷰 함수  
  - `app.py`     : Flask 애플리케이션 엔트리포인트  
  - `run.py`     : 실행 스크립트

- `전처리 코드.ipynb`   : 데이터 전처리/분석 Jupyter Notebook  
- `학습 코드.ipynb`     : 모델 학습/실험 Jupyter Notebook

## Installation & Usage
1. Python 3.9 이상 필요  
2. 의존성 설치
3. 기타 학습 환경에서 ./datasets/formatted/training.json, ./datasets/formatted/validation.json을 사용해 학습 코드.ipynb를 실행시켜 저장된 모델을 ./models로 이동시킨 후
4. ```
   cd ./
   python -m src.app로 서버 구동
   ```


## Contact
문의: sincelife777@gmail.com (illuminateP)
