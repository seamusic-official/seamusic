import React, { useState } from 'react'
import MainLayout from '../../components/layouts/MainLayout'
import { Link, useNavigate } from 'react-router-dom'
import AuthService from '../../services/AuthService'

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
    <MainLayout>
        <div className="flex justify-center mb-32">
            <div className="lg:w-[1200px] md:w-156 w-108 pb-3 ">
            <h1 className="text-white flex justify-center m-2 font-extrabold text-2xl mt-6">
        Registration on <span className='ml-2 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>SeaMusic</span>
        </h1>

      <form onSubmit={handleSubmit}>
        <div className="flex-col justify-center w-11/12 md:w-4/6 lg:w-4/6 mx-auto ">
          <div className="flex-grow mt-4">
            <label htmlFor="email" className="inline-block font-extrabold text-xs my-2 tracking-wider "><span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>*</span>What's your
              email?
            </label>
            <input 
              id="email"
              className="w-full py-2 px-2 border text-gray-900 border-gray-700 placeholder-gray-600 rounded-lg text-xs"
              type="text"
              placeholder="Enter your email."
              onChange={(e) => setEmail(e.target.value)}
              />
          </div>
          <div className="flex-grow mt-4">
            <label htmlFor="password" className="inline-block  font-extrabold text-xs my-2 tracking-wider "><span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>*</span>Create a password
            </label>
            <input 
              id="password"
              className="w-full py-2 px-2 border text-gray-900 border-gray-700 placeholder-gray-600 rounded-lg text-xs"
              type="text" 
              placeholder="Create a password."
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <div className="flex-grow mt-4">
            <label htmlFor="profile_name" className="inline-block font-extrabold text-xs my-2 tracking-wider "><span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>*</span>What should we
              call you?</label><br/>
            <input 
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
                <label className="block" htmlFor="month">Month</label>
                <div className="flex items-start border border-gray-500  focus:outline-none focus:border-gray-900 rounded">
                <select 
                      name="month" 
                      id="month"
                      className="rounded-lg text-gray-900 py-2 px-2 pr-10 block tracking-wide w-full h-full place-self-auto outline-none border-none bg-white appearance-none"
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

                  <img src="public/img/down-arrow.svg" className="w-4 mx-auto my-auto pr-1" />
                </div>
              </div>
              <div className="px-2">
                <label className="block tracking-wide" htmlFor="day">Day</label>
                <input 
                  id="day"
                  className="w-full text-gray-900 py-2 px-2 border border-gray-500 placeholder-gray-600 rounded-lg text-xs focus:outline-none focus:border-gray-900"
                  type="text" 
                  placeholder="DD" 
                  onChange={(e) => setDay(e.target.value)}
                  />
              </div>
              <div>
                <label className="block tracking-wide" htmlFor="year">Year</label>
                <input 
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
            <span className="block font-extrabold text-xs my-2 tracking-wider">Who are you?</span>
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
                className="w-full p-2 uppercase text-sm font-bold text-white bg-emerald-600  rounded-full tracking-widest hover:bg-emerald-700 transform hover:scale-105 focus:scale-100 focus:bg-emerald-800 outline-none"
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
    </MainLayout>
  )
}
