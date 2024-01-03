// import React, { useEffect } from "react";
// import SpotifyWebApi from "spotify-web-api-js";

// function useSpotify() {
//   useEffect(() => {
//     const spotify = new SpotifyWebApi();
//     const response = spotify.getTracks()
//       .then((tracks: ITrackResponse) => console.log(tracks))
//       .catch((error: string) => console.error(error));
    
//     return response.json;
//   }, []);

// }

// export default useSpotify;