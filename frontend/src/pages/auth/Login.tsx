import { Link, useNavigate } from 'react-router-dom'
import MainLayout from '../../components/layouts/MainLayout'
import { useState } from 'react'
import AuthService from '../../services/AuthService'
import { useAppDispatch } from '../../hooks/redux'
import { setAuthData } from '../../store/reducers/authSlice'
import HelloLayout from '../../components/layouts/HelloLayout'
import Input from '../../components/inputs/Input'

export default function Login() {
  const [password, setPassword] = useState("")
  const [email, setEmail] = useState("")
  const [error, setError] = useState("")
  
  const AUTH_URL = `https://accounts.spotify.com/authorize?client_id=${import.meta.env.VITE_CLIENT_ID}&response_type=code&redirect_uri=${import.meta.env.VITE_REDIRECT_URI}`
  const navigate = useNavigate()
  const dispatch = useAppDispatch()

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
        const response = await AuthService.login(email, password);
        console.log("GDSFHJMK<FSDFSDFESFDS");
        console.log(password);

        if (response && response.status === 401) {
            setError("You're not registered, please register");
        } else {
            const authData = {
                accessToken: response.data.accessToken,
                refreshToken: response.data.refreshToken,
                expiresInToken: response.data.expiresInToken,
                user: response.data.user
            };

            localStorage.setItem('accessToken', authData.accessToken);
            dispatch(setAuthData(authData)); // Dispatching setAuthData action with authData payload
            console.log('Authentication successful:', authData);
            navigate("/profile");
        }
    } catch (e) {
        console.error('Error during authentication:', e);
    }
};
  return (
    <HelloLayout>
    <div className='flex justify-center items-center my-16'>
      <div>
        <div className="flex justify-center mb-48">
            <div className="lg:w-[1200px] md:w-[1000px] w-108 pb-3 ">
            <h1 className="text-white flex justify-center m-2 font-extrabold xl:text-4xl tracking-tighter text-3xl mt-6">
          Login on <span className='ml-2 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>SeaMusic</span>
        </h1>


          <form onSubmit={handleSubmit}>
            <div className="flex-col justify-center w-11/12 md:w-4/6 lg:w-4/6 mx-auto ">
              <div className="mt-8">
              <button
                  className="w-full m-1 p-2 uppercase hover:text-black transition duration-200 ease-in-out text-sm font-bold text-white bg-zinc-800/30  rounded-full tracking-widest hover:bg-gray-200 transform hover:scale-105 focus:scale-100 focus:bg-emerald-600 outline-none">
                    <span className=''>SIGN IN THROUGH GOOGLE</span>
                </button>
                <button
                  className="w-full m-1 p-2 transition duration-200 ease-in-out uppercase text-sm font-bold text-white bg-emerald-700  rounded-full tracking-widest hover:bg-emerald-800 transform hover:scale-105 focus:scale-100 focus:bg-emerald-600 outline-none">
                    <a className="no-underline " href={AUTH_URL}>SIGN IN THROUGH SPOTIFY</a>
                </button>
              </div>          
              <div className="flex-grow mt-4">
                <label htmlFor="email" className="inline-block font-extrabold text-xs my-2 tracking-wider ">
                  <span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>
                    *
                  </span>
                    Your email
                  </label>
                <Input 
                  id="email"
                  onChange={(e) => setEmail(e.target.value)}
                  type="email" 
                  placeholder="Enter your email." />
              </div>
              <div className="flex-grow mt-4">
                <label htmlFor="password" className="inline-block  font-extrabold text-xs my-2 tracking-wider "><span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>*</span>Your password
                </label>
                <Input 
                  id="password"
                  onChange={(e) => setPassword(e.target.value)}
                  type="password" 
                  placeholder="Create a password."/>
              </div>
              <div className="flex-col mt-4">
                <p className="inline-block font-bold text-md my-2 tracking-wider">
                  {error}
                </p>
                <br />
                <div className="text-xs tracking-wide font-medium ">
                  <button
                    type="submit"
                    className="w-full p-2 uppercase text-sm font-bold text-white bg-emerald-600 transition duration-200 ease-in-out rounded-full tracking-widest hover:bg-emerald-700 transform hover:scale-105 focus:scale-100 focus:bg-emerald-800 outline-none">SIGN
                    IN
                  </button>
                  <div className=" text-center text-sm my-6">Don't you have an account? <Link to="/auth/register"><a className="text-emerald-700 underline">Registration</a></Link>.</div>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
    </HelloLayout>
  )
}
