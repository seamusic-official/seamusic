import { AxiosResponse } from "axios";
import $api from "../http";

export default class SpotifyService {
    static async get_all(): Promise<AxiosResponse> {
        return $api.get("music/spotify/")
    }

    static async get_albums(): Promise<AxiosResponse> {
        return $api.get("music/spotify/albums")
    }
    
    static async get_tracks_from_album(album_id): Promise<AxiosResponse> {
        return $api.get("music/spotify/tracks_from_album", {
            params: {
                album_id: album_id
            }
        })
    } 
    static async get_info_about_something(query): Promise<AxiosResponse> {
        return $api.get(`music/wikipedia/summary/${query}`)
    }
    
    static async get_album(album_id): Promise<AxiosResponse> {
        return $api.get("music/spotify/album", {
            params: {
                album_id: album_id
            }
        })
    }
    
    static async track(id): Promise<AxiosResponse> {
        return $api.get("music/spotify/track", {
            params: {
                id: id
            }
        })
    }

    static async get_artist(artist_id): Promise<AxiosResponse> {
        return $api.get("music/spotify/astist", {
            params: {
                artist_id: artist_id
            }
        })
    }

    static async search(query: string): Promise<AxiosResponse> {
        return $api.get("music/spotify/search", {
            params: {
                query: query
            }
        })
    } 

}