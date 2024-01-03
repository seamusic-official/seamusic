import { Link } from "react-router-dom";
import des from "../assets/everydesigner.png"

const Sidebar = () => {
  return (
    <div
    className="border-r px-6 border-gray-300 bg-gradient-to-b hidden bg-black md:w-1/5 md:block px-6 py-4 h-full fixed left-0 from-zinc-200 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit  lg:bg-gray-200 lg:p-2 lg:dark:bg-zinc-800/30"
  >
    <div className="text-gray-300 my-2 cursor-pointer">
      <h1 className="font-bold text-xl">It's SeaMusic <br/> Picture $$$</h1>

    </div>
    <button className="text-gray-200 hover:text-white flex items-center mt-4">
      <svg
        className="mr-4"
        viewBox="0 0 512 512"
        width="24"
        height="24"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M 256.274 60.84 L 84.324 166.237 L 84.324 443.063 L 193.27 443.063 L 193.27 293.73 L 320.228 293.73 L 320.228 443.063 L 428.222 443.063 L 428.222 165.476 L 256.274 60.84 Z M 256.274 35.95 L 448.452 149.145 L 448.452 464.395 L 300 464.395 L 300 315.062 L 213.499 315.062 L 213.499 464.395 L 64.095 464.395 L 64.095 150.161 L 256.274 35.95 Z"
          fill="currentColor"
        ></path>
      </svg>
      <Link to="/">
        <a className="text-gray-300 text-sm font-bold hover:text-white capitalize">
          Home
        </a>
      </Link>
    </button>
    <button className="text-gray-200 hover:text-white flex items-center mt-4">
      <svg
        className="mr-4"
        viewBox="0 0 512 512"
        width="24"
        height="24"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M349.714 347.937l93.714 109.969-16.254 13.969-93.969-109.969q-48.508 36.825-109.207 36.825-36.826 0-70.476-14.349t-57.905-38.603-38.603-57.905-14.349-70.476 14.349-70.476 38.603-57.905 57.905-38.603 70.476-14.349 70.476 14.349 57.905 38.603 38.603 57.905 14.349 70.476q0 37.841-14.73 71.619t-40.889 58.921zM224 377.397q43.428 0 80.254-21.461t58.286-58.286 21.461-80.254-21.461-80.254-58.286-58.285-80.254-21.46-80.254 21.46-58.285 58.285-21.46 80.254 21.46 80.254 58.285 58.286 80.254 21.461z"
          fill="currentColor"
          fillRule="evenodd"
        ></path>
      </svg>
      <Link to="/search">
        <a className="text-gray-300 text-sm font-bold hover:text-white capitalize">
          Search
        </a>
      </Link>
    </button>
    <button className="text-gray-200 hover:text-white flex items-center mt-4">
      <svg
        className="mr-4"
        viewBox="0 0 512 512"
        width="24"
        height="24"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M291.301 81.778l166.349 373.587-19.301 8.635-166.349-373.587zM64 463.746v-384h21.334v384h-21.334zM192 463.746v-384h21.334v384h-21.334z"
          fill="currentColor"
        ></path>
      </svg>
      <Link to="/albums/1">
        <a className="text-gray-300 text-sm font-bold hover:text-white capitalize">
          Your Library
        </a>
      </Link>

    </button>
    <button className="text-gray-200 hover:text-white flex items-center mt-4">
      <svg
        className="mr-4"
        viewBox="0 0 512 512"
        width="24"
        height="24"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          d="M291.301 81.778l166.349 373.587-19.301 8.635-166.349-373.587zM64 463.746v-384h21.334v384h-21.334zM192 463.746v-384h21.334v384h-21.334z"
          fill="currentColor"
        ></path>
      </svg>
      <Link to="/messages">
        <a className="text-gray-300 text-sm font-bold hover:text-white capitalize">
          Messages
        </a>
      </Link>

    </button>
    <div className="mt-10 mb-3 border-b border-gray-700">
      <button className="flex items-center text-black">
        <svg
          className="fill-current hover:bg-white mr-4 p-1"
          role="img"
          height="24"
          width="24"
          viewBox="0 0 16 16"
          color="#fff"
        >
          <path d="M14 7H9V2H7v5H2v2h5v5h2V9h5z"></path>
          <path fill="none" d="M0 0h16v16H0z"></path>
        </svg>
        <a
          className="text-gray-300 text-sm font-bold hover:text-white capitalize"
          >Create Playlist</a>
      </button>
      <button
        className="flex items-center text-green-500 my-3 hover:text-white"
      >
        <svg
          className="fill-emerald-600 mr-4"
          role="img"
          height="24"
          width="24"
          viewBox="0 0 16 16"
          color="#fff"

        >
          <path fill="none" d="M0 0h16v16H0z"></path>
          <path
            d="M13.797 2.727a4.057 4.057 0 00-5.488-.253.558.558 0 01-.31.112.531.531 0 01-.311-.112 4.054 4.054 0 00-5.487.253c-.77.77-1.194 1.794-1.194 2.883s.424 2.113 1.168 2.855l4.462 5.223a1.791 1.791 0 002.726 0l4.435-5.195a4.052 4.052 0 001.195-2.883 4.057 4.057 0 00-1.196-2.883z"
          ></path>
        </svg>
        <a
          className="text-gray-300 text-sm font-bold hover:text-white capitalize"
          >Liked Songs</a>
      </button>
    </div>
    <div className="flex -space-x-3 rtl:space-x-reverse">
      <img className="w-10 h-10 border-2 border-white rounded-full dark:border-gray-800" src={des} alt=""/>
      <img className="w-10 h-10 border-2 border-white rounded-full dark:border-gray-800" src={des} alt=""/>
      <img className="w-10 h-10 border-2 border-white rounded-full dark:border-gray-800" src={des} alt=""/>
      <img className="w-10 h-10 border-2 border-white rounded-full dark:border-gray-800" src={des} alt=""/>
    </div>
  </div>
  );
};

export default Sidebar;