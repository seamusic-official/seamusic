import React from 'react'
import MainLayout from '../../components/layouts/MainLayout'
import { Link } from 'react-router-dom'
import dess from '../../assets/everydesigner.png'
import { Song } from '../../components/Song'
import PictureLink from '../../components/PictureLink'
import KitLink from '../../components/KitLink'

export default function Producer() {
  return (
    <MainLayout>
           <div className="">


            <div className="flex  flex-col justify-center items-center md:hidden">
              <img
                src={dess}
                alt="alan walker artist image "
                className="w-40 h-40 rounded-full "
              />
              <h1 className="text-white capitalize font-semibold text-2xl mt-2">
                This is Alan Walker
              </h1>
              <p className="text-xs uppercase text-gray-100 mt-1">1,308,405 likes</p>
            </div>
            <div className="hidden mt-8 flex items-center md:flex">
            <div className="relative">              
                <img
                id="playlist-thumbnail"
                src="https://ugc.production.linktr.ee/e463406b-3ceb-4c69-9576-b9693c699bd1_photo-2024-01-06-19-09-46.jpeg?io=true&size=avatar-v3_0"
                alt="alan walker artist"
                className="w-56 h-56 mr-6 rounded-full border border-neutral-600"
                />
                <span className="absolute top-[190px] ml-[175px] w-6 border-2 border-neutral-600 h-6 bg-emerald-500 border-white dark:border-gray-800 rounded-full"></span>
            </div>

              <div className="mt-16">
                <h2
                  className="text-gray-50 uppercase text-xs font-bold tracking-tighter mt-1"
                >
                  Producer & Musician
                </h2>
                <span
                  className="text-white text-6xl tracking-tighter font-extrabold"
                  ><h1 id="playlist-title">whyspacy?</h1></span>
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
                damn, why spacy? WW/ Шайни, heronwater, T-fest, GONE.FLUDD, uglystephan, xxxmanera etc. 
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

              <div className="flex justify-center items-center m-4 md:hidden">
              <div className="mt-2 mb-2 ">
                    <a className="p-2 border-emerald-600 border-2 hover:border-emerald-800  font-bold rounded-xl from-zinc-200 backdrop-blur-2xl border-neutral-900 bg-zinc-800/30 from-inherit" href="">
                    Messages
                    </a>
                </div>
                <button
                  className="bg-green-500 text-white uppercase text-xs rounded-full font-semibold tracking-widest px-8 py-3"
                >
                  Shuffle Play
                </button>
              </div>
              <div
                className="hidden flex items-center text-white w-1/2 mx-4 my-2 md:flex"
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
                    <a className="p-2 border-emerald-600 border hover:border-emerald-800  font-bold rounded-xl from-zinc-200 backdrop-blur-2xl border-neutral-900 bg-zinc-800/30 from-inherit" href="">
                    Dirrect message
                    </a>
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
            <div >
            <h1 className="text-white font-extrabold text-2xl mt-6">
                whyspacy?'s kits: 
            </h1>
                <div className="flex overflow-auto justify-start items-center mb-4">
                    <div>
                      <KitLink link={`al`} image={dess} title="✕  RIOT UNIVERSE COMMUNITY STASH KIT 2024  ✕ "/>
                    </div>
                    <div>
                      <KitLink link={`al`} image={dess} title="21' happy birthday stash kit "/>
                    </div>
                    <div>
                      <KitLink link={`al`} image={dess} title="✕  RIOT UNIVERSE COMMUNITY STASH KIT 2024  ✕ "/>
                    </div>
                    <div>
                      <KitLink link={`al`} image={dess} title="✕  RIOT UNIVERSE COMMUNITY STASH KIT 2024  ✕ "/>
                    </div>
                    <div>
                      <KitLink link={`al`} image={dess} title="✕  RIOT UNIVERSE COMMUNITY STASH KIT 2024  ✕ "/>
                    </div>
                </div>
            </div>
              <div
                className="my-10 mx-2 h-72 overflow-y-auto md:h-full md:overflow-hidden"
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
                <Song name="Каждый из дизайнеров" picture={dess} author="xxxmanera" album="Каждый из дизайнеров" date="02.01.2023"/>
                <Song name="Каждый из дизайнеров" picture={dess} author="xxxmanera" album="Каждый из дизайнеров" date="02.01.2023"/>
                <Song name="Каждый из дизайнеров" picture={dess} author="xxxmanera" album="Каждый из дизайнеров" date="02.01.2023"/>
                  </tbody>
                </table>
              </div>
              
              <div className="flex justify-between items-center my-6 md:hidden">
                <button className="text-green-500">
                  <svg
                    className="fill-current mr-4"
                    role="img"
                    height="24"
                    width="24"
                    viewBox="0 0 16 16"
                  >
                    <path fill="none" d="M0 0h16v16H0z"></path>
                    <path
                      d="M13.797 2.727a4.057 4.057 0 00-5.488-.253.558.558 0 01-.31.112.531.531 0 01-.311-.112 4.054 4.054 0 00-5.487.253c-.77.77-1.194 1.794-1.194 2.883s.424 2.113 1.168 2.855l4.462 5.223a1.791 1.791 0 002.726 0l4.435-5.195a4.052 4.052 0 001.195-2.883 4.057 4.057 0 00-1.196-2.883z"
                    ></path>
                  </svg>
                </button>
                <p className="text-white font-semibold text-sm tracking-wider">
                  Heading Home,
                  <span className="text-gray-300 font-semibold text-sm"
                    >Alan Walker</span>
                  
                </p>
                <button>
                  <svg
                    className="text-white"
                    height="24"
                    role="img"
                    width="24"
                    viewBox="0 0 24 24"
                    aria-hidden="true"
                  >
                    <polygon
                      points="21.57 12 5.98 3 5.98 21 21.57 12"
                      fill="currentColor"
                    ></polygon>
                  </svg>
                </button>
              </div>

              <div
                className="flex justify-around mt-2 text-gray-200 text-xs hover:text-white md:hidden"
              >
                <button className="flex flex-col items-center">
                  <svg
                    className=""
                    viewBox="0 0 512 512"
                    width="20"
                    height="20"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M 256.274 60.84 L 84.324 166.237 L 84.324 443.063 L 193.27 443.063 L 193.27 293.73 L 320.228 293.73 L 320.228 443.063 L 428.222 443.063 L 428.222 165.476 L 256.274 60.84 Z M 256.274 35.95 L 448.452 149.145 L 448.452 464.395 L 300 464.395 L 300 315.062 L 213.499 315.062 L 213.499 464.395 L 64.095 464.395 L 64.095 150.161 L 256.274 35.95 Z"
                      fill="currentColor"
                    ></path>
                  </svg>
                  Home
                </button>
                <button className="flex flex-col items-center">
                  <svg
                    className=""
                    viewBox="0 0 512 512"
                    width="20"
                    height="20"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M349.714 347.937l93.714 109.969-16.254 13.969-93.969-109.969q-48.508 36.825-109.207 36.825-36.826 0-70.476-14.349t-57.905-38.603-38.603-57.905-14.349-70.476 14.349-70.476 38.603-57.905 57.905-38.603 70.476-14.349 70.476 14.349 57.905 38.603 38.603 57.905 14.349 70.476q0 37.841-14.73 71.619t-40.889 58.921zM224 377.397q43.428 0 80.254-21.461t58.286-58.286 21.461-80.254-21.461-80.254-58.286-58.285-80.254-21.46-80.254 21.46-58.285 58.285-21.46 80.254 21.46 80.254 58.285 58.286 80.254 21.461z"
                      fill="currentColor"
                      fill-rule="evenodd"
                    ></path>
                  </svg>
                  Search
                </button>
                <button className="flex flex-col items-center">
                  <svg
                    className=""
                    viewBox="0 0 512 512"
                    width="20"
                    height="20"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M291.301 81.778l166.349 373.587-19.301 8.635-166.349-373.587zM64 463.746v-384h21.334v384h-21.334zM192 463.746v-384h21.334v384h-21.334z"
                      fill="currentColor"
                    ></path>
                  </svg>
                  Library
                </button>
                <button className="flex flex-col items-center">
                  <svg
                    className="fill-current"
                    role="img"
                    height="20"
                    width="20"
                    viewBox="0 0 24 24"
                  >
                    <path
                      d="M11.5 0C5.149 0 0 5.148 0 11.5 0 17.851 5.149 23 11.5 23S23 17.851 23 11.5C23 5.148 17.851 0 11.5 0zm0 22C5.71 22 1 17.29 1 11.5S5.71 1 11.5 1 22 5.71 22 11.5 17.29 22 11.5 22zm.499-6.842V5h-1v10.149l-3.418-3.975-.758.652 4.678 5.44 4.694-5.439-.757-.653-3.439 3.984z"
                    ></path>
                  </svg>
                  Get App
                </button>
              </div>
            </div>
          </div>
    </MainLayout>
  )
}
