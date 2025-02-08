
# Book Management and Commenting System - Disaster Research  Unit Bibliography

## Objective

This essential project enables end-users to create, read, update, and delete entries for book titles, thereby establishing a unique database on specific topics. The "review" option is important, too, allowing readers to engage in discussions and share their thoughts on individual books.


![Landing Page](./static/images/responsive%20design.png)


## Users' Benefits and Goals

- Product Owner: The website establishes a powerful tool for knowledge dissemination, networking activities, sharing and acquiring cutting-edge ideas on specific topics.

- Final Users can expect several benefits from using this digital product,
    
#### A) For the first-time user
 - dynamic digital platform to contribute to and/or navigate through the content of book entries 

#### For returning and frequent users

- a reliable source of the latest literature on the specific topic, a place to communicate with colleagues, learn what the scientific community members think on particular issues, or even their books that became part of this project.

## Design and Development

## Prehistory

- This is a continuation of a similar project whose development was interrupted due to family circumstances.  
[Book Management and Commenting System](https://github.com/VladaAlek/code_institute_django_pp_4 "Book Management and Commenting System"). At its core are these wireframes: 

[Landing Page](./static/images/landing_page.png)

[CRUD Page](./static/images/crud.png)

## Model Design and ERD

#### Bibliography Model

 - initial stage [ERD Bibliography](./static/images/ERD_Book.png)
 - final stage [ERD Bibliography](static/images/ERD_Bibliography_2.png)

The better usage of this model was achieved by introducing a slug field in the forms.py.

#### Review Model

 - initial stage [ERD Review](./static/images/ERD_Review.png)
 - final stage [ERD Review](static/images/ERD_Review_2.png)

## User Experience (UX) Section

### Main Features and Structure  

 **Home Page**

 The landing area is divided into two sections:
 - **a.** [Form Section LG](./docs/images/form%20index%20page.png);  [Form Section MD](./docs/images/form%20index%20page%20md.png); [Form Section SM](./docs/images/form%20index%20page%20sm.png) makes it possible for the loged user to enter the new book entry.



 In order to save space and improve UI, the form is [not visible after](./docs/images/form%20index%20page%202.png) the first page.

 - **b.** [Book Section LG](./docs/images/form%20index%20page%202%20lg.png); [Book Section MD](./docs/images/form%20index%20page%202%20md.png); [Book Section SM](./docs/images/form%20index%20page%202%20sm.png) displays an overview of the six books per single page, with the following data: title, author, time of entry creation, contributors' identity, and a book's summary.

 The logged-in user has visible [edit and delete buttons](./docs/images/form%20index%20page%202%20edit%20and%20delete.png), whose function is explained bellow: 
 
 The logged-in user has the option to edit his contribution: [Edit 1](./docs/images/Test%20edit%20book.png); [Edit 2](./docs/images/Test%20edit%20book%201.png); [Edit 3](./docs/images/Test%20edit%20book%202.png).

 The logged-in user have the option to delete it's contribution. The custom [modal](./docs/images/Test%20delete%20book.png) prevents non-intentional deletion.

Upon editing [edit 1](./docs/images/edit%20bibliography%20message.png) [edit 2 with message](./docs/images/edit%20bibliography%20message%201.png) [edit 3](./docs/images/edit%20bibliography%20message%202.png) or deleting [delete 1](./docs/images/delete%20book.png) [delete 2](./docs/images/delete%20book%201.png) [delete 3 with message](./docs/images/delete%20book%202.png) bibliographical units, the appropriate messageses popup. 
 
 
  **Book Details and Book Review Page**

  This page is reachable by clicking the words [Comment Here and Chat Icon](./docs/images/comment%20here.png) of each single book.
 
  This page is divided into two sections:
 - **a.** Book Description, containing Title, Author(s), Publishing Year, Publisher, "Created by" and "Created on" fields, as well as the Book's Summary fields. Only the [LG](./docs/images/individual%20book%20description%20LG.png) format contains the book image, while this feature is missing in the [MD](./docs/images/individual%20book%20description%20MD.png) and [SM](./docs/images/individual%20book%20description%20SM.png) formats to make content navigation easier for users.

 **Displaying Static and User-Generated Images:** If [custom capture](./docs/images/custom%20book's%20image.png) not uploaded, the [generic image](./docs/images/general%20book's%20image.png) showing project's logo is displyed. For now, it is possible to upload custom images only through the [Admin Panel](./docs/images/admin.png).

- **b.** Making, editing or deleting own reviews is allowed only for [logged in](./docs/images/no%20make%20edit%20delete%20review.png) users. However, the logged-in user can [leave, or edit/delete](./docs/images/make%20edit%20delete%20review.png) it's own review.

The editing process requires two steps: [Change the text of the original review and clicking](./docs/images/edit%20review.png) the button, which results in [Updated Review Content](./docs/images/edit%20review%201.png).

[edited review message](./docs/images/review%20edited.png)

[deleted review message](./docs/images/deleted%20review.png)

**Additional feature** The review's number [counter](./docs/images/review%20count.png) indicates the number of reviews.

 **About page**
 is divided into three sections:
 
 - a: two short textual explanations about the purpose of the project. One of them contains the link to the *Home* page to make the navigation easier, as illustrated in the capture "About LG", bellow. 
  
 - b: Capture featuring a forest fire—Further development.
[About LG](./docs/images/about_page.png); [About MD](./docs/images/about_page%20MD.png); [About SM](./docs/images/about_page%20SM.png); 


### Additional Features

#### Navigation
- *Home page* 1: by clicking on DRU Bibliography in navbar 2: Home link in navbar 3. 
- *About page* 1: About link in navbar. 
- *Home page* and *About page* availble in the so-called ["hamburger menu"](docs/images/links%20responsive.png) for the small-size screens: 
- *List of book navigation* - Next and Prev button introduced [Next Only](static/images/next_only.png); [Prev Next](static/images/prev_next.png); 
[Prev Only](static/images/prev_only.png);
- *Individual Book View* by clicking on the words: *Comment Here with Chat Icon* on the *Home page*


#### Footer

Links to the social platforms in the [footer](./docs/images/footer.png) are not active.

#### Authentification

All required functions have been incorporated. They are functional and styled, to improve the UX: 
[Register_Log In](static/images/register_login.png); [Log In](static/images/log_in.png); [Logged In](static/images/loged_in.png); [Sign Up](static/images/sign_up.png); 
[Sign Out](static/images/sign_out.png); [No_Log_No_Review](static/images/unloged_no_comments.png);


## CRUD Functionality
 - Create - [submitting new bibliographical units](./docs/images/create.png) on the *index page* and [submitting new review](./docs/images/create%201.png) on the *review detail* page.
 - Read - The user can see not only the list of [all books](./docs/images/read%20.png) but, specific details of [individual book](./docs/images/read%201.png).
 - Update - The user can update the content of a *bibliographical unit* or a *individual review* - detailed explanation in the section: **Home Page**, subsection *b*, and in **Book Details and Book Review Page**, subsection *b*.
 - Delete - The user can delete [individual reviews](./docs/images/delete%20review.png) or [individual book.](./docs/images/delete%20books.png)

[Delete confirmation modal Review](./static/images/Delete%20confirmation%20modal.png) and [Delete confirmation modal Book](./docs/images/book%20deletion%20modal.png) are operational in both cases.

## Messages
To improve UI, the appropriate messages emerges on the screen following user's **CRUD OPERATIONS**. A small button makes it possible for user to delete pop-messages.

- [summary saved successfully](./docs/images/summary%20saved%20successfully.png); 
- [review submitted](./docs/images/review%20submitted.png); 
- [review updated](./docs/images/review%20updated.png); 
- [comment deleted](./docs/images/comment%20deleted.png); 
- [delete comment question Review](./docs/images/delete%20comment%20question%20modal.png) and [Delete confirmation modal Book](./docs/images/book%20deletion%20modal.png) are  present to prevent the unwanted comment's deletions.


## Technologies Used
 -  *Frontend:* HTML, CSS, JS, Bootstrap
 -  *Backend:* Python, Django, SQL

## Software Used

- [Multi-mockup-generator](https://techsini.com/multi-mockup/index.php "Multi-mockup-generator") to create the mockup for responsive pages.

## External Code Source

- navbar in base.html, inspiration from: [Shaun (Net Ninja)](https://github.com/iamshaunjp/bootstrap-5-tutorial/blob/lesson-9/index.html "Shaun (Net Ninja)")
- responsive design in index.html and about.html, inspiration from: [Shaun (Net Ninja)](https://github.com/iamshaunjp/bootstrap-5-tutorial/blob/lesson-7/index.html "Shaun (Net Ninja)")

- footer in base.html, adapted and slightly changed from: [Code Institute](https://github.com/Code-Institute-Solutions/blog/blob/main/08_templates/01_base_template/base.html "Code Institute")

## Learning Resources Used
 - [GeeksforGeeks](https://www.geeksforgeeks.org/how-to-create-equal-height-columns-in-bootstrap/ "GeeksforGeeks") 
 - [StackOverflow](https://stackoverflow.com/questions/33934947/searching-by-username-field-in-django-admin/ "StackOverflow") 


## Deployment

- [ElephantSQL](https://www.elephantsql.com/  "ElephantSQL") to store database until 31.01.24. On that date, *Code Institute Postgres Database* have been used. 
- [Cloudinary](https://cloudinary.com/  "Cloudinary") to store images added by users.
- [Heroky](https://dashboard.heroku.com/  "Heroku") to deploy the project.
- [Github](https://github.com/  "Github") for recording coding history. Unfortunately, the [wrong branch](static/images/milestone%20and%20projects%20open%20in%20the%20wrong%20repo.png) is used to create the first milestone and resubmission project. The link to projects with milestones included, [here](https://github.com/users/VladaAlek/projects/24/views/1?pane=issue&itemId=96792055&issue=VladaAlek%7Cpp-commerce-261124%7C65 "link to the repo").
 
- [Github Brunches](https://github.com/VladaAlek/Django_17_06_24_really_good/branches  "Github Brunches") - important, because it contains all Projects.


### Testing

**manual testing** - All features of the project have been intensely tested during the development stage. All test actions are documented, here are some examples of the 
manual testing process: 
- [review submitted testing](static/images/review%20submited%20testing.png); [review submitted testing success](static/images/review%20submited%20testing%201.png); explanation: extra code added to target the precise success message. The captures show the initial and end stages of development.
- [book submitted testing success](static/images/book%20submited%20testing.png);

**automated testing**

**test_forms.py** [Test Results](./docs/images/test_forms.py.png) 

- *test_form_is_not_valid*:  With this test, we falsely assume that the form might be valid, but we actually know it is not (since the content is empty). The test passes successfully if is_valid() returns False, confirming that the form validation works correctly.
- *test_form_is_valid*: This test checks if the form is valid when all required fields are provided. It passes if is_valid() returns True, confirming that the form accepts correct input.

**test_view.py** [Test Results](./docs/images/test_view%20results.png) 
- The test verifies that the book detail page loads properly, displays the correct content, and includes a review form.

**test_post_book_view.py** [Test Results Failed](./docs/images/302%20assertion%20error.png); [Test Results Success](./docs/images/302%20assertion%20error%201.png);
- the test failed becaues it expects a 200 OK response, but since the view redirects (return redirect('book_detail', bibliography_id=bibliography_id)), it returns 302 Redirect instead. The refactored test asserts new condition, resulting in the successful test.

#### Validation
**HTML:**

- **index:** [Index No Errors](docs/images/index%20no%20errors.png);  [Index Overview](docs/images/index%20overview.png);  

- **review_details:** [Single View](docs/images/detail%20whole%20view.png).
In this document, the issues that are not connected to the specificity of the Django syntax addressed: [Stray end tag](./docs/images/Stray%20end%20tag.png); [Duplicate attribute](./docs/images/detail%20Duplicate%20Attribute.png); 

- **about:**  [About No Errors](docs/images/about%20no%20errors.png);  [About Overview](docs/images/about%20overview.png);

- **edit_bibliography:** [Edit Overview](docs/images/edit%20overview.png);

- **delete_bibliography:** [Delete Overview](docs/images/delete%20overview.png);

 **CSS:** 
 - [W3C](docs/images/css%20validation.png);

**JavaScript:**  
- [JSLint](docs/images/js%20validation%201.png) doesn't support all ESJ features, hence minor error reports. When possible, the raised issues addressed, for instance, the [too long](docs/images/js%20validation%202.png) text in the comments. For the validation, the [Esprima](https://esprima.org/demo/validate.htm "Esprima JS Validation Platform") software was used, too.
 
**Python** 
- the file "book/views.py" was checked in [Pythonium](https://pythonium.net/linter) validator, which gave this [report](docs/images/python%20validation.png).


#### Accessibility
- testing black/red [webaim.org](https://webaim.org/resources/contrastchecker/?fcolor=000000&bcolor=C52B2B "[webaim.org")
- testing white/red [webaim.org](https://webaim.org/resources/contrastchecker/?fcolor=FFFFFF&bcolor=C52B2B "[webaim.org")

### List of Major Unresolved Bugs

 - updated review keeps the original creation datum unchanged [creation datum unchanged](static/images/updated%20review%20original%20datum%20unchanged.png);

 - **Favicon** *not visible* in Firefox: [06/Aug/2024 08:31:59] "GET /4/ HTTP/1.1" 500 352382
Not Found: /favicon.ico. *Visible* in Edge and Chrome.
 
### Further improvement
 - there is a possibility to use slugs (book's keywords) instead of the object's id to improve the site's ranking in search engines.

## Captures and logos

 - Capture origin [Flickr Account of Christine Warner-Morin](https://www.flickr.com/photos/christinehawks/50353850332/in/photolist-2jHADpj-7kmiGy-2jHEru9-2jFJ9Y7-22P5zJg-of6wu8-NaF2Rd-ojVc2X-2hy4jKb-ayQ9Zd-2a3Fsxe-oY5g6v-4Qan5V-9E5p81-2jeowAb-8cnfe4-8cqAej-4wfLyv-8Y56Fj-2jFBPqN-cWFQTo-pNWvyC-9EkDQJ-vRtXnm-2k5qz8h-2mg9aBL-24PzNWS-jLRWD-7Deny4-8s5SFR-6KqwLt-2mtZSi1-DaQDT9-2kbz98Q-2iF8i2J-2jEWWFC-83hwXC-2nx2aAF-EZDYqS-6KuEas-2np5gAz-28Q8YfN-27aL8kh-cpQk6E-oR5RdZ-xxdRFb-6RTSvw-2jwwdXD-8kCBE2-wPXpbo "Flickr Account of Christine Warner-Morin")
 - "Orange Fire logo" origin [Freepik.com](https://www.freepik.com/free-vector/orange-fire-logo_35202562.htm#query=fire%20burn%20logo&position=29&from_view=keyword&track=ais_user&uuid=fb1e3f8f-07cb-4333-b537-b6ca4ad264fd  "Freepik.com")

## Acknowledgments
- super helpful members of the Student Support Team. Roman, Rebecca, Sarah, Thomas, Oisin and Alan, **thank you**!


