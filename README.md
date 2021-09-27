#**Project Documentation**

##**How to setup and run repository files**

1. First clone repository to local machine through the command line using `git clone`

2. Using `pip` command, download **Flask**, **requests** and **python-dotenv** packages through the command line

3. Create a **.env** file that houses your client credentials, which includes your Spotify **Client ID** and **Client Secret** and your Genius **Access Token**

4. Use `sudo snap install` to download the **Heroku** package and login using your Heroku credentials

##**Additional Features**

1. Firstly, one additional feature that can be added are extra information pertaining to the song such as release date, artist features and their pictures. This would make the webapp more appealing and presentable to the client.

2. The above option could be further expanded to include more functionalities for the webpage. This includes providing access to pre-existing resources such as links to the album the track belongs to, links to top tracks of featured artists accessible through the webpage

3. In comparison to static information and details being presented, dynamic ones can be implemented as well. This includes information such as the updated number of streams the track is currently receiving, which changes over time.

4. In the coding section, Spotify and Genius API authorization could be implemented much easier using community developed packages such as **spotipy** and **lyricsgenius**. This would make code reading simpler and easier to follow

##**Technical Issues Encountered**

Since this was my first time developing a web application, there were numerous technical issues faced during the coding aspect.

1. The first one was following the authorization flow of the Spotify API. I had found it very difficult to follow the authorization flow as there were two ways to authorize the user. I had followed the second alternative method, which directly generates and returns the access token by submitting the **Client_ID** and **Client_Secret**. Therefore, I had to consult help from a combination of _Spotify Web API Authorization Guide_ and _Youtube_ to piece together and understand how the Authorization flow works

<https://developer.spotify.com/documentation/general/guides/authorization-guide/> "Spotify Web API Authorization Guide"
<https://www.youtube.com/watch?v=yAXoOolPvjU&t=1023s> "Video on how Authorization flow works for Spotify API"

2. Another technical issue encountered was authorizing access to Genius API. Since the documentation provided very little help, outside help had to be consulted. For instance, the most frequent resource utilized was _Stack Overflow_. This helped me to understand how to put together the `GET` request for Genius API, the **parameters** and **headers** and the information that needs to be listed in them

<https://stackoverflow.com/questions/47400466/using-genius-api> "Queries regarding Genius API `GET` request"

3. A small technical issue encountered was with the remote repositories. Initially, this repository was created with a `README` file. This meant that when I tried to commit code to the remote repository, the contents of the repository whcih was not available locally had to be pulled using `git pull origin main`. However, an error called **fatal: refusing to merge unrelated histories** keeps occurring. This meant that the `git pull origin main` had to be modified to `git pull origin main --allow-unrelated-histories`

<https://stackoverflow.com/questions/37937984/git-refusing-to-merge-unrelated-histories-on-rebase> "More information on the error"

