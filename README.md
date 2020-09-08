# Casting Agency API Capstone Project

### Published Endpoint
```
https://casting-agency-api-wh.herokuapp.com/
```

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Running the server

From within the `castingAgencyApi` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app` directs flask to use the `app` file to find the application. 

## API Documentation

### Casting Agency Endpoints
- GET /actors
- GET /movies
- GET /actor/roles
- GET /movie/casts
- GET /actor-details
- GET /movie-details
- POST /actors
- POST /movies
- PATCH /actors/actor_id
- PATCH /movies/movie_id
- DELETE /actors/actor_id
- DELETE /movies/movie_id

### Casting Agency Roles
- Casting Assistant
- Casting Director
- Executive Producer

### GET '/actors'
#### Permissions
- Public
```
Example: curl --location --request GET 'https://casting-agency-api-wh.herokuapp.com/actors'
{
    "actors": [
        {
            "id": 1,
            "name": "Chadwick Boseman"
        },
        {
            "id": 2,
            "name": "Michael B Jordan"
        },
        {
            "id": 3,
            "name": "Letitia Wright"
        },
        {
            "id": 4,
            "name": "Danai Gurira"
        },
        {
            "id": 5,
            "name": "Andy Serkis"
        },
        {
            "id": 6,
            "name": "Winston Duke"
        },
        {
            "id": 7,
            "name": "Lupita Nyong'o"
        },
        {
            "id": 8,
            "name": "Daniel Kaluuya"
        },
        {
            "id": 9,
            "name": "Angela Bassett"
        },
        {
            "id": 10,
            "name": "Sterling K. Brown"
        },
        {
            "id": 11,
            "name": "Martin Freeman"
        }
    ],
    "success": true
}
```
### GET '/movies'
#### Permissions
- Public
```
curl --location --request GET 'https://casting-agency-api-wh.herokuapp.com/movies'
{
    "movies": [
        {
            "id": 1,
            "title": "Black Panther"
        },
        {
            "id": 100000,
            "title": "Will Hughes: The Movie II"
        }
    ],
    "success": true
}
```

### GET '/actor/roles'
#### Permissions
- Public
```
Example: curl --location --request GET 'https://casting-agency-api-wh.herokuapp.com/actor/roles' 
[
    [
        {
            "actor_roles": {
                "actor_id": 1,
                "actor_name": "Chadwick Boseman",
                "movie_roles": [
                    {
                        "movie_id": 1,
                        "movie_role": "T'Challa/Black Panther",
                        "movie_title": "Black Panther"
                    }
                ]
            }
        },
        {
            "actor_roles": {
                "actor_id": 2,
                "actor_name": "Michael B Jordan",
                "movie_roles": [
                    {
                        "movie_id": 1,
                        "movie_role": "Erik Killmonger",
                        "movie_title": "Black Panther"
                    }
                ]
            }
        },
        {
            "actor_roles": {
                "actor_id": 3,
                "actor_name": "Letitia Wright",
                "movie_roles": [
                    {
                        "movie_id": 1,
                        "movie_role": "Shuri",
                        "movie_title": "Black Panther"
                    }
                ]
            }
        },
        {
            "actor_roles": {
                "actor_id": 4,
                "actor_name": "Danai Gurira",
                "movie_roles": [
                    {
                        "movie_id": 1,
                        "movie_role": "Okoye",
                        "movie_title": "Black Panther"
                    }
                ]
            }
        },
        {
            "actor_roles": {
                "actor_id": 5,
                "actor_name": "Andy Serkis",
                "movie_roles": [
                    {
                        "movie_id": 1,
                        "movie_role": "Klaw",
                        "movie_title": "Black Panther"
                    }
                ]
            }
        },
        {
            "actor_roles": {
                "actor_id": 6,
                "actor_name": "Winston Duke",
                "movie_roles": [
                    {
                        "movie_id": 1,
                        "movie_role": "M'Baku",
                        "movie_title": "Black Panther"
                    }
                ]
            }
        },
        {
            "actor_roles": {
                "actor_id": 7,
                "actor_name": "Lupita Nyong'o",
                "movie_roles": [
                    {
                        "movie_id": 1,
                        "movie_role": "Nakia",
                        "movie_title": "Black Panther"
                    }
                ]
            }
        },
        {
            "actor_roles": {
                "actor_id": 8,
                "actor_name": "Daniel Kaluuya",
                "movie_roles": [
                    {
                        "movie_id": 1,
                        "movie_role": "W'Kabi",
                        "movie_title": "Black Panther"
                    }
                ]
            }
        },
        {
            "actor_roles": {
                "actor_id": 9,
                "actor_name": "Angela Bassett",
                "movie_roles": [
                    {
                        "movie_id": 1,
                        "movie_role": "Ramonda",
                        "movie_title": "Black Panther"
                    }
                ]
            }
        },
        {
            "actor_roles": {
                "actor_id": 10,
                "actor_name": "Sterling K. Brown",
                "movie_roles": [
                    {
                        "movie_id": 1,
                        "movie_role": "N'Jobu",
                        "movie_title": "Black Panther"
                    }
                ]
            }
        },
        {
            "actor_roles": {
                "actor_id": 11,
                "actor_name": "Martin Freeman",
                "movie_roles": [
                    {
                        "movie_id": 1,
                        "movie_role": "Everett K. Ross",
                        "movie_title": "Black Panther"
                    }
                ]
            }
        }
    ],
    {
        "success": true
    }
]
```

### GET /movie/casts'
#### Permissions
- Public
```
Example: curl --location --request GET 'https://casting-agency-api-wh.herokuapp.com/movie/casts'
[
    [
        {
            "movie_cast": {
                "cast": [
                    {
                        "id": 1,
                        "name": "Chadwick Boseman",
                        "role": "T'Challa/Black Panther"
                    },
                    {
                        "id": 2,
                        "name": "Michael B Jordan",
                        "role": "Erik Killmonger"
                    },
                    {
                        "id": 3,
                        "name": "Letitia Wright",
                        "role": "Shuri"
                    },
                    {
                        "id": 4,
                        "name": "Danai Gurira",
                        "role": "Okoye"
                    },
                    {
                        "id": 5,
                        "name": "Andy Serkis",
                        "role": "Klaw"
                    },
                    {
                        "id": 6,
                        "name": "Winston Duke",
                        "role": "M'Baku"
                    },
                    {
                        "id": 7,
                        "name": "Lupita Nyong'o",
                        "role": "Nakia"
                    },
                    {
                        "id": 8,
                        "name": "Daniel Kaluuya",
                        "role": "W'Kabi"
                    },
                    {
                        "id": 9,
                        "name": "Angela Bassett",
                        "role": "Ramonda"
                    },
                    {
                        "id": 10,
                        "name": "Sterling K. Brown",
                        "role": "N'Jobu"
                    },
                    {
                        "id": 11,
                        "name": "Martin Freeman",
                        "role": "Everett K. Ross"
                    }
                ],
                "movie_id": 1,
                "movie_title": "Black Panther"
            }
        }
    ],
    {
        "success": true
    }
]
```

### GET '/actor-details'
#### Permissions
- Casting Assistant
- Casting Director
- Executive Producer
```
Example: url --location --request GET 'https://casting-agency-api-wh.herokuapp.com/actor-details' --header 'Authorization: Bearer token'
{
    "actors": [
        {
            "age": 43,
            "gender": "M",
            "id": 1,
            "name": "Chadwick Boseman"
        },
        {
            "age": 33,
            "gender": "M",
            "id": 2,
            "name": "Michael B Jordan"
        },
        {
            "age": 26,
            "gender": "F",
            "id": 3,
            "name": "Letitia Wright"
        },
        {
            "age": 42,
            "gender": "F",
            "id": 4,
            "name": "Danai Gurira"
        },
        {
            "age": 56,
            "gender": "M",
            "id": 5,
            "name": "Andy Serkis"
        },
        {
            "age": 33,
            "gender": "M",
            "id": 6,
            "name": "Winston Duke"
        },
        {
            "age": 37,
            "gender": "M",
            "id": 7,
            "name": "Lupita Nyong'o"
        },
        {
            "age": 31,
            "gender": "M",
            "id": 8,
            "name": "Daniel Kaluuya"
        },
        {
            "age": 62,
            "gender": "F",
            "id": 9,
            "name": "Angela Bassett"
        },
        {
            "age": 44,
            "gender": "M",
            "id": 10,
            "name": "Sterling K. Brown"
        },
        {
            "age": 48,
            "gender": "M",
            "id": 11,
            "name": "Martin Freeman"
        }
    ],
    "success": true
}
```

### GET '/movie-details'
#### Permissions
- Casting Assistant
- Casting Director
- Executive Producer
```
Example: curl --location --request GET 'https://casting-agency-api-wh.herokuapp.com/movie-details' --header 'Authorization: Bearer token
{
    "movies": [
        {
            "id": 1,
            "release_date": "Fri, 16 Feb 2018 00:00:00 GMT",
            "title": "Black Panther"
        }
    ],
    "success": true
}
```

### POST '/actors'
#### Permissions
- Casting Director
- Executive Producer
```
Example: curl --location --request POST 'https://casting-agency-api-wh.herokuapp.com/actors' --header 'Authorization: Bearer token --header 'Content-Type: application/json' \
--data-raw '{
    "id":100000,
    "name": "Will Hughes",
    "age": 20,
    "gender": "M"
}'

{
    "actors": [
        {
            "age": 20,
            "gender": "M",
            "id": 100000,
            "name": "Will Hughes"
        }
    ],
    "success": true
}
```

### POST '/movies'
#### Permissions
- Executive Producer
```
Example: curl --location --request POST 'https://casting-agency-api-wh.herokuapp.com/movies' --header 'Authorization: Bearer token --header 'Content-Type: application/json' \
--data-raw '{
    "id":100000,
    "title": "Will Hughes: The Movie",
    "release_date": "02/11/2000"
}'

{
    "actors": [
        {
            "id": 100000,
            "release_date": "Fri, 11 Feb 2000 00:00:00 GMT",
            "title": "Will Hughes: The Movie"
        }
    ],
    "success": true
}
```

### PATCH '/actors/actor_id'
#### Permissions
- Casting Director
- Executive Producer
```
Example: curl --location --request PATCH 'https://casting-agency-api-wh.herokuapp.com/actors/100000' --header 'Authorization: Bearer token --header 'Content-Type: application/json' \
--data-raw '{
    "age": 21
}'

{
    "actors": [
        {
            "age": 21,
            "gender": "M",
            "id": 100000,
            "name": "Will Hughes"
        }
    ],
    "success": true
}
```

### PATCH '/movies/movie_id'
#### Permissions
- Casting Director
- Executive Producer
```
Example: curl --location --request PATCH 'https://casting-agency-api-wh.herokuapp.com/movies/100000' --header 'Authorization: Bearer token --header 'Content-Type: application/json' \
--data-raw '{
    "title": "Will Hughes: The Movie II"
}'

{
    "actors": [
        {
            "id": 100000,
            "release_date": "Fri, 11 Feb 2000 00:00:00 GMT",
            "title": "Will Hughes: The Movie II"
        }
    ],
    "success": true
}
```

### DELETE '/actors/actor_id'
#### Permissions
- Casting Director
- Executive Producer
```
Example: curl --location --request DELETE 'https://casting-agency-api-wh.herokuapp.com/actors/100000' --header 'Authorization: Bearer token
{
    "deleted": 100000,
    "success": true
}
```

### DELETE '/movies/movie_id'
#### Permissions
- Executive Producer
```
Example: curl --location --request DELETE 'https://casting-agency-api-wh.herokuapp.com/movies/100000' --header 'Authorization: Bearer token
{
    "deleted": 100000,
    "success": true
}
```

### Error Handling'
```
{
    "error": 400, 
    "message": "bad request", 
    "success": false
}
```
```
{
    "error": 404, 
    "message": "resource not found", 
    "success": false
}
```
```
{
    "error": 405, 
    "message": "method not allowed", 
    "success": false
}
```
```
{
    "error": 422, 
    "message": "unprocessable", 
    "success": false
}
```
```
{
    "error": 500, 
    "message": "internal server error", 
    "success": false
}
```
```
{
    "error": {
        "code": "authorization_header_missing",
        "description": "Authorization header is expected."
    },
    "status_code": 401
}
```

## Testing
Import Postman Collection File and Run Test
```
casting-agency-api.postman_collection.json
```