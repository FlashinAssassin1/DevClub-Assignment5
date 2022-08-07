Site is deployed at [Flashlearn LMS](https://flashlearnlms.herokuapp.com/)
(All features and some bonus features have been implemented and will be updated here)

`CustomUser` model has been created for `Users` in which a user can be of three types:
1. `Student`
2. `Teacher`
3. `Admin`

Login Page:

<img width="957" alt="image" src="https://user-images.githubusercontent.com/97736785/181936141-2386426d-4024-466d-b898-8967306cb433.png">

Forgot Password:

if you ever forget your password then you can just enter your email and a password rest link will be sent to your email!

(`environment variables` have been used to store sensitive email information)

![image](https://user-images.githubusercontent.com/97736785/181937046-d27e8e68-0c56-4aa6-bd49-098622425e11.png)
![image](https://user-images.githubusercontent.com/97736785/181937048-eaa9333a-462a-45c5-b2bc-27a4edf90368.png)
![image](https://user-images.githubusercontent.com/97736785/181937071-c2594929-044e-4264-a267-bb365499c94a.png)

`Student` Home Page after login:

<img width="942" alt="image" src="https://user-images.githubusercontent.com/97736785/181936206-5105315c-326e-4816-ad96-f20abe7a3c04.png">

Pagination has been applied for more than 4 courses:

<img width="917" alt="image" src="https://user-images.githubusercontent.com/97736785/181936234-cafdbb8b-6619-417f-805d-36e9e49be26c.png">
<img width="608" alt="image" src="https://user-images.githubusercontent.com/97736785/181936247-ae14d37d-17c8-4083-abf3-5a4948f85cc1.png">

`Teacher` Home Page after login:(Similar to Student)

<img width="943" alt="image" src="https://user-images.githubusercontent.com/97736785/181936405-c1b206de-4407-45d7-aa76-c64de786dbc7.png">

`Admin` Home Page after login:

Extra `Create Course` Option opens form to create course code, title, select students and teachers. It is secure in the sense that students and teachers cannot open this route.

<img width="937" alt="image" src="https://user-images.githubusercontent.com/97736785/181936436-ca0bcaea-b78b-4e4b-8019-3ecd93e620ec.png">

`Profile` Page:
Profile page is accessible to everyone who is authenticated, however you can see the edit form only in your own profile. Profile pics are served up from `AWS S3 buckets`.

<img width="933" alt="image" src="https://user-images.githubusercontent.com/97736785/181936553-95381d3d-1cbb-42f1-8309-c71580f8e854.png">

Student View of Course:

<img width="943" alt="image" src="https://user-images.githubusercontent.com/97736785/181937300-202df462-bb71-4003-8e68-d6978fa364f9.png">
<img width="868" alt="image" src="https://user-images.githubusercontent.com/97736785/181937314-f0caee54-a9ba-4516-bdd6-1dc2d7114b6b.png">

Students in Course:
<img width="960" alt="image" src="https://user-images.githubusercontent.com/97736785/181937447-4d0f1bff-066d-4e83-9499-a485399d6842.png">

Teacher View of Course:

<img width="938" alt="image" src="https://user-images.githubusercontent.com/97736785/181993828-2ffc5cd3-fedd-4869-b0ab-b71d4ba33874.png">

Teacher creating a quiz and adding Questions(only multiple choice):
<img width="570" alt="image" src="https://user-images.githubusercontent.com/97736785/181992398-52f6fd18-5c0f-4b6e-b8cc-7ad47746800b.png">
<img width="579" alt="image" src="https://user-images.githubusercontent.com/97736785/181993215-daa22f98-7838-4a36-ae68-cda758d46616.png">
<img width="585" alt="image" src="https://user-images.githubusercontent.com/97736785/181994512-344d3dca-b4cb-44c8-8f03-68d07e2bf98a.png">

Student attempting Quiz:

<img width="273" alt="image" src="https://user-images.githubusercontent.com/97736785/181994555-15e9dd8b-9f2d-40dc-87bf-560b0e7b824d.png">

The timer of quiz stays intact even upon refresh thanks to `sessionStorage`

<img width="569" alt="image" src="https://user-images.githubusercontent.com/97736785/181994570-eb36cdac-7cac-4258-a20e-7be4f4f8e6a4.png">
<img width="283" alt="image" src="https://user-images.githubusercontent.com/97736785/181994600-9a75e4db-338b-4a76-8382-578c855d8b12.png">




# DevClub Assignment 5

You have learnt about backend engineering with Django in our session. Now use it to create a web application by yourself!
## DevClub LMS (Learning Management System)
You must have used **Moodle** in your courses, where both instructors and students login, and for each course, the instructor uses the platform to share resources, send announcements, release grades, conduct quizzes and what not!

Your task is to create your own such a learning management system using Django, where you can add functionalities as per your own creativity!

### We would recommend you to have these apps inside the project: 
- Users (to store auth logic, and models for `Instructor`, `Student`, `Course`, `Admin`)
- Grades (to store logic for sharing grades for any assessment, and models for let's say a class `Grade`)
- Documents (for Instructor to upload `Docs` like lecture notes for the course)
- Quizzes (this can have models for a `QuestionBank` containing `Question`'s which form a `Quiz`)
- Communication (to work on features like Course-wide `Announcements`, `Reply`ing in threads to announcements, sending personal `Messages`)

Try to implement as many features as you can, but make sure to plan the structure of the project and database schemas well!

### Bonus:
- Deploy on Heroku
- Create documentation for any RESTful APIs created with documenter on postman
- Markdown support for Communication
- Email: For registration, password reset, notifications, instructor custom message
- Bulk upload from CSV for grades, quizzes
- Generating PDF: Print digitally signed transcript
- Add security features for the quizzes

## Submission Instructions
- **FORK** this repository, by clicking the "Fork" button on top right
- `clone` the forked repo into your machine, and `cd` into the Repo Folder such that you are in same directory level as `manage.py`
- If on macOS, run `python3 -m venv env`, otherwise `python -m venv env`
- Now activate the virtual environment by `source env/bin/activate`
- See if the environment is correctly set by running `pip list`, it should be mostly empty
- Install dependencies with `pip install -r requirements.txt`
- We have already started a dummy project called `DevClubLMS` for you
- Now, you can use `python manage.py runserver` to start the dev server or `python manage.py startapp <appname>` to create a new app inside this project
- After completing the assignment, append instructions to run your project, along with explanation of features etc in this README
- It would be nice if you can host it on Heroku and also give a documentation of each endpoint through postman
- Finally submit with your details in the [Google Form](https://forms.gle/XSidrfbrsEZuDYfy6)
- You do NOT need to make any pull requests to this repo

# Resources
- [Slides used in the session](https://docs.google.com/presentation/d/e/2PACX-1vQbtDDGQonkIoGu68VrINL2s3sQcfiH5XVnk-iU26nk16DFBGsDabichsqhdtBvowPvpxaIbFLAV2h3/pub?slide=id.p)
- Introduction to Python and Django by [Programming With Mosh](https://youtu.be/_uQrJ0TkZlc)
- Detailed Django Tutorials by [Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
- [Mozilla's Tutorials](https://developer.mozilla.org/en-US/docs/Learn/Server-side) on Server Side Programming with Django
- [Django Official Docs](https://www.djangoproject.com/start/)
- [Talk](https://youtu.be/lx5WQjXLlq8) on how Instagram uses Django at production, and also [*the time when Justin Beiber almost crashed Instagram!*](https://youtu.be/lx5WQjXLlq8?t=715)
- Advice on Backend Engineering by [Hussein Nasser](https://www.youtube.com/c/HusseinNasser-software-engineering)
- Guide for Deploying Python apps on [Heroku](https://devcenter.heroku.com/categories/python-support)
- Guide for [Postman Documenter](https://learning.postman.com/docs/publishing-your-api/documenting-your-api/)