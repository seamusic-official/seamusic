import React from 'react'
import { Link } from 'react-router-dom'

export default function NavBar() {
  return (
    <div className="">
    <div className="flex justify-between items-center flex-wrap md:hidden">
    <button className="text-white">
      <svg
        className="fill-current"
        role="img"
        focusable="false"
        height="24"
        width="24"
        viewBox="0 0 24 24"
      >
        <polyline
          points="16 4 7 12 16 20"
          fill="none"
          stroke="#fff"
        ></polyline>
      </svg>
    </button>
    <button className="text-gray-300">
      <svg
        className="bg-black border rounded-full p-1"
        width="32"
        height="32"
        fill="currentColor"
        viewBox="0 0 18 20"
        xmlns="http://www.w3.org/2000/svg"
        data-testid="user-icon"
      >
        <path
          d="M15.216 13.717L12 11.869C11.823 11.768 11.772 11.607 11.757 11.521C11.742 11.435 11.737 11.267 11.869 11.111L13.18 9.57401C14.031 8.58001 14.5 7.31101 14.5 6.00001V5.50001C14.5 3.98501 13.866 2.52301 12.761 1.48601C11.64 0.435011 10.173 -0.0879888 8.636 0.0110112C5.756 0.198011 3.501 2.68401 3.501 5.67101V6.00001C3.501 7.31101 3.97 8.58001 4.82 9.57401L6.131 11.111C6.264 11.266 6.258 11.434 6.243 11.521C6.228 11.607 6.177 11.768 5.999 11.869L2.786 13.716C1.067 14.692 0 16.526 0 18.501V20H1V18.501C1 16.885 1.874 15.385 3.283 14.584L6.498 12.736C6.886 12.513 7.152 12.132 7.228 11.691C7.304 11.251 7.182 10.802 6.891 10.462L5.579 8.92501C4.883 8.11101 4.499 7.07201 4.499 6.00001V5.67101C4.499 3.21001 6.344 1.16201 8.699 1.00901C9.961 0.928011 11.159 1.35601 12.076 2.21501C12.994 3.07601 13.5 4.24301 13.5 5.50001V6.00001C13.5 7.07201 13.117 8.11101 12.42 8.92501L11.109 10.462C10.819 10.803 10.696 11.251 10.772 11.691C10.849 12.132 11.115 12.513 11.503 12.736L14.721 14.585C16.127 15.384 17.001 16.884 17.001 18.501V20H18.001V18.501C18 16.526 16.932 14.692 15.216 13.717Z"
        ></path>
      </svg>
    </button>
  </div>
  <div className="hidden flex justify-between md:flex">
    <div className="flex">
      <svg
        className="bg-black rounded-full bg-opacity-60 p-1"
        role="img"
        focusable="false"
        height="32"
        width="32"
        viewBox="0 0 24 24"
      >
        <polyline
          points="16 4 7 12 16 20"
          fill="none"
          stroke="#fff"
        ></polyline>
      </svg>
      <svg
        className="bg-black rounded-full bg-opacity-80 p-1 ml-4"
        role="img"
        focusable="false"
        height="32"
        width="32"
        viewBox="0 0 24 24"
      >
        <polyline
          points="8 4 17 12 8 20"
          fill="none"
          stroke="#fff"
        ></polyline>
      </svg>
    </div>
    <div className="flex items-center">
    <Link to="/dashboard">
      <button
        type="button"
        className="text-white uppercase text-xs font-extrabold text-opacity-90 tracking-widest bg-black bg-opacity-70 border border-gray-300 rounded-full px-8 py-2 mr-6 hover:bg-black"
      >
        LOGO
      </button>
    </Link>
    <Link to="/dashboard">
      <button
        type="button"
        className="text-white uppercase text-xs font-extrabold text-opacity-90 tracking-widest bg-black bg-opacity-70 border border-gray-300 rounded-full px-8 py-2 mr-6 hover:bg-black"
      >
        My studio
      </button>
    </Link>
    <Link to="/profile">
      <button
        type="button"
        className="text-white  text-sm font-bold bg-black rounded-full px-1 py-1 flex items-center bg-opacity-80 hover:bg-gray-800"
      >
          <svg
            className="bg-gray-800 rounded-full p-1 border border-gray-700"
            width="24"
            height="24"
            fill="currentColor"
            viewBox="0 0 18 20"
            xmlns="http://www.w3.org/2000/svg"
            data-testid="user-icon"
          >
            <path
              d="M15.216 13.717L12 11.869C11.823 11.768 11.772 11.607 11.757 11.521C11.742 11.435 11.737 11.267 11.869 11.111L13.18 9.57401C14.031 8.58001 14.5 7.31101 14.5 6.00001V5.50001C14.5 3.98501 13.866 2.52301 12.761 1.48601C11.64 0.435011 10.173 -0.0879888 8.636 0.0110112C5.756 0.198011 3.501 2.68401 3.501 5.67101V6.00001C3.501 7.31101 3.97 8.58001 4.82 9.57401L6.131 11.111C6.264 11.266 6.258 11.434 6.243 11.521C6.228 11.607 6.177 11.768 5.999 11.869L2.786 13.716C1.067 14.692 0 16.526 0 18.501V20H1V18.501C1 16.885 1.874 15.385 3.283 14.584L6.498 12.736C6.886 12.513 7.152 12.132 7.228 11.691C7.304 11.251 7.182 10.802 6.891 10.462L5.579 8.92501C4.883 8.11101 4.499 7.07201 4.499 6.00001V5.67101C4.499 3.21001 6.344 1.16201 8.699 1.00901C9.961 0.928011 11.159 1.35601 12.076 2.21501C12.994 3.07601 13.5 4.24301 13.5 5.50001V6.00001C13.5 7.07201 13.117 8.11101 12.42 8.92501L11.109 10.462C10.819 10.803 10.696 11.251 10.772 11.691C10.849 12.132 11.115 12.513 11.503 12.736L14.721 14.585C16.127 15.384 17.001 16.884 17.001 18.501V20H18.001V18.501C18 16.526 16.932 14.692 15.216 13.717Z"
            ></path>
          </svg>
          <span className="px-3">whyspxcyyy?</span>
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
        </Link>
    </div>
  </div>
  </div>
  )
}
