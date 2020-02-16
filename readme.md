# Sara Akhtar's Flask Book Catalogue Project

Heroku live website link:

https://sara-book-project.herokuapp.com

## Overview

This Flask project is a responsive website that utilizes mongoDB. The CRUD method has been implemented, therefore users have the ability to create, read, update and delete books from the database. 

I experimented with some of the different features and capabilities of mongoDB, therefore the home page displays the top three rated books for both fiction and non-fiction books.

Currently there aren’t any username capabilities for this website. In order to ensure the database couldn’t be left empty, I created a certain number of books that couldn’t be deleted. I achieved this by creating a hidden value and an automatic input for the books I didn’t want to delete, and for new books created.  

----------------------
### An issue that had arisen during commits - caused an error relating to contributors 

On Github there is an error whereby it states there are 2 contributors. The reason for this is because when I initially set up this repository and made my first commit, it stated that the author of that commit was usernameusername. After researching what the issue was, I found it was due to my email address being on private which meant Github was unable to recognise my username. When I fixed the issue Github successfully starting recording my username when committing, however the first commit I made during the issue could not be fully deleted and rectified. Therefore I am the only contributor to this project.  

The files that were affected during initial commit when there was a fault with the username were: 
* requirements.txt
* app.py

### Potential issue with how images are stored

Currently images aren’t stored locally. Images are displayed based on the url that users upload, and taking that image from the Internet. This could then cause potential issues, whereby if this image were to no longer be available, then it would cause a broken image file to be shown. 

For the sake of this project, this method for storing images has been kept, however in the future I would like to incorporate a system that would allow images to be stored locally. 

## UX and UI
* Identified during planning:
    - Who are my audience?
    - What do they want to achieve? 
    - Was it in line with what I wanted them to achieve? 

* My goals: 
    - Create a mobile first website that was responsive,
    - Build a website that is easy to understand and manoeuvre through, ensuring users can quickly identify the different areas of the website and perform the tasks they want to achieve:
        * Viewing different book categories, add/edit/delete a book, filter books etc. 
    - Have an appealing aesthetic.

* How was it achieved? 
    - I used Balsamiq to create wireframes in order to achieve these goals. 
    - Balsamiq allowed me to see how easy it was to see where everything was located, but also whether it was appealing for the user. 
    - Bootstrap column and row features allowed me to incorporate a mobile first design.
    - Manual testing was performed to ensure the website was responsive as intended.

### Wireframes
[View wireframes](wireframe/BookProject.pdf)

### User Stories

*Easily view books available to me*
*Add books I like and view them later*
*See which books are the most popular*
*Search through the different books*


## Features

* The CRUD process has been established in this project, allowing the user to create, read, update and delete books
    - Editing a book will allow it to be deleted if it has the 'delete_book = true' hidden value. 
    - When deleting a book, an alert is sent asking the user to confirm they would like to delete it. 
* Search filtering capability 
    - Users can filter books based on ratings and genre.
    - Users can also see which fiction and non-fiction books are in the database.
* Books are sorted;
    - Some based on author’s name, with others based on rating, depending on which page a user is on. 
* Used jQuery to add hover elements and add other aesthetic qualities.
* Users can upload an image or website link:
    - If the image upload was successful then there won’t be any mention of a website link. If the image hasn’t uploaded correctly then the user is asked if they would like to add a link to a website for the image instead. On the website I have used the Waterstones website as an example for the Sherlock Holmes book. 
    - If there is already a link to a website uploaded, then the message displayed will change and instead provide them with a link to this website.
    - As is mentioned below in the features left to implement section, an alternative method to image uploading is something that I would like to feature in order to avoid such issues.
* Interaction with users 
    - When a user clicks on a book and has its full details displayed, if applicable, books with a similar genre will also be presented at the bottom of the page.
* Used pagination for certain pages so there weren’t too many books displayed on one page.
* I developed a genre category for books classified as ‘other’: 
    - This was identified as a need during the testing process. 
    - If users add a book with a genre that isn’t recognised as a pre-selected genre type for a fiction or non-fiction book then it will be categorised with a genre of ‘other’. 
        - i.e. A non-fiction book with a fiction genre or a fiction book with a non-fiction genre. 

### Features left to implement 

* Breadcrumb navigation:
    - So I can have more control over redirects i.e. after deleting a book I would like the user to be redirected to the page they previously were on. 
* I want to learn more about added security features for the backend and different types of validation that can be used in this context.
* I would like to experiment with Javascript to see how it can further be used to enhance the usability of a website.
* Develop username capabilities.
* Allow users to comment on books, and leave their own reviews.
* Create a better method for image storage:
    - Experiment with other ways users can add images in order to make it easier and accurate without having to rely on the correct image url being uploaded. This will also prevent broken images on the website.
    - Develop a method to store images locally, therefore gaining control.
* I would like to experiment with AJAX, such as applying functions without having the page reload. 
* Change the way ratings are handled: 
    - Users would be able to hover over stars and change the rating.
* I would like to create a method for users to sort how the books are displayed to them e.g. based on rating, name, most recent etc. 

## Methods used

1. HTML
2. CSS
3. Bootstrap  
4. Javascript & jQuery 
5. Flask
6. Font Awesome - used for icons

## Testing techniques 
* Overview: 
    - IDE console 
    - Developer tools 
    - Manual testing 

### Manual testing
> Front-end 
* https://chrome.google.com/webstore/detail/responsive-web-design-tes/bdpelkpfhjfiacjeobkhlkkgaphbobea.
    - This chrome plug in was used when testing HTML and CSS to assess the responsiveness of the website on different screen sizes. 
* I also tested the website on different browsers:
    - Safari
    - Chrome
    - Firefox
* Ensured books were displayed as intended:
    - Correctly separating fiction and non-fiction books
    - Top 5 rated books were displayed on the home page, and only those books with a 4 or 5 star rating.
* Tested images:
    - Images were displayed correctly, especially when an image wasn't uploaded correctly. 
* W3C code validator was used to check the HTML portions of code.
* Tested the email icon in the navbar successfully redirects the user to their mail service 
    – This currently acts as the contact method for the website set up with an example email address. 

> Back-end
* I tried entering data that was outside what was expected to try and break the code, which helped identify what safeguards needed to be in place: 
    - This helped identify the need for having ‘other’ as a genre option, as when I entered books with genre types that didn’t match the fiction or non-fiction genre pre-sets, those books would not be able to be filtered.
* I manually tested all functions 
    - Includes testing forms by adding and editing books. I tested the delete function and ensured the confirmation message before deletion was working correctly. 
    - All search/filter functions were tested by manually filtering books and ensuring the correct ones were identified.  
* To test JavaScript code: 
    - http://jshint.com


### Form validation 
* I wanted to confirm that all the forms were working as intended and had been validated. In order to do so I performed manual tests. These included:
    - Attempting to submit the add book form without any data present. This was to ensure that an error message was successfully displayed prompting the user to first input the required data. 
    - Editing a book and submitting the form without the necessary input details; again there was an error above the input field requesting the user enter the information.  

## Deployment

Github and Heroku were both used for deployment.

Heroku live website link:

https://sara-book-project.herokuapp.com

### Heroku deployment method:

1. Create a Heroku account: https://heroku.com.
2. Install the Heroku CLI on your machine: https://devcenter.heroku.com/articles/heroku-cli
3. Confirm the Heroku CLI has been installed correctly by seeing which Heroku version you are using: 
    ```sh
        heroku --version
    ```
4. Log in to Heroku from your terminal in order to connect to the Heroku CLI:
    ```sh
        heroku login
    ```
    - You will then be given instructions to follow in your command line.

### Loading my Heroku app on your local machine 

#### Github method 
1. Download the project to be used on your IDE:
    1. Download as a zip file
    OR
    2. Git clone the project 

2. Download the packages and requirements from the requirements.txt file:
    ```sh
        pip3 install -r requirements.txt 
    ```
3. Run the project:
    ```
        python3 -m flask run
    ```

## Credits

### Media
* The images used for this project have been obtained from Google, Waterstones and Amazon.
* Waterstones was used as an example when adding a website link for a book.

### Acknowledgements 
* Feedback from mentor: Dick Vlaanderen:
    - Advised using pagination
* Pagination: Online tutorial from Pretty printed and assistance from Slack member Shane Muir.
* Tutorials from CodingEntrepreneurs:  
    - Introduction to a 'confirm' alert window:  
        - I adapted this to work for my project whereby users are sent a confirm alert. 
* Certain book descriptions have been taken from Waterstones.


**This is for educational purposes**