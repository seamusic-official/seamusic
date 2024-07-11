import { Link, useParams } from "react-router-dom"
import MainLayout from "../../components/layouts/MainLayout"
import SpotifyService from "../../services/SpotifyService";
import { useEffect, useState } from "react";
import { Song } from "../../components/songs/Song";
import { msToMin } from "../../utils/msToMin";
import { SongLoading } from "../../components/loading-elements/SongLoading";
import BeatpackService from "../../services/BeatpackServise";
import Input from "../../components/inputs/Input";
import { useAppSelector } from "../../hooks/redux";
import SubmitButton from "../../components/buttons/SubmitButton";

export default function AddBeatpack() {
  const user = useAppSelector((state) => state.auth.user);

  const [data, setData] = useState([]);
  const [tracks, setTracks] = useState([]);
  const { id } = useParams()
  const [loading, setLoading] = useState(true);
  const [info, setInfo] = useState("");
  const [file, setFile] = useState(null); 
  const [picture, setPicture] = useState(null);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [co_prod, setCo_prod] = useState('');
  const [prod_by, setProd_by] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await BeatpackService.get_one(id);
        const responseData = response.data;
        setData(responseData);
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, []);

  // useEffect(() => {
  //   const fetchData = async () => {
  //     try {
  //       const response = await BeatpackService.get_one(id);
  //       const responseData = response.data;
  //       setTracks(responseData);
  //       console.log(responseData)
  //       setLoading(false);
  //     } catch (error) {
  //       console.error(error);
  //     }
  //   };

  //   fetchData();
  // }, []);


  return (
    <MainLayout>
          <div className="">
            <div className=" mt-8 flex items-center md:flex">
              {!loading ? (
              <img
                id="playlist-thumbnail"
                src=""
                alt="alan walker artist"
                className="w-56 h-56 min-w-56 ml-4 mr-6 rounded-lg"
              />                
              ) : (
                <div
                className="w-56 h-56 min-w-56 mr-6 rounded-lg animate-pulse bg-gray-300 bg-opacity-10"></div>
              )}

              <div className="mt-8 w-full ">
                <h2
                  className="text-gray-50 uppercase text-md font-semibold tracking-tighter mr-2 mt-1"
                >
                  Beatpack by {user.username}
                </h2>
                <p
                  className="text-white mt-1 text-sm font-normal leading-none opacity-70"
                >
                  Beatpack - pack of your beats, you can to invite other beatmakers on your beatpack
                </p>
                <span
                  className="text-white text-6xl capitalize font-extrabold tracking-tighter"
                  >
                  <div className="m-1">
                    <label htmlFor="id" className="inline-block  font-extrabold text-sm tracking-wider ">
                    <span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>*</span>
                      Title
                    </label>
                      <Input
                          value={user.username}
                          id="title"
                          type="text"
                          placeholder="title 153bpm F#"
                          onChange={(e) => setTitle(e.target.value)}
                          buttonText=""
                      />
                  </div>
                  </span>
                <p
                  id="playlist-description"
                  className="text-white mt-2 text-sm font-normal leading-none "
                >
                  <div className="m-1">
                    <label htmlFor="id" className="inline-block  font-extrabold text-sm my-1 tracking-wider ">
                    <span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>*</span>
                      Picture
                    </label>
                      <Input
                          value={user.username}
                          id="title"
                          type="text"
                          placeholder="title 153bpm F#"
                          onChange={(e) => setTitle(e.target.value)}
                          buttonText=""
                      />
                  </div>
                </p>
                <div className="flex items-center mt-2">
                  <a
                    className="text-white font-semibold text-md hover:text-underline cursor-pointer"
                    >SeaMusic</a>
                  
                  <div
                    className="font-extrabold text-md text-white opacity-70 mx-1 mb-1 pb-1"
                  >
                    .
                  </div>
                  <p className="text-white opacity-70 font-normal text-sm">
                    0 likes
                  </p>
                  <div
                    className="font-extrabold text-md text-white opacity-70 mx-1 mb-1 pb-1"
                  >
                    .
                  </div>
                  <p className="text-white opacity-70 font-normal text-sm mr-1">
                    0 songs,
                  </p>
                  <p className="text-white opacity-70 font-normal text-sm">
                    0 min
                  </p>
                </div>
                
              </div>
              
            </div>
          </div>
          <div className="m-1">
                    <label htmlFor="id" className="inline-block  font-extrabold text-sm my-1 tracking-wider ">
                    <span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>*</span>
                      Description
                    </label>
                      <Input
                          value={user.username}
                          id="title"
                          type="text"
                          placeholder="title 153bpm F#"
                          onChange={(e) => setTitle(e.target.value)}
                          buttonText=""
                      />
                  </div>
          <div className="w-full " >
            <div
              className="w-full p-4"
            >
              <div className="flex justify-center items-center m-4 md:hidden">
                <button
                  className="bg-emerald-600 text-white uppercase text-xs rounded-full font-semibold tracking-widest px-8 py-3"
                >
                  Listen it
                </button>
              </div>
              <div
                className="hidden flex items-center text-white w-1/2 my-2 md:flex"
              >
                <svg
                  className="bg-emerald-600 rounded-full w-12 h-12 p-3 text-white"
                  height="28"
                  role="img"
                  width="28"
                  viewBox="0 0 24 24"
                  aria-hidden="true"
                >
                  <polygon
                    points="21.57 12 5.98 3 5.98 21 21.57 12"
                    fill="currentColor"
                  ></polygon>
                </svg>
                <div className="text-emerald-600">
                  <svg
                    className="mx-4 my-2 fill-current"
                    role="img"
                    height="32"
                    width="32"
                    viewBox="0 0 32 32"
                  >
                    <path
                      d="M27.319 5.927a7.445 7.445 0 00-10.02-.462s-.545.469-1.299.469c-.775 0-1.299-.469-1.299-.469a7.445 7.445 0 00-10.02 10.993l9.266 10.848a2.7 2.7 0 004.106 0l9.266-10.848a7.447 7.447 0 000-10.531z"
                    ></path>
                  </svg>
                </div>
                <div className="text-gray-300">
                  <svg
                    className="fill-current"
                    role="img"
                    height="32"
                    width="32"
                    viewBox="0 0 32 32"
                  >
                    <path
                      d="M5.998 13.999A2 2 0 105.999 18 2 2 0 005.998 14zm10.001 0A2 2 0 1016 18 2 2 0 0016 14zm10.001 0A2 2 0 1026.001 18 2 2 0 0026 14z"
                    ></path>
                  </svg>
                </div>
              </div>

              <div
                className="my-10 h-72 md:h-full md:overflow-hidden"
              >
                <table className="w-full">
                  <thead>
                    <tr
                      className="flex justify-around items-center text-gray-400 border-b border-gray-400 border-opacity-30 uppercase h-8"
                    >
                      <th className="text-md">
                        #<span className="text-xs ml-2">Picture</span>
                      </th>
                      <th className="text-md">
                        #<span className="text-xs ml-2">Title</span>
                      </th>
                      <th className="text-xs">Album</th>
                      <th className="text-xs">Date Added</th>
                      <th className="">
                        <svg
                          width="16"
                          height="16"
                          viewBox="0 0 16 16"
                          fill="none"
                        >
                          <path
                            d="M7.999 3H6.999V7V8H7.999H9.999V7H7.999V3ZM7.5 0C3.358 0 0 3.358 0 7.5C0 11.642 3.358 15 7.5 15C11.642 15 15 11.642 15 7.5C15 3.358 11.642 0 7.5 0ZM7.5 14C3.916 14 1 11.084 1 7.5C1 3.916 3.916 1 7.5 1C11.084 1 14 3.916 14 7.5C14 11.084 11.084 14 7.5 14Z"
                            fill="currentColor"
                          ></path>
                        </svg>
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                  {!loading ? (
                      data.beats.map((song) => (
                          <Song
                            id={song.id}
                            name={song.name}
                            date={data.release_date}
                            duration={
                              msToMin(song.duration_ms)
                            }
                            src={song.preview_url}
                            author={song.artist}
                            type={song.type}
                            picture={data.image_url}
                            album={data.name}
                            spotify_url={song.spotify_url}
                          />
                      ))
                    ) : (
                      <div>
                        <SongLoading />
                        <SongLoading />
                        <SongLoading />
                        <SongLoading />
                      </div>
                    )} 
                  </tbody>
                </table>
              </div>
                <p
                  className="text-white mb-2 text-sm font-normal leading-none opacity-70"
                >
                  When you pressed button "Publish", do you accept terms & conditions of SeaMusic
  
                </p>
              <SubmitButton title="Publish" />
            </div>
          </div>
    </MainLayout>
  )
}