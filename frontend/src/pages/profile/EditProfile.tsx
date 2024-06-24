import MainLayout from '../../components/layouts/MainLayout'
import dess from '../../assets/everydesigner.png'
import { Song } from '../../components/Song'
import { useAppSelector } from '../../hooks/redux'
import KitLink from '../../components/KitLink';
import AddButtonPlus from '../../components/icons/AddButtonPlus';
import DefaultButton from '../../components/buttons/DefaultButton';
import { useEffect, useState } from 'react';
import BeatService from '../../services/BeatService';
import { SongLoading } from '../../components/loadingElements/SongLoading';
import Input from '../../components/Input';
import SubmitButton from '../../components/buttons/SubmitButton';


export default function EditProfile() {
  const user = useAppSelector((state) => state.auth.user);
  const [file, setFile] = useState(null); 
  const [picture, setPicture] = useState(null);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [co_prod, setCo_prod] = useState('');
  const [prod_by, setProd_by] = useState('');

  const [beatId, setBeatId] = useState<number>(0);

  const handlePictureChange = async (event) => {
    const picture = event.target.files[0];
    setPicture(picture);

    const formData = new FormData();
    formData.append('file', picture);

    try {
        const response = await BeatService.update_picture(beatId, formData);
        console.log(response.data);
    } catch (error) {
        console.error('Error sending data:', error);
    }
};

  const handleFileChange = async (event) => {
      const file = event.target.files[0];
      setFile(file);

      const formData = new FormData();
      formData.append('file', file);

      try {
          const response = await BeatService.add(formData);
          setBeatId(response.data.id);
          console.log(response.data);
      } catch (error) {
          console.error('Error sending data:', error);
      }
  };
  
  const submitForm = async (event) => {
    event.preventDefault();
  
    try {
      const beats_data = {
        title: title,
        description: description,
        co_prod: co_prod,
        prod_by: prod_by,
      };

      console.log(beats_data);

      const response = await BeatService.update(beatId, beats_data);
      console.log(response.data);
      navigate("/dashboard")
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
                {user.description}
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
                                <div className="m-1">
                                  <label htmlFor="id" className="inline-block  font-extrabold text-sm my-1 tracking-wider ">
                                  <span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>*</span>
                                    Your nickname
                                  </label>
                                    <Input
                                        value={user.username}
                                        id="title"
                                        type="text"
                                        placeholder="title 153bpm F#"
                                        onChange={(e) => setTitle(e.target.value)}
                                        buttonText=""
                                    />
                                </div>
                                
                                <div className="m-1">
                                <label htmlFor="id" className="inline-block  font-extrabold text-sm my-1 tracking-wider ">
                                <span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>*</span>
                                Who's prod. it?
                                </label>
                                    <Input  
                                        id="prod_by"
                                        type="text"
                                        placeholder="f1lty"
                                        value={prod_by}
                                        onChange={(e) => setProd_by(e.target.value)}
                                        buttonText=""
                                    />
                                </div>

                                <div className="m-1">
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
                                </div>
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
                                      multiple
                                      onChange={handlePictureChange}
                                      className="opacity-0 cursor-pointer w-full"
                                      />                      
                                  </div>
                                </div>
                                <div className='m-1 my-2'>
                                  <SubmitButton title="Publish" />
                                </div>
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
