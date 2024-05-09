export interface ISpotifyPlaylist {
    id: number,
    name: string,
    body: {
        items: []
    }
}

export interface IPlaylist {
    id: number,
    name: string,
}

export interface ISpotifySong {
    id: number,
    name: string,
    body: {
        items: []
    }
}

export interface ISong {
    id: number,
    description: string
    name: string,
    picture: string,
    author: number,
    date: string,
    album: number
    
    body: {
        items: []
    }
}

export interface IArtistResponse {
    id: string;
    name: string;
    genres: string[];
    followers: {
      total: number;
    };
    images: {
      url: string;
      height: number;
      width: number;
    }[];
  }

export interface ITrackResponse {
    id: string;
    name: string;
    album: {
      name: string;
      images: {
        url: string;
        height: number;
        width: number;
      }[];
    };
    artists: {
      id: string;
      name: string;
    }[];
    duration_ms: number;
    preview_url: string;
  }

export interface IPlaylistResponse {
    id: string;
    name: string;
    owner: {
      id: string;
      display_name: string;
    };
    tracks: {
      total: number;
      items: {
        track: {
          id: string;
          name: string;
        };
      }[];
    };
  }
  