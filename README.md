## 1. 징배봇이란

## 2. 준비사항

- 미러 봇
1. ubuntu 16.04 LTS 환경
2. [heroku](https://www.heroku.com "heroku") 계정
3. [kakaotalk 플러스친구](https://center-pf.kakao.com/login "kakaotalk 플러스친구") 계정

- 마음(maum) 플랫폼 연동
1. [마음(maum)](https://maum.ai/ "마음플랫폼") 챗봇

## 3. 징배봇 만들기

### 3.1. 미러(Mirror) 봇 만들어보기

```
미러(Mirror) 봇이란 "사용자의 말을 그대로 따라하는 봇"을 의미한다.
미러 봇은 챗봇이 잘 동작하는지 확인할 수 있는 가장 좋은 방법이기 때문에,
우리는 "hello world"를 print하듯 소심하게 말을 걸어볼 수 밖에 없다.

"...안녕?"
```

#### 3.1.1. kakaotalk 플러스친구 미러봇

- virtualenv 구축

  - virtualenv는 가상환경으로, 개발자 환경과 서버의 환경을 독립적으로 구성할 때 사용한다.

```
# virtualenv 설치
pip install virtualenvwrapper

mkdir ~/.virtualenvs

# home 디렉토리의 .bashrc 하단에 아래 문구 추가
export WORKON_HOME=~/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

source ~/.profile

# virtualenv 생성
# ~/.virtualenvs/(가상환경이름)이 생성된다.

mkvirtualenv (jingbebot)

# virtualenv를 빠져나오기 위해서는 deactivate 명령어를 사용한다.
deactivate
```

- heroku 배포

  - heroku는 PaaS 서비스로, 개발자가 git을 통해 애플리케이션을 업로드, 서비스할 수 있게 도와준다.

```
# Install heroku 
wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh

# Install git & config
sudo apt install git

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

# virtualenv & heroku 진입
workon (jingbebot) # jingbebot 가상환경 진입 시 workon 명령어 사용

heroku login

# git clone (임시 저장위치에서 git clone)
git clone https://github.com/ChoiHyeonJong/jingbebot.git

# mirror-bot 폴더 내의 app.py, Procfile, requirements.txt를 가상환경 폴더로 복사
cp app.py Procfile requirements.txt /home/.virtualenvs/(jingbebot) 

# heroku create
heroku create (jingbebot)

git init 
git remote add heroku https://git.heroku.com/(jingbebot).git

git add .
git commit -m "first commit"
git push heroku master
```

- kakaotalk 플러스친구 앱등록

  - [kakaotalk 플러스친구](https://center-pf.kakao.com/login "kakaotalk 플러스친구") 스마트채팅 -> api형
  - 앱 URL(https://(jingbebot).herokuapp.com) 등록 -> api test -> api형 저장하기
  
```

"안녕?"
```

#### 3.1.2. 페이스북 메신저 미러봇

### 3.2. 마음(maum) 플랫폼 연동

```
이제 미러 봇에서 한발짝 더 나아가 마인즈랩(MindsLab)의 챗봇 플랫폼인 마음(maum) 플랫폼을 연동시켜 보자.
마음 플랫폼은 Rest API를 제공하고 있기 때문에,
마음 플랫폼에서 구축한 챗봇은 다양한 인터페이스에서 대화가 가능하다.
```

#### 3.2.1. kakaotalk 플러스친구 연동

```
# git clone (임시 저장위치에서 git clone)
git clone https://github.com/ChoiHyeonJong/jingbebot.git

# maum-bot 폴더 내의 app.py, Procfile, requirements.txt를 가상환경 폴더로 복사
cp app.py Procfile requirements.txt /home/.virtualenvs/(jingbebot)

# app.py는 https://maum.ai 내의 마인즈랩 문의(ask_mindslab) 챗봇을 통해 대화하도록 설정되어 있다.
# 하나의 챗봇은 하나의 서비스 그룹만을 바라볼 수 있으므로 필요에 따라 app.py의 url과 서비스그룹을 수정하여 사용할 수 있다.

# heroku 재배포 과정은 아래의 세 명령어로 충분하다.
git add .
git commit -m "maum-bot try"
git push heroku master
```
