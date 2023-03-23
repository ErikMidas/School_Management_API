
<!-- Back to Top Navigation Anchor -->
<a name="readme-top"></a>

<!-- Project Shields -->
<div align="center">

  [![Contributors][contributors-shield]][contributors-url]
  [![Forks][forks-shield]][forks-url]
  [![Stargazers][stars-shield]][stars-url]
  [![Issues][issues-shield]][issues-url]
  [![MIT License][license-shield]][license-url]
  [![Twitter][twitter-shield]][twitter-url]
</div>

<!-- Project Intro -->

# A Typical School Management System API Built with Flask
---
<div>
  <p align="center">
    <a href="https://github.com/ErikMidas/Student_Management_API#readme"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="/images/sample.png">View Demo</a>
    ·
    <a href="https://github.com/ErikMidas/Student_Management_API/issues">Report Bug</a>
    ·
    <a href="https://github.com/ErikMidas/Student_Management_API/issues">Request Feature</a>
  </p>
</div>

---


<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about">About</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#lessons-learned">Lessons Learned</a>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#live-demo">Live Demo</a></li>
      </ul>
    </li>    
    <li><a href="#sample">Sample</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
  <p align="right"><a href="#readme-top">back to top</a></p>
</details>

---

<!-- About -->
## About

This Student Management API is one of the projects I've been able to craft with my coding skills. It was built as an exam project for Backend Engineering track using Python Flask framework at <a href="https://altschoolafrica.com/schools/engineering">AltSchool Africa</a>.

This is a school management system API built with Flask and Flask_RestX built by according to [this requirements](https://docs.google.com/document/d/19ayXN5P1oV2aqW_7-As6EUpn7OQShkpAlZK4wRbrgBQ/). It is a simple API that allows an Admin to perform CRUD operations on students and courses. It also allows you to register students to courses and add grade for students.

<p align="right"><a href="#readme-top">back to top</a></p>

### Built With:

![Python][python]
![Flask][flask]
![SQLite][sqlite]

<p align="right"><a href="#readme-top">back to top</a></p>

---
<!-- Lessons from the Project -->
## Lessons Learned

Creating this API helped me learn and practice:
* API Development with Python
* App Deployment with PythonAnywhere
* Testing with pytest and Insomnia
* Documentation
* Debugging
* Routing
* Database Management
* Internet Security
* User Authentication
* User Authorization

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- GETTING STARTED -->
## Usage

To get a local copy up and running, follow the steps below.

### Prerequisites

Python3: [Get Python](https://www.python.org/downloads/)

### Installation

1. Clone this repo
   ```sh
   git clone https://github.com/ErikMidas/Student_Management_API.git
   ```
2. Create a virtual environment
   ```sh
   python -m venv env
   ```
3. Activate the virtual environment
   ```sh
   source env/Scripts/activate
   ```
4. Install project packages
   ```sh
   pip install -r requirements.txt
   ```
5. Run Flask
   ```sh
   python runserver.py
   ```
6. Open the link generated in the terminal on a browser or visit [http://localhost:5000](http://localhost:5000)



---
### Live Demo
To interact with the live version of this API, follow these steps:

1. Open the PythonAnywhere web app on your browser: https://erikmidas.pythonanywhere.com

2. Create an admin or student account:
   * Click "admin" to reveal a dropdown menu of administration routes, then register an admin account via the "/admin/register" route
   * Click "students" to reveal a dropdown menu of student routes, then register a student account via the "/students/register" route
   
3. Sign in via the "/auth/login" route to generate a JWT token. Copy this access token without the quotation marks

4. Scroll up to click "Authorize" at top right. Enter the JWT token in the given format, for example:
   ```sh
   Bearer this1is2a3rather4long5hex6string
   ```
5. Click "Authorize" and then "Close"

6. Now authorized, you can create, view, update and delete students, courses, grades and admins via the many routes in "students", "courses" and "admin". You can     also get:
    * All students taking a course
    * All courses taken by a student
    * A student's grades in percentage (eg: 84.8%) and letters (eg: A)
    * A student's CGPA, calculated based on all grades from all courses they are taking

7. When you're done, click "Authorize" at top right again to then "Logout"

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Sample Screenshot -->
## Sample

<br />

<img src="/images/sample.png" alt="sample"/>

<br />

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- License -->
## License

Distributed under the MIT License. See <a href="https://github.com/ErikMidas/Student_Management_API/blob/main/LICENSE">LICENSE</a> for more information.

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Contact -->
## Contact

Ayodeji Okulaja - [@Koats14](https://twitter.com/koats14) - ayotoku@gmail.com

Project Link: [PythonAnywhere](https://erikmidas.pythonanywhere.com/)

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Acknowledgements -->
## Acknowledgements

This project was made possible by:

* [AltSchool Africa School of Engineering](https://altschoolafrica.com/schools/engineering)
* [Caleb Emelike's Flask Lessons](https://github.com/CalebEmelike)

<p align="right"><a href="#readme-top">back to top</a></p>

---

<!-- Markdown Links & Images -->
[contributors-shield]: https://img.shields.io/github/contributors/ErikMidas/AltSch_Exam_Project.svg?style=for-the-badge
[contributors-url]: https://github.com/ErikMidas/AltSch_Exam_Project/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ErikMidas/AltSch_Exam_Project.svg?style=for-the-badge
[forks-url]: https://github.com/ErikMidas/AltSch_Exam_Project/network/members
[stars-shield]: https://img.shields.io/github/stars/ErikMidas/AltSch_Exam_Project.svg?style=for-the-badge
[stars-url]: https://github.com/ErikMidas/AltSch_Exam_Project/stargazers
[issues-shield]: https://img.shields.io/github/issues/ErikMidas/AltSch_Exam_Project.svg?style=for-the-badge
[issues-url]: https://github.com/ErikMidas/AltSch_Exam_Project/issues
[license-shield]: https://img.shields.io/github/license/ErikMidas/AltSch_Exam_Project.svg?style=for-the-badge
[license-url]: https://github.com/ErikMidas/AltSch_Exam_Project/blob/main/LICENSE.txt
[twitter-shield]: https://img.shields.io/badge/-@koats14-1ca0f1?style=for-the-badge&logo=twitter&logoColor=white&link=https://twitter.com/koats14
[twitter-url]: https://twitter.com/koats14
[midas-blog-screenshot]: /static/images/Midas%20Blog.png
[python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[jinja]: https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black
[html5]: https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white
[css3]: https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white
[sqlite]: https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white
