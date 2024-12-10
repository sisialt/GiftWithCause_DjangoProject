![logo.png](static%2Fimages%2Flogo.png)

# GiftWithCause

This is my first personal project with Django Framework for the final exam of Django Advanced course at SoftUni.

It is a website for finding gifts, that are hand made from a parent of a child with disabilities.

Users can register, log in, edit and delete their profiles, comment all posts, add gift posts to their favourite lists, create search posts. If the user is a creator/hero (parent of a child), he can also create gift offers. Only admins can change user to be a creator.

I created a simple Front End, practicing HTML and CSS.

I used PostgreSQL as Database.

The application has a customized admin site.


## Run Locally


Install dependencies

```bash
  pip install -r requirements.txt
```

Run the server

```bash
  python manage.py runserver
```



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file. I committed the .env file with the sensitive information, in order to be easier for the trainer jury.

`SECRET_KEY`

`DEBUG`

`ALLOWED_HOSTS`

`DB_NAME`

`DB_USER`

`DB_PASSWORD`

`DB_HOST`

`DB_PORT`


## Screenshots




## Running Tests

To run tests, run the following command

```bash
  python manage.py test
```

