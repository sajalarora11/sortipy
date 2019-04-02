# sortipy

## Running this file
```bash
$ git clone https://www.github.com/sajalarora11/sortipy.git
$ cd sortipy
$ python3 -m venv /path/to/new/virtual/environment
# source venv/bin/activate
$ pip install -r requirements.txt
$ export FLASK_APP=main.py
$ flask run
```
Now, open Postman and set the request type as POST and enter http://localhost:5000/sort_dict to get the output

## Sample input

```javascript
[
  {
    "id": 92,
    "name": "a21"
  },
  {
    "id": 12,
    "name": "a10"
  },
  {
    "id": 15,
    "name": "a5"
  },
  {
    "id": 72,
    "name": "a82"
  }
]
```

## Sample output
```javascript
[
  {
    "id": 15,
    "name": "a5"
  },
  {
    "id": 12,
    "name": "a10"
  },
  {
    "id": 92,
    "name": "a21"
  },
  {
    "id": 72,
    "name": "a82"
  }
]
```
