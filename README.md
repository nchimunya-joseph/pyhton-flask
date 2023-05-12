# WEB WITH FLASK
Flask is apyhton flamework that makes it easy to write websites

### Prerequites
- python installed on your machine
- bootstrap
- css
- html

```
web-python/
|   app.py
|
|___static/
|   |____css/
|   |    |   style.css
|   |
|   |____img/
|        |   img.jpg
|
|
|___templates/
|   |   index.html
|   |   about.html
|   |   create.html
|   |   edit.html
|   |   post.html
|
|   init_db.py
|   schema.sql
```
## USAGE

create a virtual enviroment using this command

## Windows uses

    python -m venv [name_of_your_venv]

then

    [name_of_your_venv]\Scripts\activate

now install flask in your virtaul enviroment:

    pip install flask

## Linux or MacOS

    python3 -m venv [name_of_your_venv]

then

    source [name_of_your_venv]/bin/activate

now install flask in your virtaul enviroment:

    pip3 install Flask


### Query Single Post

```python
    def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()

    if post is None:
        abort(404)
    return post
```

Author: Joseph Nchimunya

Reference: [Digital Occean]()