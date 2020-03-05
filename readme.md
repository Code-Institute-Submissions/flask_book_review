# Sara Akhtar's Flask Book Catalogue Project

Heroku live website link:

https://sara-book-project.herokuapp.com

## Overview

This Flask project is a responsive book catalogue website that utilizes mongoDB, as well as the CRUD method. Users have the ability to create, read, update and delete books from the database. 

I experimented with some of the different features and capabilities of mongoDB, for example the home page displays the top three rated books for both fiction and non-fiction books.

Currently there aren’t any username capabilities for this website. In order to ensure the database couldn’t be left empty, I created a certain number of books that couldn’t be deleted. I achieved this by creating a hidden value and an automatic input for the books I didn’t want to delete, and for new books created.  

The books that can’t be deleted are:
* The Institute - Stephen King
* Doctor Sleep - Stephen King
* Wolf Of Winter - John Connolly
* Astrophysics For People In A Hurry - Neil Degrasse Tyson
* Pinch Of Nom - Kate Allinson

----------------------
### An issue that had arisen during commits - caused an error relating to contributors 

On Github there is an error whereby it states there are 2 contributors, however I am the only contributor. The reason for this is because when I initially set up this repository and made my first commit, it stated that the author of that commit was usernameusername. After researching what the issue was, I found it was due to my email address being on private which meant Github was unable to recognise my username. When I fixed the issue Github successfully starting recording my username when committing, however the first commit I made during the issue could not be fully deleted and rectified. Therefore I am the only contributor to this project.  

The files that were affected during initial commit when there was a fault with the username were: 
* requirements.txt
* app.py

### Issue with images and website uploads - along with solutions
- Breakdown of issues regarding images and website uploads:
    * Currently images aren’t stored locally. Images are displayed based on the image address that a user uploads, and takes that image from the Internet. 
    * This upload method could cause potential issues:
        - If this image were to no longer be available, then it would cause a broken image file to be shown. 
    
    * Currently there isn’t any server side validation before a form is submitted:
        - If an error has occurred and an image upload has not been successful, then the if statement I created will give users the option to upload a website link instead. 
        - The site can also be left with a broken image if the user uploads an image with an invalid file type, or they upload the image in the website url area accidentally.
        - User can enter an invalid website which will cause an error if they attempt to click on it later.
        

- If a user does upload an invalid image type, I created a method to provide some validation to a certain extent. This involved creating a list with valid image file type endings. Images beginning with ‘data:image/’ are also classified as valid and will produce an image on the website, which is something I discovered through testing. If an image is uploaded that doesn’t begin with ‘data:image/’ and end in the valid file types, then the if statement I created will add this image to a list called invalid_image that will be accessed later, and will be used to display the default image I have added rather than a broken image. 
- The message displayed to the user will also change accordingly, and could offer some clarification as to why they may be experiencing issues with their image or website link, and prompt them to try again.
- The original if statement only dealt with the main image displayed on the full book details page. A separate function needed to be made in order to deal with an invalid book image across the different webpages. 
    * I created a function called ‘invalid_image_function’ that will be used globally to handle this issue. 

- This method does however have its limits as some websites have their images ending with fit measurements. 
- I have also created my own error 500 page so as to give the user some kind of information regarding why they may be facing issues with images or their website link. 
 
For the sake of this project, this method for storing images has been kept, however in the future I would like to incorporate an alternative method for uploading images, such as using a file input and storing them locally. I would also like to work towards providing server-side validation in order to prompt the user if a file or any of the information provided is invalid before submitting the form. 

### Pagination absent for ratings and genre filter
Currently pagination hasn’t been applied when displaying rating and genre filter results. This has purposefully been decided as in the future I would like to alter the way books are filtered, whereby users can filter books based on multiple requirements, as opposed to currently where only one filter parameter can be done at a time. 

My mentor and I decided that this reasoning worked best for the sake of this project, especially since I have already proven my ability to use pagination throughout the rest of this project. 

## UX and UI

### Wireframes
[View wireframes](wireframe/BookProject.pdf)


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
    - I worked through the user stories to understand the core reasoning for this website. This gave the planning process a vision and purpose, and also helped steer the designing process. 
    - I used Balsamiq to create wireframes in order to achieve these goals. 
    - Balsamiq allowed me to see how easy it was to see where everything was located, but also whether it was appealing for the user. 
    - Bootstrap column and row features allowed me to incorporate a mobile first design.
    - Manual testing was performed to ensure the website was responsive as intended and allowed the user to perform the tasks the website provided and reach their goals.


### User Stories

- *Easily view all books available to me*
- *Add books I like and view them later*
- *See which books are the most popular*
- *Search through the different books available*


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
    - If the image upload was successful then there won’t be any mention of a website link. If the image hasn’t uploaded correctly then the user is asked if they would like to add a link to a website for the image instead. 
    - If there is already a link to a website uploaded, then the message displayed will change and instead provide them with a link to their website link.
    - On the website I have used the Waterstones website as an example for the book "The Binding" by Bridget Collins. If the book image is deleted then the website link will automatically appear under the default image. 
    - As is mentioned below in the features left to implement section, an alternative method to image uploading is something that I would like to feature in order to avoid issues from occurring.

* Interaction with users 
    - When a user clicks on a book and has its full details displayed, if applicable, books with a similar genre will also be presented at the bottom of the page.

* Used pagination for certain pages so too many books weren't displayed on one page.

* I developed a genre category for books classified as ‘other’: 
    - This was identified as a need during the testing process. 
    - If users add a book with a genre that isn’t recognised as a pre-selected genre type for a fiction or non-fiction book then it will be categorised with a genre of ‘other’. 
        - i.e. A non-fiction book with a fiction genre or a fiction book with a non-fiction genre. 

### Features left to implement 

* Create a better method for image storage:
    - Experiment with other ways users can add images in order to make it easier and accurate without having to rely on the correct image url being uploaded. This will also prevent broken images on the website.
    - Develop a method to store images locally, therefore gaining control.
    - This will also prevent users from inputting a website url in the image upload section and vice versa. 

* Breadcrumb navigation:
    - So I can have more control over redirects e.g. after deleting a book I would like the user to be redirected to the page they previously were on. 

* Increased server-side and back-end validation:
    - I want to learn more about added security features for the backend and different types of validation that can be used in this context.
    - Allow the server to acknowledge whether the text or file type that is uploaded is correct, and alerting the user if it isn’t.
    - Allow the server to see whether the correct piece of information has been entered for that section. E.g. a website address for the website url, an image for the image upload etc. 

* I would like to experiment with Javascript to see how it can further be used to enhance the usability of a website.

* I would like to experiment with AJAX, such as applying functions without having the page reload. 

* Develop username capabilities.

* Allow users to comment on books, and leave their own reviews.

* Change the way ratings are handled: 
    - Users would be able to hover over stars and change the rating rather than having to be redirected to the edit page function.

* I would like to create a method for users to sort how the books are displayed to them e.g. based on rating, name, most recent etc. 

* Add more sophisticated methods when filtering books e.g. filtering based on multiple requirements such as both genre and ratings. 

* Alert the user if they are trying to add a book that is already in the database. This is something that had arisen during testing, where I was able to add the same book twice.

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
    - This chrome plug-in was used when testing HTML and CSS to assess the responsiveness of the website on different screen sizes. 

* I also tested the website on different browsers:
    - Safari
    - Chrome
    - Firefox

* Ensured books were displayed as intended:
    - Correctly separating fiction and non-fiction books
    - Top 5 rated books were displayed on the home page, and only those books with a 4 or 5 star rating.

* W3C code validator was used to check the HTML portions of code.

* Tested the email icon in the navbar successfully redirects the user to their mail service 
    – This currently acts as the contact method for the website set up with an example email address. 

> Back-end
* I tried entering data that was outside what was expected to try and break the code, which helped identify what safeguards needed to be in place: 
    - This helped identify the need for having ‘other’ as a genre option, as when I entered books with genre types that didn’t match the fiction or non-fiction genre pre-sets, those books would not be able to be filtered.

* I manually tested all functions 
    - Includes testing forms by adding and editing books. I tested the delete function and ensured the confirmation message before deletion was working correctly. 
    - All search/filter functions were tested by manually filtering books and ensuring the correct ones were identified. 

* Image testing: 
    - Images were displayed correctly if the image ended in the file types outlined in app.py.
    - Added images with the wrong file type.
    - Added invalid images.
    - Input image in the wrong input area.
    - Uploaded a book without an image.
    - Lead to the creation of fun little pages for 404 and 500 page errors. 

* To test JavaScript code: 
    - http://jshint.com


### Form validation 
* I wanted to confirm that all the forms were working as intended and had been validated. In order to do so I performed manual tests. These included:
    - Attempting to submit the add book form without any data present. This was to ensure that an error message was successfully displayed prompting the user to first input the required data. 
    - Editing a book and submitting the form without the necessary input details; again there was an error above the input field requesting the user enter the information. 
    - Inputting data in the wrong fields. This highlighted issues with image and website url uploads which lead to their solutions outlined below.
        * I added an image into the website option and vice versa, and also added an image into the book description area. 
        * I attempted to upload an invalid image.

        * Doing so raised the need for further server-side validation. Currently the user isn’t prompted with an alert if they enter information that isn’t the valid type for that input section, for example if they enter a website address into the image upload section. The server also won’t check if the information is valid before submitting the form, for example the user may enter an invalid website address. They will then be met with an error if they attempt to click on this link later. Therefore, as previously mentioned, server-side validation is something I want to incorporate in the future. 

### Overview of issues and solutions identified during testing
- Image uploads: 
    * **Issue 1**: An invalid image may be uploaded causing a broken image to be shown.
    * Solution 1: Users are given the opportunity to upload a website link instead.
    * Solution 2: Created an if statement in app.py to check if a file is valid and display a default image for invalid images, and a message to the user according to what is returned. 
    * Solution 3: Created a function that would be used globally to also identify whether a book had an invalid or valid image uploaded. This would display the default image rather than causing a broken image to be shown.   

    * **Issue 2**: User could accidentally add the image url in the book description. This affected the text wrapping whereby the text would overlap with the image. 
    * Solution: Added hyphens so text would be forced to wrap even if it meant breaking the word. 

- Website links:
    * **Issue**: Link may be invalid.
    * Solution: Custom error 500 page has been created. They are noted of an issue, and are given a suggestion to check if their information is valid. 

- I had pre-set genres for fiction and non-fiction books:
    * **Issue**: If a user added a book with a genre that wasn’t within the pre-set list, then the book couldn’t be filtered.
    * Solution: Added logic to recognise a book that was added outside of these genre pre-sets and classified them as ‘other’. I then created ‘other’ as an option when attempting to filter books. 

- Book description:
    * **Issue**: Originally I had the first letter capitalized using the capitalize filter in jinja, but I noticed this would then force other letters within the description to be lowercase. 
    * Solution: Created my own method to store the book description using:
    
        ``` sh
            for k,v in book.items():
                if k == 'book_info':
                    info.append(v[0].capitalize() + v[1:])
        ```

- Book name length:
    * **Issue**: If the book name was too long it would affect the layout of that specific book when next to others. 
    * Solution: Added a custom class to the book name as well as author name, utilising the ellipses feature. 

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

3. Set config variables 
    - The secret key will need to be assigned personally as the details are hidden

4. Run the project on your local machine for development purposes using: 
    ```sh
        python3 -m flask run

        or

        python3 app.py
    ```

## Credits

### Media
* The images used for this project have been obtained from Google, Waterstones and Amazon.
* Waterstones was used as an example when adding a website link for a book.

### Acknowledgements 
* Feedback from mentor: Dick Vlaanderen:
    - Also advised using pagination
* Pagination: Online tutorial from Pretty printed and assistance from Slack member Shane Muir.
* Tutorials from CodingEntrepreneurs:  
    - Introduction to a 'confirm' alert window:  
        - I adapted this to work for my project whereby users are sent a confirm alert. 
* Book descriptions have been taken from Waterstones.


**This is for educational purposes**