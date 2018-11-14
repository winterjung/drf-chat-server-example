# DRF chat server example

A RESTful chat API server example used Django REST framework with pytest

## Used stack

* Python 3
* Django 2
* Django REST framework 3
* pytest

## Example features

* 1:1 chat
* list of chat room
* register & login with nickname
* message will be removed after short time
* search message
* push notification

## API

You can see [API document](https://github.com/JungWinter/drf-chat-server-example/blob/develop/API-spec.md)

## Development story

For easily understanding, you can follow development story.

* Init develop environment - `.editorconfig`, `.gitignore`, `pipenv`
* Separate settings to development and production [`[commit]`](https://github.com/JungWinter/drf-chat-server-example/commit/f387088a6a599598ee2d14ad6f59af11bdce1f75)
* Implement [basic models](https://github.com/JungWinter/drf-chat-server-example/commit/af46c666ed6fce40ab128937ed116ce5a10a8f88), [serializers](https://github.com/JungWinter/drf-chat-server-example/commit/3085e11257c6f958903f03c33c1a0d3cf14fa95d), [viewsets and nested router](https://github.com/JungWinter/drf-chat-server-example/commit/3ec6ecf0ab497ba65080f512b6822a213c81406b). [`[merge commit]`](https://github.com/JungWinter/drf-chat-server-example/commit/ff53905425005d0289f0de3eaf5df921f8a869bd)
* Add basic tests using pytest [`[merge commit]`](https://github.com/JungWinter/drf-chat-server-example/commit/49802b51c022e4fc3088a5c8ef8afb6c7924cced)
* Implement user features with jwt [`[merge commit]`](https://github.com/JungWinter/drf-chat-server-example/commit/dacfdadfb7894851b2043163c97d03c2b5985014)
  * Update dependencies - [drf-simplejwt](https://github.com/davesque/django-rest-framework-simplejwt)
  * Add jwt authentication views
  * Test views with jwt authentication and implement GET/POST views
  * [Fix wrong behavior of POST](https://github.com/JungWinter/drf-chat-server-example/commit/76fe710f6e00f0ccdc35aa0f0dceb72c2fd42e42), [Fix wrong user registration](https://github.com/JungWinter/drf-chat-server-example/commit/80be9e75cd37abca1199681c4b8f673602761653)
* Implement search feature [`[merge commit]`](https://github.com/JungWinter/drf-chat-server-example/commit/ff56c2cb33a2ab32218e08521542d4b07e75ead6)
* Implement push notification feature [`[merge commit]`](https://github.com/JungWinter/drf-chat-server-example/commit/543fd812c697d594559bd81b5130edf299958723)
  * Update dependencies - [django-background-tasks](https://github.com/arteria/django-background-tasks)
  * Test using mock [`[commit]`](https://github.com/JungWinter/drf-chat-server-example/commit/69e3e3d2ece060ecef0b7fbc4bdee487f68ca42d)
* Delete messages after a certain amount of time [`[merge commit]`](https://github.com/JungWinter/drf-chat-server-example/commit/2bcd664cb48c282eda1b15df2a8beba65ba2f157)
* Dockerize
