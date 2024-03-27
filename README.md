
# To Do APP API

## Authors

- [@Luis Eduardo](https://www.github.com/LUISEDOCCOR)


## Installation

Install my-project 

```bash
    git clone "https://github.com/LUISEDOCCOR/api-to-do-app"
    cd api-to-do-app
    pip install ---
    pyhton index.py
```
    
## API Reference

### Auth

#### SignUp
```http
  GET /signup
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | **Required**.|
| `password` | `string` | **Required**.|



#### Login
```http
  GET /login
```
 Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | **Required**.|
| `password` | `string` | **Required**.|


#### They return a JWT, which is necessary to access the other routes

### To Do

#### Create
```http
  GET /todo/create
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `string` | **Required**.|
| `content` | `string` | **Required**.|




#### DELETE
```http
  GET /todo/delete
```

 Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `id` | **Required**.|



#### UPDATE
```http
  GET /todo/edit
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `title` | `string` | **Required**.|
| `content` | `string` | **Required**.|
| `id` | `int` | **Required**.|


#### GET
```http
  GET /todos
```
