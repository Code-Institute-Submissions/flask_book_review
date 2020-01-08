# Sara Akhtar's Flask Book Catalogue Project

## Overview

This Flask project is a responsive website that utilizes mongoDB. The CRUD method has been implemented, therefore users have the ability to create, read, update and delete books from the database. 

I experimented with some of the different features and capabilities of mongoDB, therefore the home page displays the top five rated books for both fiction and non-fiction books.

Currently there aren’t any username capabilities for this website. In order to ensure the database couldn’t be left empty, I created a certain number of books that couldn’t be deleted. I achieved this by creating a hidden value and an automatic input for the books I didn’t want to delete, and for new books created.  

----------------------
### An issue that had arisen during commits

On Github there is an error whereby it states there are 2 contributors. The reason for this is because when I initially set up this repository and made my first commit, it stated that the author of that commit was usernameusername. After researching what the issue was, I found it was due to my email address being on private which meant Github was unable to recognise my username. When I fixed the issue Github successfully starting recording my username when committing, however the first commit I made during the issue could not be fully deleted and rectified. Therefore I am the only contributor to this project.  

The files that were affected during initial commit when there was a fault with the username were: 
* requirements.txt
* app.py
 

## UX and UI

I wanted to create a simple UX and UI design that was easy to use. I used wireframes in order to ensure this was achieved. I also wanted to create a mobile first and responsive website that responded to various screen sizes. 

## Features

* The CRUD process has been established in this project, allowing the user to create, read, update and delete books
    - Editing a book will allow it to be deleted if it has the 'delete_book = true' hidden value. 
* Search capability 
    - Users can search based on ratings and genre.
    - Users can also see which fiction and non-fiction books are in the database.
* Books are sorted;
    - Some based on author’s name, with others based on rating, depending on which page a user is on. 
* Used jQuery to add hover elements and add other aesthetic qualities.
* Users can upload an image 
    - If the image hasn’t uploaded correctly they are asked if they would like to add a link to a website for the image. On the website I have used the Waterstones website as an example. 
    - If there is already a link to a website uploaded, then the message displayed will change and instead provide them with a link to this website.
* Interaction with users 
    - When a user clicks on a book and has its full details displayed, if applicable, books with a similar genre will also be presented at the bottom of the page.

### Features left to implement 

* I would like to experiment with Javascript to see how it can further be used to enhance the usability of a website.
* Develop username capabilities.
* Allow users to comment on books, and leave their own reviews.
* Experiment with other ways users can add images in order to make it easier, and not having to rely on the correct image url being uploaded.
* I would like to experiment with AJAX, such as applying functions without having the page reload. 

## Methods used

1. HTML
2. CSS
3. Bootstrap  
4. Javascript & jQuery 
5. Flask
6. Font Awesome - used for icons

## Testing techniques 

When testing the code for this website http://jshint.com, manual testing and Google’s responsive web tester were utilized. 

### Manual testing

* https://chrome.google.com/webstore/detail/responsive-web-design-tes/bdpelkpfhjfiacjeobkhlkkgaphbobea.
    - This chrome plug in was used when testing HTML and CSS to assess the responsiveness of the website on different screen sizes. 
* I also tested the website on different browsers.


## Deployment

Github and Heroku were both used for deployment.

## Credits

### Media

* The images used for this project have been obtained from Google and Amazon.
* Waterstones was used as an example when adding a website link for a book.


### Acknowledgements 


**This is for educational purposes**