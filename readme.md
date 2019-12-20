# Sara Akhtar's Flask Book Catalogue Project

## Overview

This project focuses on the CRUD method when dealing with databases, and primarily uses Flask. 

On the home page the top five rated books are shown, as well as being separated into either fiction or non-fiction books. 

This website doesn’t as of yet have username abilities, therefore I created certain books that can’t be deleted, which can be seen when clicking on the book for its full details. This was to ensure that the database wouldn’t be completely empty. 

----------------------
### An issue that had arisen during commits

On Github it states that there are 2 contributors. The reason for this is because when I initially set up this repository and made my first commit, it stated that the author of that commit was usernameusername. After researching what the issue was, I found it was due to my email address being on private. When I fixed the issue Github successfully starting recording my username when committing, however the first commit I made during the issue could not be fully deleted. Therefore I am the only contributor to this project.  

The files that were affected and were committed when there was a fault with the username were: requirements.txt and app.py during initial commit. 
 

## UX and UI

I wanted to create a simple UX and UI design that was easy to use. I used wireframes in order to ensure this was achieved. I also wanted to create a mobile first and responsive website that responded to various screen sizes. 

## Features

* The CRUD process has been established in this project, allowing the user to create, read, update and delete books
    - Editing a book will allow it to be deleted if it has the 'delete_book = true' hidden value. 
* Search capability 
* Books are sorted;
    - Some based on author’s name, with others based on rating.
* Used jQuery to add hover elements and add other aesthetic qualities.
* Users can upload an image 
    - If the image hasn’t uploaded correctly they are asked if they would like to add a link to a website for the image.
    - If there is already a link to a website, then the message displayed will change and instead provide them with a link to this website.

### Features left to implement 

* I would like to experiment with Javascript to see how it can further be used to enhance the usability of a website.
* Develop username capabilities.
* Allow users to comment on books, and leave their own reviews.
* Experiment with other ways users can add images in order to make it easier.
* I would like to experiment with AJAX, such as applying functions without having the page to reload. 

## Methods used

1. HTML
2. CSS
3. Bootstrap  
4. Javascript & jQuery 
5. Flask
6. Font Awesome - used for icons

## Testing techniques 

When testing the code for this website http://jshint.com, manual testing and Google’s responsive web tester were implemented. 

### Manual testing

* https://chrome.google.com/webstore/detail/responsive-web-design-tes/bdpelkpfhjfiacjeobkhlkkgaphbobea.
This chrome plug in was used when testing HTML and CSS to assess the responsiveness of the website on different screen sizes. 
* I also tested the website on different browsers.


## Deployment

Github and Heroku were both used for deployment.

## Credits

### Media

* The images used for this project have been obtained from Google and Amazon.
* Waterstones was used as an example when adding a website link for a book.


### Acknowledgements 


**This is for educational purposes**