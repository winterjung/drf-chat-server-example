# API

- All endpoints require JWT with HTTP Authorization except the register API (`POST /users/`).
- Using UUID to improve security is not yet considered.

## User

### `GET /users/<int:pk>/`

- Get user info

#### Response

```json
{
  "id": 2,
  "username": "JungWinter",
}
```

### `POST /users/`

- Register
- Only this endpoint is opened in public.

#### Request

```json
{
  "username": "JungWinter",
  "password": "test",
}
```

#### Response

```json
{
  "id": 1,
  "username": "JungWinter",
}
```

### `POST /auth/login`

#### Request

```json
{
  "username": "JungWinter",
  "password": "test",
}
```

#### Response

```json
{
  "access": "access token",
  "refresh": "refresh token",
}
```

### `POST /auth/refresh`

#### Request

```json
{
  "token": "refresh token",
}
```

#### Response

```json
{
  "access": "access token",
}
```

## Chat

### `GET /rooms/`

#### Response

```json
[
  {
    "id": 1,
    "title": "Room001",
    "participants": [
      1,
      2,
    ],
  },
  {
    "id": 2,
    "title": "Room002",
    "participants": [
      2,
      3,
    ],
  },
]
```

### `POST /rooms/`

#### Request

```json
{
  "title": "Test Room",
  "participants": [
    1,
    2,
  ],
}
```

#### Response

```json
{
  "id": 1,
  "title": "Test Room",
  "participants": [
    1,
    2,
  ],
}
```

### `GET /rooms/<int:pk>/`

#### Response

```json
{
  "id": 1,
  "title": "Test Room",
  "participants": [
    1,
    2,
  ],
}
```

### `GET /rooms/<int:pk>/messages/`

#### Response

```json
[
  {
    "id": 2,
    "sender": 1,
    "room": 1,
    "content": "Good",
  },
  {
    "id": 1,
    "sender": 2,
    "room": 1,
    "content": "How are you?",
  },
]
```

### `POST /rooms/<int:pk>/messages/`

#### Request

```json
{
  "sender": 1,
  "room": 1,
  "content": "Good",
}
```

#### Response

```json
{
  "id": 2,
  "sender": 1,
  "room": 1,
  "content": "Good",
}
```

### `GET /rooms/<int:pk>/messages/<int:pk>/`

#### Response

```json
{
  "id": 1,
  "sender": 2,
  "room": 1,
  "content": "How are you?",
},
```
