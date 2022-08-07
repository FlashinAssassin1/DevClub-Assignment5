Site is deployed at [Flashlearn LMS](https://flashlearnlms.herokuapp.com/)
(All features and some bonus features have been implemented and will be updated here)

`CustomUser` model has been created for `Users` in which a user can be of three types:
1. `Student`
2. `Teacher`
3. `Admin`

Register Page
Each Person can register either as a student or a teacher and must choose a unique Username accordingly. Upon registering you can find a six digit uinque ID in your profile.

<img width="849" alt="image" src="https://user-images.githubusercontent.com/97736785/183304131-4da3a00b-89fb-4082-bbc4-591165431e8c.png">


Login Page:

<img width="960" alt="image" src="https://user-images.githubusercontent.com/97736785/183298881-d620f0c7-0a3f-467f-a012-6b65650dd39d.png">

Forgot Password:

if you ever forget your password then you can just enter your email and a password rest link will be sent to your email!

(`environment variables` have been used to store sensitive email information)

<img width="960" alt="image" src="https://user-images.githubusercontent.com/97736785/183298924-e7faa87b-06e2-4c5f-a626-ad0d7c6b3d63.png">
<img width="615" alt="image" src="https://user-images.githubusercontent.com/97736785/183298950-b66e236e-649c-4f7a-9275-79d044ab2603.png">
<img width="547" alt="image" src="https://user-images.githubusercontent.com/97736785/183298987-8ea91fb2-4c35-4e3b-aaa7-bbea8e4f221a.png">

`Student` Home Page after login:

<img width="941" alt="image" src="https://user-images.githubusercontent.com/97736785/183300579-a2d214d4-5455-4f1e-bfc8-9a3c9651ea9c.png">

Pagination has been applied for more than 4 courses:

<img width="941" alt="image" src="https://user-images.githubusercontent.com/97736785/183300621-faf2871e-bd9e-47e2-a0c7-d2ad67cbf9b2.png">
<img width="595" alt="image" src="https://user-images.githubusercontent.com/97736785/183300635-7cd82c2b-a482-46fc-9e23-d5e3cdbab5b8.png">

`Teacher` Home Page after login:(Similar to Student)

<img width="944" alt="image" src="https://user-images.githubusercontent.com/97736785/183300579-a2d214d4-5455-4f1e-bfc8-9a3c9651ea9c.png">

`Admin` Home Page after login:

Extra `Create Course` Option opens form to create course code, title, select students and teachers. It is secure in the sense that students and teachers cannot open this route.

<img width="947" alt="image" src="https://user-images.githubusercontent.com/97736785/183300669-8c33c57b-459c-41bb-b6a7-b165d12466ce.png">

`Profile` Page:
Each person is automatically assigned a unique six digit ID.
Profile page is accessible to everyone who is authenticated, however you can see the edit form only in your own profile. Profile pics and all other media are served up using `AWS S3 buckets`.

<img width="946" alt="image" src="https://user-images.githubusercontent.com/97736785/183300883-7a7b3864-bcc6-4644-aa1c-e67e93080245.png">

Student View of Course:

<img width="942" alt="image" src="https://user-images.githubusercontent.com/97736785/183300898-2b359ce4-6f1d-45ab-8706-0d84722ebed4.png">
<img width="902" alt="image" src="https://user-images.githubusercontent.com/97736785/183300911-4a3c9086-e0ff-4763-866e-276559d5b6f7.png">

Students in Course:
<img width="955" alt="image" src="https://user-images.githubusercontent.com/97736785/183300930-1f5df0e2-b5a3-472c-885b-e89610f4981a.png">

Teacher View of Course:

<img width="944" alt="image" src="https://user-images.githubusercontent.com/97736785/183300950-f3650292-bae1-4369-bcf8-a466ca8f6d17.png">

Teacher creating a quiz and adding Questions(only multiple choice):
<img width="570" alt="image" src="https://user-images.githubusercontent.com/97736785/181992398-52f6fd18-5c0f-4b6e-b8cc-7ad47746800b.png">
<img width="935" alt="image" src="https://user-images.githubusercontent.com/97736785/183301050-6c2a2c61-c6b2-4dd4-9253-08296a49bf62.png">
<img width="911" alt="image" src="https://user-images.githubusercontent.com/97736785/183301075-a150d24d-2e88-4a8e-9966-32156f3196db.png">

Student attempting Quiz:

<img width="267" alt="image" src="https://user-images.githubusercontent.com/97736785/183301103-0e234420-08dd-4bb4-ab44-b7522b1f96bb.png">

The timer of quiz stays intact even upon refresh thanks to `sessionStorage`

<img width="570" alt="image" src="https://user-images.githubusercontent.com/97736785/183301117-b048ec73-2689-4877-a825-d5b185e204c2.png">
<img width="286" alt="image" src="https://user-images.githubusercontent.com/97736785/183301126-ae9dbb2f-d88c-4454-bb78-53d83c5c23a9.png">

`CourseGrade` model has been used to store grades of a course. Teacher can use a csv to bulk upload the final grades of a course!

<img width="559" alt="image" src="https://user-images.githubusercontent.com/97736785/183301792-6165150a-cac8-4903-b15a-9984087649a8.png">

<img width="587" alt="image" src="https://user-images.githubusercontent.com/97736785/183301879-3967e90b-7d89-4797-bc5d-ceeb9d79bcb3.png">
<img width="336" alt="image" src="https://user-images.githubusercontent.com/97736785/183301896-0976281a-d6f6-4710-b416-1cc44f4c6791.png">
<img width="574" alt="image" src="https://user-images.githubusercontent.com/97736785/183301906-61512d70-7fa1-4c2f-b5b1-7d73939af4f8.png">
<img width="563" alt="image" src="https://user-images.githubusercontent.com/97736785/183302724-d50ccb3c-f393-41f5-8a71-4c5f037a3109.png">

Teachers of a course can upload lecture notes for the course whose filetype will automatically be parsed to show image associated with it!

<img width="588" alt="image" src="https://user-images.githubusercontent.com/97736785/183304021-04789f86-0592-41c4-9068-dcdc3f5e5522.png">
<img width="578" alt="image" src="https://user-images.githubusercontent.com/97736785/183302845-ac51e408-417c-4a03-9f26-5bb26f49eba2.png">

There is a general forum as well as a forum for each course where `markdown` is supported for content of each post. Further one can `reply in threads` to each post!

<img width="595" alt="image" src="https://user-images.githubusercontent.com/97736785/183303056-623f4948-b1d9-4782-a6fd-6cdde0c519a0.png">
<img width="548" alt="image" src="https://user-images.githubusercontent.com/97736785/183303012-fa2e9e36-bdcc-4021-9e31-2fcd8a2bb2d0.png">
<img width="887" alt="image" src="https://user-images.githubusercontent.com/97736785/183303031-fc241fb0-2cd5-47f2-a1af-05904af57cb5.png">

You can search for a user by name using the option in sidebar. This allows you to access their profile which you can use to chat with them.

<img width="775" alt="image" src="https://user-images.githubusercontent.com/97736785/183303075-6fd5ff02-b6e3-444a-9f96-8eff07add03c.png">
<img width="591" alt="image" src="https://user-images.githubusercontent.com/97736785/183303367-09afc13d-e346-4cd7-86b9-4c467c5c4886.png">
<img width="742" alt="image" src="https://user-images.githubusercontent.com/97736785/183303199-207fc839-329b-47bd-9ad3-e83b9a7f45a9.png">







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