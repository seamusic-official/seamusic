import React, { useState } from 'react'
import MainLayout from '../../components/layouts/MainLayout'
import { Link, useNavigate } from 'react-router-dom'
import AuthService from '../../services/AuthService'
import HelloLayout from '../../components/layouts/HelloLayout'
import DecorText from '../../components/DecorText'
import Input from '../../components/Input'

export default function Register() {
  const [username, setUsername] = useState("")
  const [role, setRole] = useState("")
  const [year, setYear] = useState(0)
  const [month, setMonth] = useState(0)
  const [day, setDay] = useState(0) 
  const [password, setPassword] = useState("")
  const [email, setEmail] = useState("")
  const navigate = useNavigate()

  const handleSubmit = async (event) => {
    event.preventDefault();
    const birthday = new Date(year, month - 1, day);

    try {
        const response = await AuthService.register(username, role, birthday.toISOString().split('T')[0], password, email);
        navigate("/auth/login")
        console.log('Registration successful:', response.data);
      } catch (error) {
            console.error('Error during registration:', error);
        }
    };


  return (
    <HelloLayout>
    <div className='flex justify-center items-center my-10'>
        <div>
          <div className="flex justify-center mb-48">
              <div className="lg:w-[1200px] md:w-156 w-108 pb-3 ">
              <h1 className="text-white flex justify-center m-2 font-extrabold text-3xl xl:text-4xl mt-6">
                <div>
                  Registration on <DecorText font="extrabold">SeaMusic</DecorText> 
                </div>
          </h1>

        <form onSubmit={handleSubmit}>
          <div className="flex-col justify-center w-11/12 md:w-4/6 lg:w-4/6 mx-auto ">
            <div className="flex-grow mt-4">
              <label htmlFor="email" className="inline-block font-extrabold text-xs my-2 tracking-wider "><span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>*</span>What's your
                email?
              </label>
              <Input 
                id="email"
                className="w-full py-2 px-2 border text-gray-900 border-gray-700 placeholder-gray-600 rounded-lg text-xs"
                type="email"
                placeholder="Enter your email."
                onChange={(e) => setEmail(e.target.value)}
                />
            </div>
            <div className="flex-grow mt-4">
              <label htmlFor="password" className="inline-block  font-extrabold text-xs my-2 tracking-wider "><span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>*</span>Create a password
              </label>
              <Input 
                id="password"
                className="w-full py-2 px-2 border text-gray-900 border-gray-700 placeholder-gray-600 rounded-lg text-xs"
                type="password" 
                placeholder="Create a password."
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
            <div className="flex-grow mt-4">
              <label htmlFor="profile_name" className="inline-block font-extrabold text-xs my-2 tracking-wider "><span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>*</span>What should we
                call you?</label><br/>
              <Input 
                id="profile_name"
                className="w-full py-2 px-2 border text-gray-900 border-gray-700 placeholder-gray-600 rounded-lg text-xs"
                type="text" 
                placeholder="Enter a username"
                onChange={(e) => setUsername(e.target.value)}
              />
            </div>
            <span className="block mt-2 text-xs font-semibold tracking-wide">This appears on your profile.</span>
            <div className="flex-grow mt-4">
              <span className="inline-block font-extrabold text-xs mt-2 mb-1 tracking-wider "><span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>*</span>What's your date of
                birth?</span>
              <div className="grid grid-cols-4 gap-4 text-xs font-semibold">
                <div className="col-span-2">
                <label className="block tracking-wide mb-1 " htmlFor="month"><span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>*</span> Month</label>

                  <div className="flex items-start rounded">
                  <select 
                        name="month" 
                        id="month"
                        className="tracking-tighter block p-2.5 w-full text-sm rounded-md font-bold  border-neutral-800 rounded-s-2 border bg-zinc-800/30 placeholder-neutral-700 text-white"
                        onChange={(e) => setMonth(e.target.value)}
                    >
                        <option value="" disabled selected>Month</option>
                        <option value="01">January</option>
                        <option value="02">February</option>
                        <option value="03">March</option>
                        <option value="04">April</option>
                        <option value="05">May</option>
                        <option value="06">June</option>
                        <option value="07">July</option>
                        <option value="08">August</option>
                        <option value="09">September</option>
                        <option value="10">October</option>
                        <option value="11">November</option>
                        <option value="12">December</option>
                    </select>

                  </div>
                </div>
                <div className="px-2">
                  <label className="block tracking-wide mb-1 " htmlFor="day"><span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>*</span> Day</label>
                  <Input 
                    id="day"
                    className="w-full text-gray-900 py-2 px-2 border border-gray-500 placeholder-gray-600 rounded-lg text-xs focus:outline-none focus:border-gray-900"
                    type="text" 
                    placeholder="DD" 
                    onChange={(e) => setDay(e.target.value)}
                    />
                </div>
                <div>
                  <label className="block tracking-wide mb-1 " htmlFor="year"><span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>*</span> Year</label>
                  <Input 
                    id="year"
                    className="w-full text-gray-900 py-2 px-2 border border-gray-500 placeholder-gray-600 rounded-lg text-xs focus:outline-none focus:border-gray-900"
                    type="text" 
                    placeholder="YYYY" 
                    onChange={(e) => setYear(e.target.value)}
                    />
                </div>
              </div>
            </div>
            <div className="flex-col mt-4">
              <span className="mb-1 block font-extrabold text-xs my-2 tracking-wider"><span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>*</span> Who are you?</span>
              <div className="flex">
              <label htmlFor="artist" className="flex ">
                  <input 
                    id="artist" 
                    type="radio" 
                    name="role" 
                    value="Artist"
                    className="my-auto hover:color-red-700"
                    onChange={(e) => setRole(e.target.value)}
                  />
                  <span className="text-xs my-auto ml-3 mr-8 text-center font-semibold tracking-wide">Artist</span>
              </label>
              <label htmlFor="beatmaker" className="flex ">
                  <input 
                    id="beatmaker" 
                    type="radio" 
                    name="role" 
                    value="Producer"
                    className="my-auto border-solid border-green-900"
                    onChange={(e) => setRole(e.target.value)}
                  />
                  <span className="text-xs my-auto ml-3 mr-8 text-center font-semibold tracking-wide">Producer</span>
              </label>
              <label htmlFor="listener" className="flex ">
                  <input 
                    id="listener" 
                    defaultChecked 
                    type="radio" 
                    name="role" 
                    value="Listener"
                    className="my-auto" 
                    onChange={(e) => setRole(e.target.value)}
                  />
                  <span className="text-xs my-auto ml-3 mr-8 text-center font-semibold tracking-wide">Listener</span>
              </label>
          </div>


              <br />
              <div className="text-xs tracking-wide font-medium ">
                <span className="inline-block text-center  mb-3">By clicking on Sign up, you agree to Spotify's <a href=""
                    className="text-emerald-600 underline"> Terms and Conditions of Use.</a></span>
                <span className="inline-block mx-2 text-center  mb-3">To learn more about how Spotify collects, uses, shares
                  and protects your personal data please read Spotify's <a href="#" className="text-emerald-600 underline">
                    Privacy Policy.</a></span>
                <button
                  className="w-full transition duration-200 ease-in-out p-2 uppercase text-sm font-bold text-white bg-emerald-600  rounded-full tracking-widest hover:bg-emerald-700 transform hover:scale-105 focus:scale-100 focus:bg-emerald-800 outline-none"
                  type="submit">
                    SIGN UP
                </button>
                <div className=" text-center text-sm my-6">Have an account? <Link to="/auth/login"><a className="text-emerald-600 underline">Login</a>.</Link></div>
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
