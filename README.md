<p align="center">
  <img src="https://github.com/user-attachments/assets/0643d874-0b73-4b9b-bce0-108f4a99f410" alt="logo-small" />
</p>

# GiftWithCause


This is my first personal project with Django Framework for the final exam of Django Advanced course at SoftUni.

It is a website for finding gifts, that are hand made from a parent of a child with disabilities.

Users can register, log in, edit and delete their profiles, comment all posts, add gift posts to their favourite lists, create search posts. If the user is a creator/hero (parent of a child), he can also create gift offers. Only admins can change user to be a creator.

I created a simple Front End, practicing HTML and CSS and also implementing Responsive Web Page Design.

I used PostgreSQL as Database.

The application has a customized admin site, where admins and staff can create/view/edit/delete users and gifts.

I also added tests for GiftBaseForm, GiftCreateView and GiftEditView.


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

`SECRET_KEY` `DEBUG` `ALLOWED_HOSTS` `DB_NAME` `DB_USER` `DB_PASSWORD` `DB_HOST` `DB_PORT`


## Running Tests

To run tests, run the following command

```bash
  python manage.py test
```

## Screenshots

![GiftWithCause-home](https://github.com/user-attachments/assets/77f927c3-649a-4225-988b-45ba67b21975)

![GiftWithCause-gift-offers](https://github.com/user-attachments/assets/4925efde-a50b-4e98-b2f8-b26425c48886)

![GiftWithCause-our-heroes](https://github.com/user-attachments/assets/a4b896a5-c17e-4005-8272-10a953bd4c4e)

![GiftWithCause-gift-details](https://github.com/user-attachments/assets/0e119556-2f2b-4b0d-86a7-1d42d086c9f5)

![GiftWithCause-gift-search-details](https://github.com/user-attachments/assets/ed0afa42-eed6-4f62-8f33-8544179b3e9a)

![GiftWithCause-profile-details](https://github.com/user-attachments/assets/26fba5c8-6b39-4557-84fe-7d2f078c68ce)

![GiftWithCause-profile-details2](https://github.com/user-attachments/assets/63da7540-922a-40c3-91b1-3dd2cda61099)

![GiftWithCause-profile-details3](https://github.com/user-attachments/assets/6b395baa-5eb2-4c2e-bb2d-6f00de0d3ef2)

![GiftWithCause-gift-create](https://github.com/user-attachments/assets/3a9b215d-8655-46e2-8a2c-8c28a2766e95)

