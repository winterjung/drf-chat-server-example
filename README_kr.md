# DRF chat server example

Django REST framework와 pytest를 이용한 RESTful 채팅 API 서버 예제

## 사용된 스택

* Python 3
* Django 2
* Django REST framework 3
* pytest

## 예제 기능

* 1:1 채팅
* 채팅방 목록 보기
* 가입 및 로그인이 가능하며 닉네임을 받음
* 메세지는 서버에 저장되며 일정 시간이 지나면 삭제됨
* 메세지 검색
* 메세지 알람 푸시 (임의의 프로토콜로 localhost:7000에 전송)
