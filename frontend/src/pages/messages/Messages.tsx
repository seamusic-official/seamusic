import MainLayout from '../../components/layouts/MainLayout'
import des from '../../assets/everydesigner.png'
import { Link } from 'react-router-dom'

export default function Messages() {
  return (
    <MainLayout>
      <div className="mt-2 ">
        <div className="flex items-center ">
          <div className="relative">
            <img className="w-10 h-10 border-2 border-white rounded-full dark:border-gray-800" src={des} alt=""/>
            <span className=  "bottom-0 left-7 absolute  w-3.5 h-3.5 bg-green-400 border-2 border-white dark:border-gray-800 rounded-full"></span>
          </div>
          <div className="p-2">
            <p className="font-semibold">xxxmanera</p>
            <p className="text-sm font-semibold text-gray-300">печатает..</p>
          </div>
          <Link to="/profile">
            <button
              type="button"
              className="justify-end ml-2 text-white uppercase text-xs font-extrabold text-opacity-90 tracking-widest bg-black bg-opacity-70 border border-gray-300 rounded-full px-8 py-2 mr-6 hover:bg-black"
            >
              Profile
            </button>
          </Link>
        </div>

        <div className="p-2 overflow-y-auto max-w-screen block">
          <div className="left">
            <div className="flex items-center ">
              <img className="w-8 h-8 border-2 border-white rounded-full dark:border-gray-800" src={des} alt=""/>
              <div className="p-2">
                <p className="text-sm font-bold">xxxmanera</p>
                <p className="text-gray-300 text-sm font-semibold">сколько exc стоит бро?</p>
              </div>
            </div>
          </div>
        
          <div className="flex justify-end">
            <div className="flex items-center">
              <div className="p-2">
                <p className="flex text-sm font-bold justify-end">whyspxcyyy</p>
                <p className="text-gray-300 flex text-sm justify-end font-semibold">50$</p>
              </div>
              <img className="w-8 h-8 border-2 border-white rounded-full dark:border-gray-800" src={des} alt=""/>
            </div>
          </div>

        </div>
        <form className="fixed bottom-36 ">
          <div className="flex">
            <button id="dropdown-button" data-dropdown-toggle="dropdown" className="flex-shrink-0 z-10 inline-flex items-center py-2.5 px-4 text-sm font-medium text-center text-gray-900 bg-gray-100 border border-e-0 border-gray-300 dark:border-gray-700 dark:text-white rounded-s-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-300 dark:bg-gray-900 dark:hover:bg-gray-700 dark:focus:ring-gray-800" type="button">All categories <svg className="w-2.5 h-2.5 ms-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
            </svg>
          </button>
          <div id="dropdown" className="z-10 hidden bg-white divide-y divide-gray-100 rounded-lg shadow w-44 dark:bg-gray-700">
              <ul className="py-2 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdown-button">
              <li>
                  <a href="#" className="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Shopping</a>
              </li>
              <li>
                  <a href="#" className="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Images</a>
              </li>
              <li>
                  <a href="#" className="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">News</a>
              </li>
              <li>
                  <a href="#" className="block px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Finance</a>
              </li>
              </ul>
          </div>
          <div className="relative w-full">
              <input type="search" id="search-dropdown" className="block p-2.5 w-full z-20 text-sm rounded-e-lg rounded-s-gray-100 rounded-s-2 border bg-gray-900 border-gray-700 placeholder-gray-700 text-white" placeholder="Search" required />
              <button type="submit" className="font-semibold absolute top-0 end-0 p-2.5 h-full text-sm font-medium text-white bg-emerald-700 rounded-e-lg border border-emerald-700 hover:bg-emerald-800 focus:ring-4 focus:outline-none focus:ring-emerald-300 dark:bg-emerald-600 dark:hover:bg-emerald-700 dark:focus:ring-emerald-800">
               Send
              </button>
          </div>
      </div>
  </form>
      </div>
    </MainLayout>
  )
}
