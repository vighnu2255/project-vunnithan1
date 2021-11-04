# Flask and `create-react-app`

# Heroku app link
https://polar-springs-86981.herokuapp.com/

## Requirements
1. `npm install`
2. `pip install -r requirements.txt`

## Run Application
1. Run command in terminal (in your project directory): `npm run build`. This will update anything related to your `App.js` file (so `public/index.html`, any CSS you're pulling in, etc).
2. Run command in terminal (in your project directory): `python3 app.py`
3. Preview web page in browser 'localhost:8080/' (or whichever port you're using)

## Deploy to Heroku
1. Create a Heroku app: `heroku create --buildpack heroku/python`
2. Add nodejs buildpack: `heroku buildpacks:add --index 1 heroku/nodejs`
3. Push to Heroku: `git push heroku main`

## Technical issues
1. One technical issue faced was that the map function in **App.js** was not working. It was because there was an undefined object, namely **artistId**. This issue is still unresolved as I was not able to find a solution to it.

2. Another technical issue faced was that the *css* file for the **register**, **login** and **welcome** pages were not rendering. This issue is still unresolved as I was not able to find a solution to it. There maybe an issue with file location or maybe cloning from another repository, due to which the *css* file is not being found, which is throwing a *404* Error on the console.

3. The final technical issue faced was that the **signup** page was not redirecting to the **welcome** page if user entered a user id that was already registered. This was solved by loading the user if it exists and then reditecting using the statement `load_user(username)` in the **signup** section.

Part of the stack I am most comfortable with was setting up of the **App.js** file, especially the React *components*, *states* and the *button clicks*. However, initializing the *mapping functions* and debugging the *fetch calls* were the sections that I was least comfortable with
