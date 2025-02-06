
# Book Management and Commenting System - Disaster Research  Unit Bibliography

## Objective

This basic project enables end-users to create, read, update, and delete entries for book titles , thereby establishing a unique database on specific topics. The "review" option is important too, allowing readers to engage in discussions and share their thoughts on individual books.


![Landing Page](./static/images/responsive%20design.png)


## Users Benefits and Goals

- Product Owner 
    the website establishes a powerful tool for knowledge dissemination, networking activities, sharing and acquiring cutting-edge ideas on specific topics.

- Final Users can expect several benefits from using this digital product
    
#### A) For the first-time user
 - dynamic digital platform to contribute to and/or navigate through the content of book entries 

#### For returning and frequent users

- a reliable source of the latest literature on the specific topic, a place to communicate with colleagues, learn what the scientific community members think on particular issues, or even their books that became part of this project.

## User Experience (UX) Section

### Main Features and Structure  

 **Home Page**

 The landing area is devided in two sections:
 - **a.** [Form Section LG](./docs/images/form%20index%20page.png);  [Form Section MD](./docs/images/form%20index%20page%20md.png); [Form Section SM](./docs/images/form%20index%20page%20sm.png) makes it possible for the loged user to enter the new book entry.



 To save space and improve UI, the form is [not visible after](./docs/images/form%20index%20page%202.png) the first page.

 - **b.** [Book Section LG](./docs/images/form%20index%20page%202%20lg.png); [Book Section MD](./docs/images/form%20index%20page%202%20md.png); [Book Section SM](./docs/images/form%20index%20page%202%20sm.png) displays an overview of the six books per single page, with the following data: title, author, time of entry creation, contributors' identity, and a book's summary.

 The loged-in user have visible [edit and delete buttons](./docs/images/form%20index%20page%202%20edit%20and%20delete.png), whose function is explaned bellow: 
 
 The logged-in user have the option to edit it's contribution: [Edit 1](./docs/images/Test%20edit%20book.png); [Edit 2](./docs/images/Test%20edit%20book%201.png); [Edit 3](./docs/images/Test%20edit%20book%202.png).

 The logged-in user have the option to delete it's contribution. The custom [modal](./docs/images/Test%20delete%20book.png) prevents non-intentional deletion.

Upon editing [edit 1](./docs/images/edit%20bibliography%20message.png) [edit 2 with message](./docs/images/edit%20bibliography%20message%201.png) [edit 3](./docs/images/edit%20bibliography%20message%202.png) or deleting [delete 1](./docs/images/delete%20book.png) [delete 2](./docs/images/delete%20book%201.png) [delete 3 with message](./docs/images/delete%20book%202.png) bibliographical units, the appropriate messageses popup. 
 
 
  **Book Details and Book Review Page**

  This page is reachable by clicking words [Comment Here and Chat Icon](./docs/images/comment%20here.png) of each single book.
 
  This page is devided in two sections:
 - **a.** Book Description, containig Title, Author(s), Publishing Year, Publisher, "Created by" and "Created on", as well es Book's Summary fields. Only [LG](./docs/images/individual%20book%20description%20LG.png) format contains the immage of the book, while this feature is missing in the [MD](./docs/images/individual%20book%20description%20MD.png) and [SM](./docs/images/individual%20book%20description%20SM.png) formats to make the content navigation easier to the users.

- **b.** Making, editing or deleting own reviews is allowed only to [logged in](./docs/images/no%20make%20edit%20delete%20review.png) users. However, the logged in user can [leave, or edit/delete](./docs/images/make%20edit%20delete%20review.png) it's own review.

Editing process requires two steps: [Change the text of the original review and clicking](./docs/images/edit%20review.png) button, which results in [Updated Review Content](./docs/images/edit%20review%201.png) .

[edited review message](./docs/images/review%20edited.png)

[deleted review message](./docs/images/deleted%20review.png)

**additional feature** The review'number [counter](./docs/images/review%20count.png) indicates the number of reviews.

 **About page**
 is divided into three sections:
 
 - a: two short textual explanation about the purpose of the project. This section contains the link to the *Home* page to make the navigation easier. 
  
 - b: Capture featuring a forest fire—Further development.
[About LG](./docs/images/about_page.png); [About MD](./docs/images/about_page%20MD.png); [About SM](./docs/images/about_page%20SM.png); 


### Additional Features

#### Navigation
 - *Home page* 1: by clicking on DRU Bibliography in navbar 2: Home link in navbar 3: 
 - *List of book navigation* - Next and Prev button introduced [Next Only](static/images/next_only.png); [Prev Next](static/images/prev_next.png); 
[Prev Only](static/images/prev_only.png);
- *Individual Book View* by clicking on the words *Comment Here with Chat Icon* on the *Home page*
- *About page* 1: About link in navbar


#### Footer

Links to the social platforms in the [footer](./docs/images/footer.png) are not active.

#### Authentification

All required functions have been incorporated. They are functional and styled, when possible, to improve the UX: 
[Register_Log In](static/images/register_login.png); [Log In](static/images/log_in.png); [Loged In](static/images/loged_in.png); [Sign Up](static/images/sign_up.png); 
[Sign Out](static/images/sign_out.png); [No_Log_No_Review](static/images/unloged_no_comments.png);

#### Displaying Static and User-Generated Images

- please check the detail view  *"At Risk: Natural Hazards, People's Vulnerability and Disasters"* on the *Home page*: [User-Generated Images](static/images/featured_image.png);


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

#### Review Model

 - initial stage [ERD Review](./static/images/ERD_Review.png)
 - final stage [ERD Review](static/images/ERD_Review_2.png)


## CRUD Functionality
 - Create - [submitting new bibliographical units](./static/images/new_biblio_unit_submitted.png)
 - Read - The user can see not only the list of books but each book 
 - Update - The user can update individual reviews. For this and Delete points, the explanation is attached:  
 [Delete and Edit Bugs 1](./static/images/list%20of%20noticed%20bugs_page1.jpg); 
 [Delete and Edit Bugs 2](./static/images/list%20of%20noticed%20bugs_page2.jpg);  
 [Delete and Edit Bugs 3](./static/images/list%20of%20noticed%20bugs_page3.jpg); 
 - Delete - The user can delete individual reviews. *Delete confirmation modal* is operational: [Delete confirmation modal](./static/images/Delete%20confirmation%20modal.png)

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

#### list of used book reviews:
 - https://www.preventionweb.net/files/670_72351.pdf
 - https://www.researchgate.net/publication/227704544_Climate_change_and_the_imagination
 - https://academic.oup.com/book/40836
 - https://nap.nationalacademies.org/catalog/13457/disaster-resilience-a-national-imperative
 - https://www.amazon.de/-/en/David-Alexander/dp/1857280938
 - https://www.routledge.com/Natural-Disasters/Alexander/p/book/9781857280944
 - https://www.amazon.com/Disaster-Research-Multidisciplinary-International-Perspectives/dp/1138051616
 - https://https://www.sciencedirect.com/science/article/pii/S2590061724000279
 - https://www.amazon.de/-/en/Dr-Allen-Beattie/dp/B0CLH4J3SZ
 - https://books.google.de/books/about/El_Ni%C3%B1o_Ready_Nations_and_Disaster_Risk.html?id=O1piEAAAQBAJ&source=kp_book_description&redir_esc=y


## Deployment

- [ElephantSQL](https://www.elephantsql.com/  "ElephantSQL") to store database until 31.01.24. On that date, *Code Institute Postgres Database* have been used. 
- [Cloudinary](https://cloudinary.com/  "Cloudinary") to store images added by users
- [Heroky](https://dashboard.heroku.com/  "Heroku") to deploy the project
- [Github](https://github.com/  "Github") for recording coding history. Unfortunately, the [wrong repo](static/images/milestone%20and%20projects%20open%20in%20the%20wrong%20repo.png) is used to create the first milestone and project. The link to this milestone, [here](https://github.com/users/VladaAlek/projects/24/views/1 "link to the repo")
 

- [Github Brunches](https://github.com/VladaAlek/Django_17_06_24_really_good/branches  "Github Brunches") - important, because it contains all Projects.

## Messages
To improve UI, the appropriate messages emerges on the screen following user's **CRUD OPERATIONS**. A small button makes it possible for user to delete pop-messages.

- [summary saved successfully](./docs/images/summary%20saved%20successfully.png); 
- [review submitted](./docs/images/review%20submitted.png); 
- [review updated](./docs/images/review%20updated.png); 
- [comment deleted](./docs/images/comment%20deleted.png); 
- [delete comment question modal](./docs/images/delete%20comment%20question%20modal.png) is present to prevent the unwanted comment's deletions


[CSS Index](static/images/CSS_index.png);

### Testing

- [review submitted testing](static/images/review%20submited%20testing.png); [review submitted testing success](static/images/review%20submited%20testing%201.png); explanation: extra code added to target the precise success message. The captures show the initial and end stages of development.
- [book submitted testing success](static/images/book%20submited%20testing.png);

#### Validation

*Manual*
- CSS
[CSS Index](static/images/CSS_index.png); [CSS About](static/images/CSS_about.png); [CSS Single View](static/images/CSS%20single%20view.png);
- HTML
[Index](static/images/validation%20index%20.png); [About](static/images/validation%20about.png); [Single View](static/images/validation%20single%20view.png); [Registration](static/images/validation%20register.png); [Create Review](static/images/validation%20review%20creation.png);
- JavaScript JSLint doesn't support all ESJ feat; hence minor error reports [Jslint](static/images/jslint.png). When possible, the raised issues addressed - too long text in the comments;
- Python [Pythonium](https://pythonium.net/linter)

*Automatic*

- conducted in a few cases

#### Accessibility
- testing black/red [webaim.org](https://webaim.org/resources/contrastchecker/?fcolor=000000&bcolor=C52B2B "[webaim.org")
- testing white/red [webaim.org](https://webaim.org/resources/contrastchecker/?fcolor=FFFFFF&bcolor=C52B2B "[webaim.org")

### List of major Bugs

#### Resolved
- 

#### Unresolved

 - updated review keeps the original creation datum unchanged [creation datum unchanged](static/images/updated%20review%20original%20datum%20unchanged.png);

 - **Favicon** *not visible* in Firefox: [06/Aug/2024 08:31:59] "GET /4/ HTTP/1.1" 500 352382
Not Found: /favicon.ico. *Visible* in Edge and Chrome.
 - deleted bibliographic unit still visible in the list [Not Deleted](static/images/Disaster_Reseach.png);
 

### Further improvement
 - use slugs (book's keywords) instead of the object's id to improve the site's ranking in search engines.

## Acknowledgments

 - Capture origin [Flickr Account of Christine Warner-Morin](https://www.flickr.com/photos/christinehawks/50353850332/in/photolist-2jHADpj-7kmiGy-2jHEru9-2jFJ9Y7-22P5zJg-of6wu8-NaF2Rd-ojVc2X-2hy4jKb-ayQ9Zd-2a3Fsxe-oY5g6v-4Qan5V-9E5p81-2jeowAb-8cnfe4-8cqAej-4wfLyv-8Y56Fj-2jFBPqN-cWFQTo-pNWvyC-9EkDQJ-vRtXnm-2k5qz8h-2mg9aBL-24PzNWS-jLRWD-7Deny4-8s5SFR-6KqwLt-2mtZSi1-DaQDT9-2kbz98Q-2iF8i2J-2jEWWFC-83hwXC-2nx2aAF-EZDYqS-6KuEas-2np5gAz-28Q8YfN-27aL8kh-cpQk6E-oR5RdZ-xxdRFb-6RTSvw-2jwwdXD-8kCBE2-wPXpbo "Flickr Account of Christine Warner-Morin")
 - "Orange Fire logo" origin [Freepik.com](https://www.freepik.com/free-vector/orange-fire-logo_35202562.htm#query=fire%20burn%20logo&position=29&from_view=keyword&track=ais_user&uuid=fb1e3f8f-07cb-4333-b537-b6ca4ad264fd  "Freepik.com")

- super helpful members of the Student Support Team. Roman, Rebecca, Sarah, Thomas, Oisin and Alan, **thank you**!

- 

