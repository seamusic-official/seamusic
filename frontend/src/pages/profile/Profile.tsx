import MainLayout from '../../components/layouts/MainLayout'
import dess from '../../assets/everydesigner.png'
import { Song } from '../../components/songs/Song'
import { useAppSelector } from '../../hooks/redux'
import KitLink from '../../components/kits/KitLink';
import AddButtonPlus from '../../components/icons/AddButtonPlus';
import DefaultButton from '../../components/buttons/DefaultButton';
import { useEffect, useState } from 'react';
import BeatService from '../../services/BeatService';
import { SongLoading } from '../../components/loading-elements/SongLoading';
import LicenseLink from '../../components/licenses/LicenseLink';


export default function Profile() {
  const user = useAppSelector((state) => state.auth.user);
  const [beats, setBeats] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const get_all_beats = async () => {
      try {
          const response = await BeatService.my();
          const responseData = response.data
          setBeats(responseData)
          setLoading(false)
          console.log("THIS IS RESPONSE", response);
        } catch(error){
          setLoading(false)
          console.error()
        }
      };

    get_all_beats()
  }, []);

  return (
    <MainLayout>
           <div className="">
            <div className="mt-2 flex items-center flex-wrap">
            <div className="relative">              
                <img
                id="playlist-thumbnail"
                src={user.picture_url}
                alt="alan walker artist"
                className="w-56 h-56 mr-6 rounded-full border border-neutral-600"
                />
                <span className="absolute top-[190px] ml-[175px] w-6 border-2 border-neutral-600 h-6 bg-emerald-500 border-white dark:border-gray-800 rounded-full"></span>
            </div>

              <div className="mt-16">
                <h2
                  className="text-gray-50 uppercase text-xs font-semibold tracking-tighter mt-1"
                >
                  {user.role}
                </h2>
                <h1 className='text-white text-6xl tracking-tighter font-extrabold truncate'>{user.username}</h1>
                <div className="mr-1 mb-4 mt-4">
                    <a className="p-2 m-1 font-semibold rounded-xl from-zinc-200 backdrop-blur-2xl border-neutral-900 bg-zinc-800/30 from-inherit" href="">
                    Opium
                    </a>
                    <a className="p-2 m-1 font-semibold rounded-xl from-zinc-200 backdrop-blur-2xl border-neutral-900 bg-zinc-800/30 from-inherit" href="">
                    Newjazz
                    </a>
                    <a className="p-2 m-1 font-semibold rounded-xl from-zinc-200 backdrop-blur-2xl border-neutral-900 bg-zinc-800/30 from-inherit" href="">
                    Trap
                    </a>
                </div>
                <p
                  id="playlist-description"
                  className="text-white mt-6 text-sm font-normal leading-none opacity-70"
                >
                 Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing layouts and visual mockups.
                </p>

                <div className="flex items-center mt-2">
                <a
                    className="flex text-white font-bold text-sm hover:text-underline cursor-pointer"
                    >
                    <img className="mr-1 w-5 invert" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAfElEQVR4nO2TSwqAIBRFz8hFRRuIFpZtMz/QKmxiQdDHpzYIPPDAwb3e51OhUcgIWCAklAEGaYBJ3HyvRRoQMqoF8MmIuhddXxqQQgv4yYgUMAMeWF9MEu2BFrxtnfMPvMDkcwLchcFW0D4ee6qgPV2cjt25uFYVtA1u2QBivZ8j3cMZWwAAAABJRU5ErkJggg==" />
                    Listen a voice tag</a>
                  
                  <div
                    className="font-extrabold text-md text-white opacity-70 mx-1 mb-1 pb-1"
                  >
                    .
                  </div>
                  <p className="text-white opacity-70 font-normal text-sm">
                    1,308,405 likes
                  </p>
                  <div
                    className="font-extrabold text-md text-white opacity-70 mx-1 mb-1 pb-1"
                  >
                    .
                  </div>
                  <p className="text-white opacity-70 font-normal text-sm mr-1">
                    50 songs,
                  </p>
                  <p className="text-white opacity-70 font-normal text-sm">
                    2hr 36 min
                  </p>
                </div>
              </div>
            </div>
          </div>
          <div className="w-full " >
            <div
              className="w-full p-4"
            >
              <div
                className=" flex items-center text-white mx-2 my-2 md:flex"
              >
                <svg
                  className="bg-emerald-600 rounded-full w-12 h-12 p-3 text-white"
                  role="img"
                  height="24"
                  width="24"
                  viewBox="0 0 24 24"
                  aria-hidden="true"
                >
                  <polygon
                    points="21.57 12 5.98 3 5.98 21 21.57 12"
                    fill="currentColor"
                  ></polygon>
                </svg>


                <div className="text-emerald-500">
                  <svg
                    className="mx-2 my-2 fill-current"
                    role="img"
                    height="38"
                    width="38"
                    viewBox="0 0 32 32"
                  >
                    <path
                      d="M27.319 5.927a7.445 7.445 0 00-10.02-.462s-.545.469-1.299.469c-.775 0-1.299-.469-1.299-.469a7.445 7.445 0 00-10.02 10.993l9.266 10.848a2.7 2.7 0 004.106 0l9.266-10.848a7.447 7.447 0 000-10.531z"
                    ></path>
                  </svg>
                </div>
            
                <div className="m-2">
                  <DefaultButton href={`/profile/update`} title="Edit profile" />
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
            <div>
              <h1 className="flex items-center text-white font-extrabold text-2xl mt-6">
                    Licenses <AddButtonPlus link="/dashboard"/>
                </h1>
                <div className="flex overflow-auto justify-start items-center mb-4">
                    <div>
                      <LicenseLink 
                          link="/license" 
                          image={dess} 
                          title="EXCLUSIVE RIGHTS" 
                          description="U're get a exclusive beat with track out" 
                          price="from 100$ / contactual" />
                    </div>
                </div>              
            </div>

            <div>
                <h1 className="flex items-center text-white font-extrabold text-2xl mt-6">
                    {user.username}'s kits <AddButtonPlus link="/dashboard"/>
                </h1>
                <div className="flex overflow-auto justify-start items-center mb-4">
                    <div>
                      <KitLink link="/kit/newera" image={dess} title="✕  RIOT UNIVERSE COMMUNITY STASH KIT 2024  ✕ "/>
                    </div>
                </div>
            </div>
            <h1 className="flex items-center text-white font-extrabold text-2xl mt-6">
                {user.username}'s tracks <AddButtonPlus link="/dashboard" />
            </h1>
              <div
                className="my-1 mx-2 h-72 overflow-y-auto md:h-full md:overflow-hidden"
              >
                <table className="w-full cursor-default">
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
                  {!loading ? 
                    (
                      beats.map((beat) => (
                        <Song
                          id={beat.id}
                          name={beat.title} 
                          picture={beat.picture_url} 
                          author={beat.prod_by} 
                          src={beat.file_url} 
                          album="any" 
                          date={beat.created_at}
                          type={beat.type}
                          isAction={false}
                        />
                      ))
                    ) 
                    : (
                      <>
                        <SongLoading />
                        <SongLoading />
                        <SongLoading />
                        <SongLoading />
                        <SongLoading />
                      </>
                    )
                  }
                  </tbody>
                </table>
              </div>

              <h1 className="flex items-center text-white font-extrabold text-2xl mt-6">
                  It is also found in..
                </h1>
                <div className="flex overflow-auto justify-start items-center mb-4">
                    <div>
                      <LicenseLink 
                          link="/license" 
                          image={dess} 
                          title="EXCLUSIVE RIGHTS" 
                          description="U're get a exclusive beat with track out" 
                          price="from 100$ / contactual" />
                    </div>
                </div>   
            </div>
          </div>
    </MainLayout>
  )
}
