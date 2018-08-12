# API

- JWT is not yet considered.
- Using UUID to improve security is not yet considered.

## GET /rooms

### Response

```json
[
  {
    "id": 1,
    "participants": [
      1,
      2,
    ],
  },
  {
    "id": 2,
    "participants": [
      2,
      3,
    ],
  },
]
```

## POST /rooms

### Request

```json
{
  "title": "Test Room",
  "participants": [
    1,
    2,
  ],
}
```

### Response

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

## GET /rooms/<int:pk>

### Response

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

## GET /rooms/<int:pk>/messages

### Response

```json
[
  {
    "id": 2,
    "sender": 1,
    "content": "Good",
  },
  {
    "id": 1,
    "sender": 2,
    "content": "How are you?",
  },
]
```

## POST /rooms/<int:pk>/messages

### Request

```json
{
  "sender": 1,
  "room": 1,
  "content": "Good",
}
```

### Response

```json
{
  "id": 2,
  "sender": 1,
  "room": 1,
  "content": "Good",
}
```

## GET /rooms/<int:pk>/messages/<int:pk>

### Response

```json
{
  "id": 1,
  "sender": 2,
  "room": 1,
  "content": "How are you?",
},
```

## GET /user

### Response

```json
{
  "id": 2,
  "username": "JungWinter",
}
```

## POST /user

### Request

```json
{
  "username": "JungWinter",
  "password": "test",
}
```
