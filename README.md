# Operation Manual



### Contents

1. Auth

   1. Login
   2. Logout

2. Database

   1. User
      1. Select
   2. Purchase
      1. Select
      2. Insert
   3. Program
      1. Select
      2. Insert
   4. Season
      1. Select
      2. Insert
   5. Episode
      1. Select
      2. Insert

   

   

### 1. Auth

#### 	1.Login

##### Request

```
Target: http://localhost:5000

GET /oauth/login HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded
Content-Length:

access_token={access_token}&token_type={token_type}&id={id}
```

- access_token
- Token_type

- Id

##### Response

```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length:
Server: Werkzeug/2.0.1 Python/3.9.6

{
	"token": {token_data},
	"token_type": {token_type},
	"id": {id}
}
```

- token
- Token_type
- id



#### 	2. Logout

#####  

```
Target: http://localhost:5000

GET /oauth/logout HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded
Content-Length:

access_token={access_token}&token_type{token_type}
```

- access_token
- Token_type



##### Response

```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length:
Server: Werkzeug/2.0.1 Python/3.9.6

{
	"Logout":"True"
}
```

- Logout: 
  - True
  - False

### 2. Database

#### 	1. User

##### Request

```
Target: http://localhost:5000

GET /api/user HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded
Content-Length:

access_token={access_token}&token_type{token_type}
```

- Access_token
- Token_type



##### Response

```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length:
Server: Werkzeug/2.0.1 Python/3.9.6

{
	"user_id": {user_id},
	"name": {name},
	"email": {email},
	"adult": {adult}
	"last_login_time": {last_login_time}
}
```

- User_id
- name
- email
- Adult : notadult or adult
- Last_login_time: time_stamp



#### 	2. Purchase

​		1. Select

##### Request

```
Target: http://localhost:5000

GET /api/purchase HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded
Content-Length:

access_token={access_token}&token_type{token_type}
```

- Access_token
- Token_type



##### Response

```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length:
Server: Werkzeug/2.0.1 Python/3.9.6

{
	{Contents_list}
}
```

- Contents_list
  - {purchase_id, user_id, contents_name, purchase_time}



​		2.Insert

##### Request

```
Target: http://localhost:5000

POST /api/purchase HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded
Content-Length:

access_token={access_token}&token_type{token_type}&episode_id={episode_id}
```

- Access_token
- Token_type
- Episode_id



##### Response

```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length:
Server: Werkzeug/2.0.1 Python/3.9.6


```

- Error: if exist





#### 3. Program

​		1. Select

##### Request

```
Target: http://localhost:5000

GET /api/program HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded
Content-Length:


```





##### Response

```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length:
Server: Werkzeug/2.0.1 Python/3.9.6

{
	{Program_list}
}
```

- Contents_list
  - {Program_id, title, description}



​		2.Insert

##### Request

```
Target: http://localhost:5000

POST /api/program HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded
Content-Length:

access_token={access_token}&token_type{token_type}&title={title}&description={description}
```

- Access_token
- Token_type
- title
- Description



##### Response

```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length:
Server: Werkzeug/2.0.1 Python/3.9.6


```

- Error: if exist





#### 4. Season

​		1. Select

##### Request

```
Target: http://localhost:5000

GET /api/season HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded
Content-Length:

program_id={program_id}
```

- Program_id

##### Response

```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length:
Server: Werkzeug/2.0.1 Python/3.9.6

{
	{Season_list}
}
```

- Contents_list
  - {Season_id, program_id, title, member, director, season_cnt, genre}



​		2.Insert

##### Request

```
Target: http://localhost:5000

POST /api/season HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded
Content-Length:

access_token={access_token}&token_type{token_type}&title={title}&member={member}&director={director}&season_cnt={season_cnt}&genre={genre}
```

- Access_token
- Token_type
- title
- member
- director
- Season_cnt
- Genre



##### Response

```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length:
Server: Werkzeug/2.0.1 Python/3.9.6


```

- Error: if exist



#### 5. Episode

​		1. Select

##### Request

```
Target: http://localhost:5000

GET /api/episode HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded
Content-Length:

access_token={access_token}&token_type{token_type}&season_id={season_id}
```

- Access_token
- Token_type
- Season_id



##### Response

```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length:
Server: Werkzeug/2.0.1 Python/3.9.6

{
	{episode_list}
}
```

- Contents_list
  - {episode_id, season_id, number, guest, date, grade}



​		2.Insert

##### Request

```
Target: http://localhost:5000

POST /api/episode HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded
Content-Length:

access_token={access_token}&token_type{token_type}&season_id={season_id}&number={number}&guest={guest}&date={date}&grade={grade}
```

- Access_token
- Token_type
- season_id
- number
- guest
- date
- Grade

##### Response

```
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length:
Server: Werkzeug/2.0.1 Python/3.9.6


```

- Error: if exist



