import MainLayout from '../../components/layouts/MainLayout'
import des from '../../assets/everydesigner.png'
import { Link } from 'react-router-dom'
import Input from '../../components/Input'
import { useAppSelector } from '../../hooks/redux';

export default function MessagesDetail() {
  const user = useAppSelector((state) => state.auth.user);

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
              <img className="w-10 h-10 rounded-full" src={des} alt=""/>
              <div className="m-2">
                <p className="text-lg font-bold">xxxmanera</p>
                <p className="text-gray-300 text-md font-semibold">сколько exc стоит бро?</p>
              </div>
            </div>
          </div>
        
          <div className="flex justify-end">
            <div className="flex items-center">
              <div className="m-2">
                <p className="flex text-lg font-bold justify-end">{user.username}</p>
                <p className="text-gray-300 flex text-md justify-end font-semibold">50$</p>
              </div>
              <img className="w-8 h-8 border-2 border-white rounded-full dark:border-gray-800" src={des} alt=""/>
            </div>
          </div>

        </div>
        <div className="">
          <Input buttonText="Send" placeholderText="Write a message.." addictButtonText="Add"/>
        </div>
      </div>
    </MainLayout>
  )
}
