## 1. 징배봇이란

## 2. 준비사항

1. ubuntu 16.04 LTS 환경
2. [heroku](https://www.heroku.com "heroku") 계정
3. [kakaotalk 플러스친구](https://center-pf.kakao.com/login "kakaotalk 플러스친구") 계정

## 3. 징배봇 만들기

### 3.1. 미러(Mirror) 봇 만들어보기

```
미러(Mirror) 봇이란 "사용자의 말을 그대로 따라하는 봇"을 의미한다.
개인적으로 어린시절 말을 그대로 따라 하는 장난을 가장 싫어했다.
하지만 미러 봇은 챗봇이 잘 동작하는지 확인할 수 있는 가장 좋은 방법이기 때문에,
우리는 "hello world"를 print하듯 소심하게 말을 걸어볼 수 밖에 없다.

"...안녕?"
```

#### kakaotalk 플러스친구 미러봇

##### virtualenv 구축

virtualenv는 가상환경으로, 개발자 환경과 서버의 환경을 독립적으로 구성할 때 사용한다.

```
# Install virtualenv
pip install virtualenvwrapper

# 환경설정
mkdir ~/.virtualenvs
export WORKON_HOME=~/.virtualenvs

# home 디렉토리 .bashrc 하단에 아래 문구 추가
export WORKON_HOME=~/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

# reload profile
source ~/.profile

# virtualenv 생성
# ~/.virtualenvs/(가상환경이름)이 생성된다.

mkvirtualenv jingbebot 

# virtualenv를 빠져나오기 위해서는 deactivate 명령어를 사용한다.
deactivate
```

##### heroku  

heroku는 PaaS 서비스로, 개발자가 어플리케이션을 git을 통해 업로드, 서비스할 수 있게 도와준다.

```
# Install heroku 
wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh

# Install git & config
sudo apt install git

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

# virtualenv, heroku 진입

workon jingbebot
heroku login

# jingbebot 징배봇 가상환경 (~/.virtualenvs/jingbebot) 안으로 git clone 

heroku create jingbebot
git init 
git remote add heroku https://git.heroku.com/(jingbebot).git
git add .
git commit -m "first commit"
git push heroku master

```

- 페이스북 메신저 미러봇
