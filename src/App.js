import logo from './logo.svg';
import './App.css';
import { useState, useRef } from 'react';


function App() {
  // fetches JSON data passed in by flask.render_template and loaded
  // in public/index.html in the script with id "data"
  const args = JSON.parse(document.getElementById("data").text);
  console.log(args);

  // TODO: Implement your main page as a React component.
  const [ArtistIds, setArtistIds] = useState(args["artist_ids"]);
  const [SongName, setSongName] = useState(args["name_song"]);
  const [ArtistName, setArtistName] = useState(args["artist_name"]);
  const [Images, setImages] = useState(args["picture_song"]);
  const [Preview, setPreview] = useState(args["player"]);
  const [Lyrics, setLyrics] = useState(args["lyrics_url"]);
  const inputId = useRef(inputId);

  function onClickAdd() {
    let newList = [...ArtistIds, inputId.current.value];
    setArtistIds(newList);
    inputId.current.value = "";
  }
  function onClickDelete(index) {
    let newList = ArtistIds.splice(index, 1);
    setArtistIds(newList);
  }
  function onClickSave() {
    let artistJson = { "artistIds": ArtistIds };
    fetch("/save", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(artistJSON)
    })
      .then(response => response.json())
      .then(data => {
        setArtistIds(data.artist_ids)
        setSongName(data.name_song)
        setArtistName(data.artist_name)
        setImages(data.picture_song)
        setPreview(data.player)
        setLyrics(data.lyrics_url)
      })
  }

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
      <div>
        <input ref={inputId} type="text" placeholder="Artist ID" />
        <button onClick={onClickAdd}>Add Artist</button>
        <button onClick={onClickSave}>Save Artist IDs </button>
      </div>
    </div>
  );
}

export default App;
