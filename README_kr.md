# DRF chat server example

[English](./README.md) | [한국어](./README_kr.md)

Django REST framework와 pytest를 이용한 RESTful 채팅 API 서버 예제입니다.

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
* 메세지 푸시 알람 (임의의 프로토콜로 localhost:7000에 전송)

## API

[API 문서](./API-spec.md)에서 확인 가능합니다.

## 개발 과정

아래의 개발 과정을 통해 어떤 순서로 기능이 구현되었는지 참고할 수 있습니다.

* 개발 환경 세팅 - `.editorconfig`, `.gitignore`, `pipenv`
* settings를 development와 production으로 구분 [`[commit]`](https://github.com/JungWinter/drf-chat-server-example/commit/f387088a6a599598ee2d14ad6f59af11bdce1f75)
* [basic models](https://github.com/JungWinter/drf-chat-server-example/commit/af46c666ed6fce40ab128937ed116ce5a10a8f88), [serializers](https://github.com/JungWinter/drf-chat-server-example/commit/3085e11257c6f958903f03c33c1a0d3cf14fa95d), [viewsets와 nested router](https://github.com/JungWinter/drf-chat-server-example/commit/3ec6ecf0ab497ba65080f512b6822a213c81406b) 구현. [`[merge commit]`](https://github.com/JungWinter/drf-chat-server-example/commit/ff53905425005d0289f0de3eaf5df921f8a869bd)
* pytest를 이용한 기본 테스트 추가 [`[merge commit]`](https://github.com/JungWinter/drf-chat-server-example/commit/49802b51c022e4fc3088a5c8ef8afb6c7924cced)
* JWT를 사용해 유저 관련 기능 구현 [`[merge commit]`](https://github.com/JungWinter/drf-chat-server-example/commit/dacfdadfb7894851b2043163c97d03c2b5985014)
  * 의존성 추가 - [drf-simplejwt](https://github.com/davesque/django-rest-framework-simplejwt)
  * JWT 인증과 GET/POST 뷰 테스트 추가
  * [POST 버그 수정](https://github.com/JungWinter/drf-chat-server-example/commit/76fe710f6e00f0ccdc35aa0f0dceb72c2fd42e42), [가입 버그 수정](https://github.com/JungWinter/drf-chat-server-example/commit/80be9e75cd37abca1199681c4b8f673602761653)
* 검색 기능 구현 [`[merge commit]`](https://github.com/JungWinter/drf-chat-server-example/commit/ff56c2cb33a2ab32218e08521542d4b07e75ead6)
* 메세지 푸시 알람 구현 [`[merge commit]`](https://github.com/JungWinter/drf-chat-server-example/commit/543fd812c697d594559bd81b5130edf299958723)
  * 의존성 추가 - [django-background-tasks](https://github.com/arteria/django-background-tasks)
  * mock으로 테스트 [`[commit]`](https://github.com/JungWinter/drf-chat-server-example/commit/69e3e3d2ece060ecef0b7fbc4bdee487f68ca42d)
* 일정 시간 후 메세지를 삭제하는 기능 추가 [`[merge commit]`](https://github.com/JungWinter/drf-chat-server-example/commit/2bcd664cb48c282eda1b15df2a8beba65ba2f157)
* Dockerize
