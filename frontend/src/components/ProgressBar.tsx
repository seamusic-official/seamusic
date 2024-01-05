import des from "../assets/everydesigner.png"

export default function ProgressBar() {
  return (     
<div style={{zIndex: '9999'}} className="dark:border-neutral-800 border-t bg-zinc-800/30 dark:from-inherit backdrop-blur-lg fixed left-0 bottom-0 right-0 h-auto flex justify-between flex-row items-center">
    <div className="mx-2 my-2 flex justify-start items-center w-1/3">
      <img
        src={des}
        alt=""
        className="shadow-2xl rounded-md w-24 h-24"
      />
      <div className="flex flex-col justify-center m-4">
        <h5 id="song-name" className="text-white font-semi-bold text-sm text-left">
          The Spectre
        </h5>
        <p id="artist-name" className="text-gray-400 font-semi-bold text-xs">
          Alan Walker
        </p>
      </div>
      <div className="text-gray-300 flex justify-center items-center">
        <svg
          className="fill-current ml-2"
          role="img"
          height="16"
          width="16"
          viewBox="0 0 16 16"
        >
          <path
            d="M13.764 2.727a4.057 4.057 0 00-5.488-.253.558.558 0 01-.31.112.531.531 0 01-.311-.112 4.054 4.054 0 00-5.487.253A4.05 4.05 0 00.974 5.61c0 1.089.424 2.113 1.168 2.855l4.462 5.223a1.791 1.791 0 002.726 0l4.435-5.195A4.052 4.052 0 0014.96 5.61a4.057 4.057 0 00-1.196-2.883zm-.722 5.098L8.58 13.048c-.307.36-.921.36-1.228 0L2.864 7.797a3.072 3.072 0 01-.905-2.187c0-.826.321-1.603.905-2.187a3.091 3.091 0 012.191-.913 3.05 3.05 0 011.957.709c.041.036.408.351.954.351.531 0 .906-.31.94-.34a3.075 3.075 0 014.161.192 3.1 3.1 0 01-.025 4.403z"
          ></path>
        </svg>
        <svg
          className="ml-4"
          width="16"
          height="16"
          xmlns="http://www.w3.org/2000/svg"
        >
          <g fill="currentColor" fill-rule="evenodd">
            <path
              d="M1 3v9h14V3H1zm0-1h14a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H1a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1z"
              fill-rule="nonzero"
            ></path>
            <path d="M10 8h4v3h-4z"></path>
          </g>
        </svg>
      </div>
    </div>
    <div
      className="w-2/5 flex flex-col justify-center items-center m-0 p-0 border-0"
    >
      <div
        className="text-gray-300 mb-3 flex justify-between w-2/5 items-center"
      >
        <svg
          className="fill-current"
          role="img"
          height="16"
          width="16"
          viewBox="0 0 16 16">
        
          <path
            d="M4.5 6.8l.7-.8C4.1 4.7 2.5 4 .9 4v1c1.3 0 2.6.6 3.5 1.6l.1.2zm7.5 4.7c-1.2 0-2.3-.5-3.2-1.3l-.6.8c1 1 2.4 1.5 3.8 1.5V14l3.5-2-3.5-2v1.5zm0-6V7l3.5-2L12 3v1.5c-1.6 0-3.2.7-4.2 2l-3.4 3.9c-.9 1-2.2 1.6-3.5 1.6v1c1.6 0 3.2-.7 4.2-2l3.4-3.9c.9-1 2.2-1.6 3.5-1.6z"
          ></path>
        </svg>
        <svg
          className="fill-current"
          role="img"
          height="16"
          width="16"
          viewBox="0 0 16 16"
        >
          <path d="M13 2.5L5 7.119V3H3v10h2V8.881l8 4.619z"></path>
        </svg>
        <button
        id="play-btn"
          className="bg-white rounded-full w-8 h-8 flex justify-center items-center"
        >
          <svg
            role="img"
            height="16"
            width="16"
            viewBox="0 0 16 16"
            className="Svg-ulyrgf-0 hJgLcF"
          >
            <path fill="none" d="M0 0h16v16H0z"></path>
            <path d="M3 2h3v12H3zM10 2h3v12h-3z"></path>
          </svg>
        </button>
        <svg
          className="fill-current"
          role="img"
          height="16"
          width="16"
          viewBox="0 0 16 16"
        >
          <path d="M11 3v4.119L3 2.5v11l8-4.619V13h2V3z"></path>
        </svg>
        <svg
          className="fill-current"
          role="img"
          height="16"
          width="16"
          viewBox="0 0 16 16"
        >
          <path
            d="M5.5 5H10v1.5l3.5-2-3.5-2V4H5.5C3 4 1 6 1 8.5c0 .6.1 1.2.4 1.8l.9-.5C2.1 9.4 2 9 2 8.5 2 6.6 3.6 5 5.5 5zm9.1 1.7l-.9.5c.2.4.3.8.3 1.3 0 1.9-1.6 3.5-3.5 3.5H6v-1.5l-3.5 2 3.5 2V13h4.5C13 13 15 11 15 8.5c0-.6-.1-1.2-.4-1.8z"
          ></path>
        </svg>
      </div>
      <div className="flex flex-row justify-between items-center w-full">
        <div id="time-elapsed" className="text-gray-300 text-xs text-center">1:41</div>
        <div
          className="bg-gray-600 flex w-full h-full border border-gray-600 rounded-full mx-4"
        >
          <div
          id="progress"
            className="bg-gray-300 border border-gray-300 rounded-full w-0 h-1"
          ></div>
        </div>
        <div id="duration" className="text-gray-300 text-xs text-center">3:04</div>
      </div>
    </div>
    <div className="flex flex-row justify-end items-center w-1/3 mr-4">
      <div
        className="flex justify-center w-2/5 items-center text-gray-300"
      >
        <svg
          className="fill-current m-4"
          height="20"
          width="20"
          viewBox="0 0 48 48"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path d="M0 0h48v48H0z" fill="none" />
          <path
            d="M30 12H6v4h24v-4zm0 8H6v4h24v-4zM6 32h16v-4H6v4zm28-20v16.37c-.63-.23-1.29-.37-2-.37-3.31 0-6 2.69-6 6s2.69 6 6 6 6-2.69 6-6V16h6v-4H34z"
          />
        </svg>
        <svg
          className="fill-current mr-2"
          role="img"
          height="16"
          width="16"
          viewBox="0 0 16 16"
        >
          <path
            d="M12.945 1.379l-.652.763c1.577 1.462 2.57 3.544 2.57 5.858s-.994 4.396-2.57 5.858l.651.763a8.966 8.966 0 00.001-13.242zm-2.272 2.66l-.651.763a4.484 4.484 0 01-.001 6.397l.651.763c1.04-1 1.691-2.404 1.691-3.961s-.65-2.962-1.69-3.962zM0 5v6h2.804L8 14V2L2.804 5H0zm7-1.268v8.536L3.072 10H1V6h2.072L7 3.732z"
          ></path>
        </svg>

        <div
          className="bg-gray-300 border border-gray-300 rounded-full w-3/5 h-1"

        ></div>
      </div>
    </div>
  </div>
  

  )
}
