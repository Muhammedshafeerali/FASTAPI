
# FASTP API [BLOG API]

Blog and User CRUD with SQL Database and JWT token


## Demo

https://i150h9.deta.dev/docs/



## API Reference

#### Authentication

```http
  POST /login/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**.     |
| `password` | `string` | **Required**.     |

#### Get all Blogs

```http
  GET /blog/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`      | `string` | **Required**.        |

#### Get Blog

```http
  GET /blog/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`      | `string` | **Required**.        |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Create Blog

```http
  POST /blog/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`      | `string` | **Required**.        |
| `title`      | `string` | **Required**.        |
| `body`      | `string` | **Required**.  |

#### Update Blog

```http
  PUT /blog/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`      | `string` | **Required**.        |
| `id`      | `string` | **Required**. Id of item to fetch |
| `title`      | `string` | **Required**.        |
| `body`      | `string` | **Required**.  |


#### Get all Users

```http
  GET /user/
```

#### Get User

```http
  GET /user/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


#### Create User

```http
  POST /user/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**.  |
 `email`      | `string` | **Required**.  |
  `password`      | `string` | **Required**.  |


## Run Locally

Clone the project

```bash
  git clone https://github.com/Muhammedshafeerali/FASTAPI.git
```

Go to the project directory

```bash
  cd FASTAPI
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  uvicorn Blog.main:app --reload
```


## Documentation

[Documentation](https://fastapi.tiangolo.com/)

