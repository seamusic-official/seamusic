import MainLayout from '../../components/layouts/MainLayout'
import dess from '../../assets/everydesigner.png'
import { Song } from '../../components/songs/Song'
import { useAppDispatch, useAppSelector } from '../../hooks/redux'
import KitLink from '../../components/kits/KitLink';
import AddButtonPlus from '../../components/icons/AddButtonPlus';
import DefaultButton from '../../components/buttons/DefaultButton';
import { useEffect, useState } from 'react';
import BeatService from '../../services/BeatService';
import { SongLoading } from '../../components/loadingElements/SongLoading';
import Input from '../../components/inputs/Input';
import SubmitButton from '../../components/buttons/SubmitButton';
import { useNavigate } from 'react-router-dom';
import { setAuthData, updateAuthData } from '../../store/reducers/authSlice';
import AuthService from '../../services/AuthService';


export default function EditProfile() {
  const user = useAppSelector((state) => state.auth.user);
  const dispatch = useAppDispatch();
  const navigate = useNavigate()
  const [picture, setPicture] = useState(null);
  const [username, setUsername] = useState('');

  const userId = user.id

  const handlePictureChange = async (event) => {
    const picture = event.target.files[0];
    setPicture(picture);

    const formData = new FormData();
    formData.append('file', picture);

    try {
        const response = await AuthService.update_user_picture(userId, formData);
        const update_data = await AuthService.get_user(userId);
        console.log(response.data);
        user_data = {
          
        }
        dispatch(updateAuthData(update_data))
    } catch (error) {
        console.error('Error sending data:', error);
    }
};

  
  const submitForm = async (event) => {
    event.preventDefault();
    try {
      const response = await AuthService.update_user(userId, {
        username: username,
      });

      console.log(response.data);
      navigate("/profile")
      dispatch(updateAuthData(response.data))
    } catch (error) {
      console.error('Ошибка при отправке данных:', error);
    }
  };

  return (
    <MainLayout>
           <div className="">
            <div className=" mt-2 flex items-center md:flex flex-wrap">
              <div className="md:relative flex items-center justify-center">      
                <div className="mx-auto ">
                    <img
                        id="playlist-thumbnail"
                        src={user.picture_url}
                        alt="alan walker artist"
                        className="mx-auto w-56 h-56 md:mr-6 rounded-full border border-neutral-600"
                    />
                    <span className="absolute top-[190px] ml-[175px] w-6 border-2 border-neutral-600 h-6 bg-emerald-500 border-white dark:border-gray-800 rounded-full"></span>
                </div>        
            </div>

              <div className="mt-16">
                <h2
                  className="text-gray-50 uppercase text-xs font-semibold tracking-tighter mt-1"
                >
                  {user.role}
                </h2>
                <span
                  className="text-white text-6xl tracking-tighter font-extrabold"
                  ><h1 id="playlist-title">{user.username}</h1></span>
                <div className="mr-1 mb-4 mt-4">
                    <a className="p-2 m-1 font-semibold rounded-xl from-zinc-200 backdrop-blur-2xl border-neutral-900 bg-zinc-800/30 from-inherit" href="">
                    Opium
                    </a>
                </div>
                <p
                  id="playlist-description"
                  className="text-white mt-6 text-sm font-normal leading-none opacity-70"
                >
                
                </p>

                <div className="flex items-center mt-2">
                <a
                    className="flex text-white font-bold text-sm hover:text-underline cursor-pointer"
                    >
                    <img className="mr-1 w-5 invert" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAfElEQVR4nO2TSwqAIBRFz8hFRRuIFpZtMz/QKmxiQdDHpzYIPPDAwb3e51OhUcgIWCAklAEGaYBJ3HyvRRoQMqoF8MmIuhddXxqQQgv4yYgUMAMeWF9MEu2BFrxtnfMPvMDkcwLchcFW0D4ee6qgPV2cjt25uFYVtA1u2QBivZ8j3cMZWwAAAABJRU5ErkJggg==" />
                    Listen a voice tag</a>
                  
                  <div
                    className="font-extrabold text-md text-white opacity-70 mx-1 mb-1 pb-1"
                  >
                    .
                  </div>
                  <p className="text-white opacity-70 font-normal text-sm">
                    1,308,405 likes
                  </p>
                  <div
                    className="font-extrabold text-md text-white opacity-70 mx-1 mb-1 pb-1"
                  >
                    .
                  </div>
                  <p className="text-white opacity-70 font-normal text-sm mr-1">
                    50 songs,
                  </p>
                  <p className="text-white opacity-70 font-normal text-sm">
                    2hr 36 min
                  </p>
                </div>


              </div>
            </div>
          </div>
          <div className="w-full " >
            <div
              className="w-full p-4"
            >

              <div
                className="flex items-center text-white mx-4 my-2"
              >
                <div  className={` w-full `}>
                  <form onSubmit={submitForm} encType="multipart/form-data">
                                <div className="m-1">
                                  <label htmlFor="id" className="inline-block  font-extrabold text-sm my-1 tracking-wider ">
                                  <span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>*</span>
                                    Your nickname
                                  </label>
                                    <Input
                                        id="title"
                                        type="text"
                                        placeholder={user.username}
                                        onChange={(e) => setUsername(e.target.value)}
                                        buttonText=""
                                    />
                                </div>
                                

                                {/* <div className="m-1">
                                <label htmlFor="descritpion" className="inline-block  font-extrabold text-sm my-1 tracking-wider ">
                                <span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'></span>
                                Description
                                </label>
                                    <Input
                                        id="descritpion"
                                        type="text"
                                        placeholder="Description"
                                        value={description}
                                        onChange={(e) => setDescription(e.target.value)}
                                        buttonText=""
                                    />
                                </div> */}
                                <div className="m-1">
                                <label htmlFor="descritpion" className="inline-block  font-extrabold text-sm my-1 tracking-wider ">
                                  <span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'></span>
                                  Profile picture 
                                  
                                </label>
                                  <div className="tracking-tighter block p-2.5 z-20 text-sm rounded-md font-bold  border-neutral-800 rounded-s-2 border bg-zinc-800/30 placeholder-neutral-700 text-white">
                                    <input
                                      id="picture"
                                      type="file"
                                      name="file"
                                      onChange={handlePictureChange}
                                      className="opacity-0 cursor-pointer w-full"
                                      />                      
                                  </div>
                                </div>
                                <div className='m-1 my-2'>
                                  <SubmitButton title="Publish" />
                                </div>
                        </form>
                      </div>
            </div>
            <div >
            <h1 className="flex items-center text-white font-extrabold text-2xl mt-6">
                {user.username}'s kits <AddButtonPlus link="/dashboard"/>
            </h1>
                <div className="flex overflow-auto justify-start items-center mb-4">
                    <div>
                      <KitLink link="/kit/newera" image={dess} title="✕  RIOT UNIVERSE COMMUNITY STASH KIT 2024  ✕ "/>
                    </div>
                    <div>
                      <KitLink link="/kit/newera" image={dess} title="21' happy birthday stash kit "/>
                    </div>
                </div>
            </div>
            </div>
          </div>
    </MainLayout>
  )
}
