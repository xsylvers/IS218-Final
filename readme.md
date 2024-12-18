# The User Management System Final Project: Your Epic Coding Adventure Awaits! 🎉✨🔥

## Links to Commits
Commit: (https://github.com/xsylvers/IS218-Final/commit/25b52c0433dc875c179bacd583c2121031843105)

Commit: (https://github.com/xsylvers/IS218-Final/commit/186f5481a200dd006133b6995bef09bd7f316305)

Commit: (https://github.com/xsylvers/IS218-Final/commit/cf914f5fbe243a90bac4bd1edbec48771249e2d4)

Commit: (https://github.com/xsylvers/IS218-Final/commit/d2fe01c18057973cc9e60e757af1b59639eff742)

Commit: (https://github.com/xsylvers/IS218-Final/commit/c7589e4e02bb74b21b1682cf53f07f32cb13cd0a)

Commit: (https://github.com/xsylvers/IS218-Final/commit/82497a495959f21ca7733069202f0ea00b602b7d)

Commit: (https://github.com/xsylvers/IS218-Final/commit/96c315bd403751a7dd8da4523da0885291fc49c9)

Commit: (https://github.com/xsylvers/IS218-Final/commit/0a1db3a4ce8026635484e6760d04c9572838da8a)

Commit: (https://github.com/xsylvers/IS218-Final/commit/49c03c72ce72552ca97c7613706b0604c57e099e)

Commit: (https://github.com/xsylvers/IS218-Final/commit/3b2560603ac10af8b01acfc7d26586deef069233)

Commit: (https://github.com/xsylvers/IS218-Final/commit/50ba019daee85a14d7b94e577d293d72567d9a80)

Commit: (https://github.com/xsylvers/IS218-Final/commit/e152d0a74e27a53765d869796057567d606d7c2d)

Commit:(https://github.com/xsylvers/IS218-Final/commit/d49e7f6826c7b9ae7bdda0e8be9d851ae84215da)




## Introduction: Buckle Up for the Ride of a Lifetime 🚀🎬

Welcome to the User Management System project! 🏫👨‍🏫⭐ This project is your gateway to coding glory, providing a bulletproof foundation for a user management system that will blow your mind! 🤯 You'll bridge the gap between the realms of seasoned software pros and aspiring student developers like yourselves. 

### [Instructor Video - Project Overview and Tips](https://youtu.be/gairLNAp6mA) 🎥

- [Introduction to the system features and overview of the project - please read](system_documentation.md) 📚
- [Project Setup Instructions](setup.md) ⚒️
- [Features to Select From](features.md) 🛠️
- [About the Project](about.md)🔥🌟

## Goals and Objectives: Unlock Your Coding Superpowers 🎯🏆🌟

Get ready to ascend to new heights with this legendary project:

1. **Practical Experience**: Dive headfirst into a real-world codebase, collaborate with your teammates, and contribute to an open-source project like a seasoned pro! 💻👩‍💻🔥
2. **Quality Assurance**: Develop ninja-level skills in identifying and resolving bugs, ensuring your code quality and reliability are out of this world. 🐞🔍⚡
3. **Test Coverage**: Write additional tests to cover edge cases, error scenarios, and important functionalities - leave no stone unturned and no bug left behind! ✅🧪🕵️‍♂️
4. **Feature Implementation**: Implement a brand new, mind-blowing feature and make your epic mark on the project, following best practices for coding, testing, and documentation like a true artisan. ✨🚀🎆
5. **Collaboration**: Foster teamwork and collaboration through code reviews, issue tracking, and adhering to contribution guidelines - teamwork makes the dream work, and together you'll conquer worlds! 🤝💪🌍
6. **Industry Readiness**: Prepare for the software industry by working on a project that simulates real-world development scenarios - level up your skills to super hero status  and become an unstoppable coding force! 🔝🚀🏆⚡

## Managing the Project Workload: Stay Focused, Stay Victorious ⏱️🧠⚡

This project requires effective time management and a well-planned strategy, but fear not - you've got this! Follow these steps to ensure a successful (and sane!) project outcome:

1. **Select a Feature**: [Choose a feature](features.md) from the provided list of additional improvements that sparks your interest and aligns with your goals like a laser beam. ✨⭐🎯 This is your chance to shine!

2. **Test Coverage Improvement**: Review the existing test suite and identify gaps in test coverage like a pro. Create 10 additional tests to cover edge cases, error scenarios, and important functionalities related to your chosen feature. Focus on areas such as user registration, login, authorization, and database interactions. Simulate the setup of the system as the admin user, then creating users, and updating user accounts - leave no stone unturned, no bug left behind! ✅🧪🔍🔬 Become the master of testing!

3. **New Feature Implementation**: Implement your chosen feature, following the project's coding practices and architecture like a coding ninja. Write appropriate tests to ensure your new feature is functional and reliable like a rock. Document the new feature, including its usage, configuration, and any necessary migrations - future you will thank you profusely! 🚀✨📝👩‍💻⚡ Make your mark on this project!

4. **Maintain a Working Main Branch**: Throughout the project, ensure you always have a working main branch deploying to Docker like a well-oiled machine. This will prevent any last-minute headaches and ensure a smooth submission process - no tears allowed, only triumphs! 😊🚢⚓ Stay focused, stay victorious!

## Commands

1. Start and build a multi-container application:

```
docker compose up --build
```

2. Goto http://localhost/docs to view openapi spec documentation

Click "authorize" input username: `admin@example.com` password: `secret`

3. Goto http://localhost:5050 to connect and manage the database.

The following information must match the ones in the `docker-compose.yml` file.

Login:

- Email address / Username: `admin@example.com`
- Password: `adminpassword`

When add new server:

- Host name/address: `postgres`
- Port: `5432`
- Maintenance database: `myappdb`
- Username: `user`
- Password: `password`

## Optional Commands

### Run `pytest` inside the containers:

Run all tests:

```
docker compose exec fastapi pytest
```

Run a single test:

```
docker compose exec fastapi pytest tests/test_services/test_user_service.py::test_list_users
```

### Creating database migration:

```
docker compose exec fastapi alembic revision --autogenerate -m 'added admin'
```


### Apply database migrations:

```
docker compose exec fastapi alembic upgrade head
```


## Submission and Grading: Your Chance to Shine 📝✏️📈

1. **Reflection Document**: Write a document file (`.md` file, at least 400 words) reflecting on your learnings throughout the course and your experience working on this epic project. Include **10 NEW tests, and 1 Feature** you'll be graded on. Make sure your project successfully deploys to DockerHub and include a link to your Docker repository in the document - let your work speak for itself! 📄🔗💥

2. **Commit History**: Show off your consistent hard work through your commit history like a true coding warrior. **Projects with less than 10 commits will get an automatic 0 - ouch!** 😬⚠️ A significant part of your project's evaluation will be based on your use of issues, commits, and following a professional development process like a boss - prove your coding prowess! 💻🔄🔥

3. **Deployability**: Broken projects that don't deploy to Dockerhub or pass all the automated tests on GitHub actions will face point deductions - nobody likes a buggy app! 🐞☠️ Show the world your flawless coding skills!

### Grading Rubric: (100 Points)

#### 1. Reflection Document (20 Points)

- 10 Points: Quality and completeness of the reflection document, including insights into learnings, challenges faced, and how they were overcome. Must meet the minimum word count (400 words).
- 10 Points: Clear and detailed description of the new feature implemented, including its purpose, usage, and configuration.

#### 2. Commit History and Professional Development Process (20 Points)

- 20 Points: Consistent commit history with meaningful commit messages. Projects with fewer than 10 commits receive 0 points in this category.


#### 3. Test Coverage and Quality Assurance (30 Points)

- 15 Points: Quality and thoroughness of 10 new test cases, covering edge cases, error scenarios, and critical functionalities.
- 10 Points: New test cases must integrate well with the existing test suite and pass on GitHub Actions.
- 5 Points: Tests demonstrate creativity and critical thinking, ensuring robust quality assurance for both existing and new features.

#### 4. New Feature Implementation (30 Points)

- 15 Points: Functionality and reliability of the new feature, including adherence to project coding standards and architecture.
- 10 Points: Tests written for the new feature ensure it works as intended and handles edge cases.
- 5 Points: Documentation of the new feature, including its purpose, configuration, and any necessary migrations.

#### 5. Deployability (~~20 Points~~ Optional)

- 10 bonus points: Working deployment to DockerHub, with no critical issues or broken functionalities. Add the DockerHub deployment link to the README or upload a screenshot of your project being pushed to DockerHub.
- Maintains a clean and functional main branch throughout the project lifecycle.

### Notes:

This is our final assignment. You have two weeks to complete it, and late submissions will not be accepted.

Remember, it's more important to make something work reliably and be reasonably complete than to implement an overly complex feature. Focus on creating a feature that you can build upon or demonstrate in an interview setting - show off your skills like a rockstar! 💪🚀🎓

Don't forget to always have a working main branch deploying to Docker at all times. If you always have a working main branch, you will never be in jeopardy of receiving a very disappointing grade :-). Keep that main branch shining bright!

Let's embark on this epic coding adventure together and conquer the world of software engineering! You've got this, coding rockstars! 🚀🌟✨
