# Database Term Project: API Server

<br>

# Summary

## Subject
> ### Tving Clone Cording  
> We made it following the API server of tving.

## Requirement

Language
- Python: 3.12.4

Packages
- Flask: 3.1.0
- Flask-Restx: 1.3.0
- Numpy: 2.1.3
- Pandas: 2.2.3
- PyMySQL: 1.1.1
```shell
pip install flask
pip install flask-restx
pip install numpy
pip install pandas
pip install pymysql
```

---

# Project Architecture

```
~/(root) 
├ commen  // related to server’s environment settings 
│ └ config 
│ │ └ Config.py 
├ controller   // related for user to access this server by HTTP 
│ ├ ContentController.py 
│ ├ GenreController.py
│ ├ SearchController.py 
│ ├ UserController.py 
├ dto    // entities transforming service result to HTTP response 
│ ├ content 
│ │ ├ ContentDTO.py 
│ │ ├ LinkedContentDTO.py 
│ │ ├ PurchasedContentDTO.py 
│ │ └ WatchedContentDTO.py 
│ ├ user 
│ │ └ UserDTO.py 
├ excption 
│ ├ HttpException.py      // ex. (400) bad-request 
│ └ ValueException.py    // ex. DTO converting error 
├ repository   // functions to execute SQL 
│ ├ ContentRepository.py 
│ ├ GenreRepository.py 
│ ├ SearchRepository.py 
│ └ UserRepository.py 
├ service   // to process our service 
│ ├ ContentService.py 
│ ├ GenreService.py 
│ ├ SearchService.py 
│ └ UserService.py 
├ utils   // useful functions and variables unrelated to upper directory 
│ ├ DateFromat.py   // to format and parse a date in servie 
│ └ DB.py   // an instance of MySQL 
└ main.py
```

---

# API Documentation

| HTTP Method | Endpoint                      | Request Parameter                        | Response Fields                                                                                      | Description                                         |
|-------------|-------------------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| GET         | /user                         | { "uid": <int\> }                      | { "uid": <int\>, "name": <string\>, "image": <string\>, "email": <string\>, "phone": <string\>, "cash": <int\>, "payment": <int\> } | Get user information, such as name, email, etc.    |
| GET         | /user/like                    | { "uid": <int\> }                      | { "video_id": <char\>, "name": <string\>, "image": <string\>, "runtime": <int\>, "date": <string\> }   | Get contents that the user preferred.               |
| GET         | /user/purchase                | { "uid": <int\> }                      | { "video_id": <char\>, "name": <string\>, "image": <string\>, "type": <string\>, "price": <int\>, "runtime": <int\>, "date": <string\> } | Get contents that the user purchased.               |
| GET         | /user/watch                   | { "uid": <int\> }                      | { "video_id": <char\>, "name": <string\>, "image": <string\>, "runtime": <int\>, "date": <string\> }   | Get contents that the user watched.                 |
| GET         | /genre                        | -                                       | [ { "genre_id": <int\>, "name": <string\> } ]                                                       | Get all genres available.                            |
| GET         | /content                      | { "content_id": <int\> }               | { "content_id": <int\>, "name": <string\>, "image": <string\>, "limit_age": <string\>, "description": <string\>, "publisher": <string\>, "url": <string\>, "genre": <string\>, "actor": [ { "name": <string\>, "role": <string\> } ], "episode": [ { "video_id": <string\>, "url": <string\>, "quantity": <int\>, "episode_number": <int\> } ] } | Get details of specific content.                     |
| GET         | /content/recommend           | { "content_id": <int\> }               | [ { "id": <int\>, "name": <string\>, "image": <string\>, "category": <string\>, "description": <string\>, "publisher": <string\> } ] | Get related contents to a specified content.        |
| GET         | /content/list/popular        | -                                       | [ { "id": <int\>, "name": <string\>, "image": <string\>, "category": <string\>, "description": <string\>, "publisher": <string\> } ] | Get top 20 most popular contents.                    |
| GET         | /content/list/recently       | -                                       | [ { "id": <int\>, "name": <string\>, "image": <string\>, "category": <string\>, "description": <string\>, "publisher": <string\> } ] | Get 20 most recently added contents.                 |
| GET         | /content/list/genre          | -                                       | [ { "id": <int\>, "name": <string\>, "image": <string\>, "category": <string\>, "description": <string\>, "publisher": <string\> } ] | Get 20 contents related to the genre of specified content. |
| POST        | /search/actor                 | { "keyword": <string\> }               | [ { "id": <int\>, "name": <string\>, "image": <string\>, "category": <string\>, "description": <string\>, "publisher": <string\> } ] | Search contents by actor.                             |
| POST        | /search/title                 | { "keyword": <string\> }               | [ { "id": <int\>, "name": <string\>, "image": <string\>, "category": <string\>, "description": <string\>, "publisher": <string\> } ] | Search contents by title.                             |
| GET         | /search/popular               | -                                       | [ { "id": <int\>, "name": <string\>, "image": <string\>, "category": <string\>, "description": <string\>, "publisher": <string\> } ] | Get 20 contents that are popular for a day.         |
| GET         | /search/recom-mend/like      | { "uid": <int\> }                      | [ { "id": <int\>, "name": <string\>, "image": <string\>, "category": <string\>, "description": <string\>, "publisher": <string\> } ] | Get 20 contents related to genres of contents which user liked. |
| GET         | /search/recommend/watch       | { "uid": <int\> }                      | [ { "id": <int\>, "name": <string\>, "image": <string\>, "category": <string\>, "description": <string\>, "publisher": <string\> } ] | Get 20 contents related to genres of contents which user watched. |
| GET         | /watch                        | { "uid": <int\>, "video_id": <string\> } | { "video_id": <string\>, "content_id": <int\>, "name": <string\>, "image": <string\>, "limit_age": <string\>, "description": <string\>, "runtime": <int\>, "upload_date": <string\>, "user_like": <int\> } | Get streaming information of a specified content.     |

---

# Reference

## Contributor
- protaku
- parkseonin
- yoonchulShin
- 23mooon

## Related Repo
- [Data Crawling Codes](https://github.com/DB-Group-1/Data-collection-Part-DB-Group-1)
