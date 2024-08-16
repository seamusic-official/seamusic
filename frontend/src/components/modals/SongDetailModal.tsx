import Menu from "Menu"
import { useAppSelector, useAppDispatch } from "../../hooks/redux"
import { play, pause, updateTime, updateDuration } from '../../store/reducers/playerSlice'
import { useEffect, useState } from "react";
import SpotifyService from "../../services/SpotifyService";
import { Link } from "react-router-dom";
import SongLinkLoading from "../loading-elements/SongLinkLoading";
import default_picture from "../../assets/default-track-picture.png"


export default function ProgressBar({ isOpen, onClose }) {
  const dispatch = useAppDispatch();
  const { currentSong, timeElapsed, isActive, trackUrl } = useAppSelector((state) => state.player);
  const isPlaying = useAppSelector((state) => state.player.isPlaying);
  const link = currentSong.src
  const [src, setSrc] = useState(null)

  // useEffect(() => {
  //   const fetchData = async () => {
  //     try {
  //       const response = await SpotifyService.track(link);
  //       const responseData = response.data;
  //       setSrc(responseData);
  //       console.log(response)

  //     } catch (error) {
  //       console.error(error);
  //     }
  //   };

  //   fetchData();
  // }, []);

  const [audio] = useState(link ? new Audio() : new Audio());

  useEffect(() => {
    if (src) {
      audio.src = src;
      audio.controls = true;
      audio.autoplay = true;
    }
  }, [src]);
  
  const handlePlay = () => {
    dispatch(play());
    audio.play().catch(error => console.error('Error playing audio:', error));
  };
  

  const handlePause = () => {
    dispatch(pause())
    audio.pause();
  };
  return (     
    <div className={""}>
    {isOpen && (
      <div className="h-full">
        <div className="justify-between md:mb-0 ">
          <div className="mx-4 my-8 pt-2 lg:pt-0 flex justify-start w-full lg:w-1/3">
            <div>
              {currentSong.picture ? (
                <img
                  src={currentSong.picture}
                  alt=""
                  className="shadow-2xl m-1 rounded-md w-80 h-80"
                />                
              ) : (
                <img
                  src={default_picture}
                  alt=""
                  className="invert shadow-2xl m-1 rounded-md w-80 h-80"
                />
              )}

              <div className="flex flex-col justify-center m-1 lg:m-4">
                <h6 id="song-name" className="text-white font-semibold text-3xl text-left">
                  {currentSong.name}
                </h6>
                <p className="text-gray-400 font-semi-bold text-xl">
                  {currentSong.author}
                </p>
                <p className="mt-8 text-gray-400 w-96 font-semi-bold text-lg">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                </p>
              </div>
            </div>
            <div>
              <h2 className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter" id="playlist-title">
                Artists:
              </h2>
              <Link to="">
                <div className="p-2">
                  <img src={currentSong.picture} alt="" className="m-1 rounded-full w-32 h-32" />
                  <p className="w-32 text-gray-300 flex justify-center items-center font-bold text-lg leading-tight truncate ">{currentSong.author}</p>
                </div>
              </Link>
              <h2 className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter" id="playlist-title">
                Other them works:
              </h2>
              <div className="p-4">
                  <div className="flex justify-start items-center gap-4">
                    <SongLinkLoading />
                    <SongLinkLoading />
                    <SongLinkLoading />
                    <SongLinkLoading />
                    <SongLinkLoading />
                    <SongLinkLoading />
                  </div>
                </div>
            </div>
          </div>
        

        </div>
    </div>
    )}
  </div>
  

  )
}
