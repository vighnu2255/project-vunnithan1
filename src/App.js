import logo from './logo.svg';
import './App.css';
import { useState, useRef } from 'react';


function App() {
  // fetches JSON data passed in by flask.render_template and loaded
  // in public/index.html in the script with id "data"
  const args = JSON.parse(document.getElementById("data").text);

  const [ArtistIds, setArtistIds] = useState(args[]);
  const [SongName, setSongName] = useState(args["name_song"]);
  const [ArtistName, setArtistName] = useState(args["artist_name"]);
  const [Images, setImages] = useState(args["picture_song"]);
  const [Preview, setPreview] = useState(args["player"]);
  const [Lyrics, setLyrics] = useState(args["lyrics_url"]);


  console.log(args);
  // TODO: Implement your main page as a React component.

  return (
    <div>
      <h1>{args.name_song}</h1>
      <h2>by: {args.artist_name}</h2>
      <br />
      <img src={args.picture_song} />
      <br />
      <audio controls="controls" id="audioPreview">
        <source src={args.player} type="audio/mp3" />
      </audio>
      <br />
      <a href={args.lyrics_url}>Lyrics</a>
      <br />

    </div>
  );
}

export default App;
