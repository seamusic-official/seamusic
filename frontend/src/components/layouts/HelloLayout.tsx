import React, { useRef } from 'react'
import Footer from '../Footer'
import DropdownMenu from '../Dropdown'
import DefaultButton from '../buttons/DefaultButton'
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';


type MyComponentProps = React.PropsWithChildren;

export default function HelloLayout({ children }: MyComponentProps) {
  const dropdownRef = useRef(null);

  return (
    <div className='p-4'>
        <div className="relative z-[-20] w-24 h-24 fixed top-0 left-0 z-0">
            <div className="bg-gradient-to-br  rounded-full from-blue-400 to-purple-800 opacity-80 w-full h-full"></div>
        </div>

        <div className='p-2 fixed top-0 right-0 left-0  backdrop-blur-md z-20 border-neutral-800 border-b'>
            <div className="flex justify-between mx-4 items-center">
                <div className="text-gray-100 my-2 cursor-pointer">
                    <h2 className="mt-1 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter" id="">
                        <Link to="/">
                            SeaMusic
                        </Link>
                    </h2>
                </div>
                <ul className="w-full flex justify-center font-semibold p-4 p-0 mt-4 border border-gray-100  flex-row mt-0 border-0">
                    <li>
                    <a href="#" className="block py-2 px-5 text-white rounded hover:bg-gray-100" aria-current="page">Home</a>
                    </li>
                    <li>
                    <a href="#" className="block py-2 px-5 text-white rounded hover:bg-gray-100">Services</a>
                    </li>
                    <li>
                    <a href="#" className="block py-2 px-5 text-white rounded hover:bg-gray-100">Pricing</a>
                    </li>
                    <li>
                    <a href="#" className="block py-2 px-5 text-white rounded hover:bg-gray-100">Contact</a>
                    </li>
                </ul>                
                <div className="flex justify-between items-center">

                    <DropdownMenu reference={dropdownRef}/>
                </div>
            </div>
        </div>
        <div className=''>

        {children}
        </div>
        <div>
            <Footer />
        </div>
    </div>
  )
}
