#**Project Documentation**

##**Heroku Webapp URL:** <https://obscure-stream-46373.herokuapp.com/>

##Resources used in this repository

1. **Frameworks:** Flask
2. **Web Deployment:** Heroku
3. **APIs:** Spotify, Genius
4. **Libraries:** requests, dotenv, json, os, random, SQLAlchemy and Flask-Login

Here, **requests** is used for the `GET` and `POST` functions in order to authorize and interact with each APIs, **dotenv** and **os** are used to access variables defined and initialized in the environment and the rest are used to access and display information within code 

**SQLAlchemy** is a python library used to communicate with the **PostGres** Database, which involves functions such as creating tables, querying adding and deleting records from specific tables.

**Flask-Login** is a python library within flask which serves the basic purpose of handling *login requests* for each application. 

##**How to setup and run repository files**

For someone looking to fork this repository here are the additional resources required: 

1. First, update your package index using `sudo apt update`. Then install **PostGresQL** using `sudo apt install postgresql`

2. Next install **psycopg2** using the statement `pip install psycopg2-binary`. This is to allow the user to interact with local DBs if needed

3. Next, install **SQLAlchemy** using `pip install Flask-SQLAlchemy==2.1`

4. Install **Flask-Login** using `pip install flask-login` 

5. Clone repository to local machine through the command line using `git clone`

6. To install the heroku addons that allow us to create the **PostGres** database, enter `heroku addons:create heroku-postgresql:hobby-dev -a 'Your app name'` on the command line

7. Use the command `heroku pg:psql` to communicate with the database and the tables created

8.See the config vars set by Heroku using `heroku config`. Copy paste the value for **DATABASE_URL** as an *environment variable* by entering this in the terminal: `export DATABASE_URL='copy-paste-value-in-here'`

9. Use `\d` to view your list of relations and `\q` to exit the database view. You can also use **SQL** querying syntax to view the contents of each table


##**Technical Issues Encountered**

1. One technical issue encountered was during the validation of the **Artist ID**. In the design, there was a decision to make whether to include a second method whose sole purpose is to validate the input entered by the user using the **Artist API** or to include it in the `fetch_data()` method. In the end, the former was preferred since it allowed to validate user input at different stages of the app without having to call the main method

2. Another technical issue encountered was during the coding of **error** messages. Instead of using `flask.flash`, it was easier in design to pass in a *boolean check* in `flask.render_template()`, where, if the *boolean check* was **False**, then an error message was displayed in the corresponding **HTML** page using `if` conditions 

3. Instead of displaying the **Artist ID** form on the `/homepage`, there was another page at the `/welcome` endpoint created that solely facilitated the submission of **Artist ID** from the user. This was done to avoid page congestion

4. Another technical issue resolved was during creation of **User** table for the purpose of *User Login*. When creating the **User** class, `UserMixin` was passed as a parameter. This avoids the creation of methods such as `is_authenticated()`, `is_active()`, `is_anonymous()` and `get_id()`. In addition, the *primary key* has to be named as `id`.

##**Suggested Improvements**

1. The first suggested improvement that can be made is to improve the functionalities of user input. This app can be improved by taking *Artist Name* as input from the user instead of *Artist ID* due to convenience and ease of use. 


2. Another suggested improvement is to include the feature of a **password** along with the username during user validation. This adds an extra layer of protection for the app and also means that users with the same username will not share the same *data* and *information*.


3. A third improvement that can be made for user convenience is the ability to *delete records* from the database. Users should have the option to remove any **Artist IDs** that he/she may have entered incorrectly

##**Experience and Expectations**

In working with this milestone, it was *exponentially* more challenging than the first milestone. In this, I had encountered more *errors* due to *RunTimeError*, *KeyError*, *BaseQuery* errors and much more. It was also exceptionally more difficult to debug them due to the nature of the outputs. However, this was a very informative milestone which presented a **steep learning curve** in that, I learnt much more functionalities that I can add to future applications which could have only been learnt through experience from designing an app, which is what was done in this milestone.