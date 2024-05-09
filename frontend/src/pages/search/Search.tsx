import React, { ChangeEvent, ChangeEventHandler, useEffect, useState } from 'react'
import MainLayout from '../../components/layouts/MainLayout'
import Input from '../../components/Input'
import ArtistLink from '../../components/ArtistLink'
import SpotifyService from '../../services/SpotifyService';
import { Song } from '../../components/Song';
import SongLink from '../../components/SongLink';
import PictureLink from '../../components/PictureLink';
import { msToMin } from '../../utils/msToMin';
import ArtistLinkLoading from '../../components/loadingElements/ArtistLinkLoading';
import PictureLinkLoading from '../../components/loadingElements/PictureLinkLoading';
import { SongLoading } from '../../components/loadingElements/SongLoading';

export default function Search() {
    const [data, setData] = useState(null);
    const [query, setQuery] = useState('');
    const [loading, setLoading] = useState(true);
    const [status, setStatus] = useState(false);

    const handleInputChange: ChangeEventHandler<HTMLInputElement> = (event) => {
      setQuery(event.target.value);
    };

    const handleInputSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
      e.preventDefault();
      setStatus(true)
      setLoading(true)
      try {
        if (query === '') return;
        const response = await SpotifyService.search(query);
        const responseData = response.data;
        setData(responseData);
        setLoading(false);
        console.log(responseData);
      } catch (error) {
        console.error(error);
      }
    }

  return (
    <MainLayout>
      <form onSubmit={(e) => handleInputSubmit(e)}>
        <Input 
            type="text"
            buttonText="Search" 
            placeholder="xxxmanera.." 
            value={query}
            onChange={(e) => (handleInputChange(e))}
        />
        </form>
        <div>

      {status ? (
        !loading ? (
          <div>
              <h2 className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter" id="playlist-title">
                Artists:
              </h2>
            <div className="flex overflow-auto justify-start items-center">
              {data.map((item) => (
                item.type === "artist" && (
                  <div key={item.id}>
                    <ArtistLink key={item.id} link="/profile/1" image={item.image_url} title={item.name} />
                  </div>
                )
              ))}
            </div>
            <h2 className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter" id="playlist-title">
                Albums:
              </h2>
            <div className="flex overflow-auto justify-start items-center">
              {data.map((item) => (
                item.type === "album" && (
                  <div className="m-1" key={item.id}>
                    <PictureLink link={`/albums/${item.id}`} artist={item.artist} image={item.image_url} title={item.name} />
                  </div>
                )
              ))}
            </div>
            <h2 className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter" id="playlist-title">
                Tracks:
              </h2>
            <div>
              {data.map((item) => (
                item.type === "track" && (
                  <div key={item.id}>
                          <Song
                            id={item.id}
                            name={item.name}
                            date={item.release_date}
                            duration={
                              msToMin(item.duration_ms)
                            }
                            author={item.artist}
                            picture={item.image_url}
                            album={item.name}
                          />
                  </div>
                )
              ))}
            </div>
          </div>

        ) : (
          <div>
              <h2 className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter" id="playlist-title">
                Artists:
              </h2>
            <div className="flex overflow-auto justify-start items-center">
              <ArtistLinkLoading />
              <ArtistLinkLoading />
              <ArtistLinkLoading />
              <ArtistLinkLoading />
              <ArtistLinkLoading />
            </div>
            <h2 className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter" id="playlist-title">
                Albums:
              </h2>
            <div className="flex overflow-auto justify-start items-center">
              <PictureLinkLoading />
              <PictureLinkLoading />
              <PictureLinkLoading />
              <PictureLinkLoading />
            </div>
            <h2 className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter" id="playlist-title">
                Tracks:
              </h2>
            <div>
              <SongLoading />
              <SongLoading />
              <SongLoading />
              <SongLoading />
            </div>
          </div>
        )

        ) : (
          <h2 className="mt-4 mb-2 text-white text-3xl capitalize font-extrabold tracking-tighter" id="playlist-title">
            Search on Seamusic
          </h2>
        )
      }
        </div>
    </MainLayout>
  )
}
