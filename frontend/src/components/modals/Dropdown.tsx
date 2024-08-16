import React, { useEffect, useRef, useState } from 'react';
import { Link, redirect } from 'react-router-dom';
import { useAppDispatch, useAppSelector } from '../../hooks/redux';
import Logout from '../Logout';

const DropdownMenu = ({ reference }) => {
  const {isAuthenticated, user} = useAppSelector((state) => state.auth)
  const [isOpen, setIsOpen] = useState(false);

  const toggleDropdown = () => {
    setIsOpen(!isOpen);
  };

  const handleClickOutside = (event) => {
    if (reference.current && !reference.current.contains(event.target)) {
      setIsOpen(false);
    }
  };

  useEffect(() => {
    document.addEventListener("click", handleClickOutside, true);
    return () => {
      document.removeEventListener("click", handleClickOutside, true);
    };
  }, []);

  const redirectToLogin = () => {
    return redirect("/auth/login")
  }

  return (
    <div className="relative " ref={reference}>
      <button
        type="button"
        className="flex flex-row items-center text-white text-sm font-bold rounded-full p-2 flex items-center bg-opacity-5  bg-gray-200"
        onClick={isAuthenticated ? (toggleDropdown) : (redirectToLogin)}

      >
          <img className="bg-gray-300 rounded-full border border-gray-700 w-6 h-6" src={user.picture_url} alt="" />

          {isAuthenticated ? (
            <span className="px-2">{user.username}</span>
          ): (
            <span className="px-2"><Link to="/auth/login">LOGIN</Link></span>
          )}
          <svg
            className="fill-current"
            role="img"
            height="16"
            width="16"
            viewBox="0 0 16 16"
          >
            <path d="M3 6l5 5.794L13 6z"></path>
          </svg>
      </button>

      {isOpen && (
        <div className="p-2 absolute rounded-md right-0 mt-2 py-1 w-[175px] border border-neutral-800 bg-gradient-to-b bg-black from-zinc-200   dark:bg-zinc-800/30 dark:from-inherit z-20 lg:bg-gray-200 lg:p-2 lg:dark:bg-zinc-800/30">
            <button className="text-gray-200  hover:text-white flex items-center">
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
              <Link to="/profile">
                <a className="text-gray-200 text-sm font-bold hover:text-white capitalize">
                  PROFILE
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
                <a className="text-gray-200 text-sm font-bold hover:text-white capitalize">
                  SEARCH
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
                <a className="text-gray-200 text-sm font-bold hover:text-white capitalize">
                  MESSAGES
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
              <Link to="/dashboard">
                <a className="text-gray-200 text-sm font-bold hover:text-white capitalize">
                  DASHBOARD
                </a>
              </Link>

            </button>
          {isAuthenticated ? (
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
                        <Logout/>
                      </button>
          ): (
            <></>
          )}
        </div>
      )}
    </div>
  );
};

export default DropdownMenu;