import React, { useRef, useState } from 'react';
import Input from '../../inputs/Input';
import SubmitButton from '../../buttons/SubmitButton';
import { Song } from '../../songs/Song';
import $api from '../../../http';
import { useAppSelector } from '../../../hooks/redux';
import axios from 'axios'
import BeatService from '../../../services/BeatService';
import { useNavigate } from 'react-router-dom';

const PostingBeatModal = ({ isOpen, onClose }) => {
  const [file, setFile] = useState(null); 
  const [picture, setPicture] = useState(null);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [co_prod, setCo_prod] = useState('');
  const [prod_by, setProd_by] = useState('');
  const navigate = useNavigate()
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
      const response = await BeatService.update(beatId, {
        title: title,
        description: description,
        co_prod: co_prod,
        prod_by: prod_by,
      });

      console.log(response.data);
      navigate("/profile");
    } catch (error) {
      console.error('Ошибка при отправке данных:', error);
    }
  };

  return (
    <>
      {isOpen && (
        <div className="fixed z-10 inset-0 overflow-y-auto">
          <div className="flex border-neutral-800 items-center rouded-lg justify-center min-h-screen pt-2 px-2 pb-20 text-center sm:block sm:p-0">
            <div className="fixed inset-0 transition-opacity">
              <div
                className="absolute backdrop-filter backdrop-blur inset-0 bg-black opacity-75"
                onClick={onClose}
              ></div>
            </div>

            {/* Содержимое модального окна */}
            <div
              className="inline-block border-neutral-800 align-bottom bg-black  text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full"
              role="dialog"
              aria-modal="true"
              aria-labelledby="modal-headline"
            >
              <div className="border-neutral-800 border rounded-lg dark:bg-zinc-800/30 px-2 pt-5 pb-4 sm:p-6 sm:pb-4">
                <div className="sm:flex sm:items-start">
                  <div className="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                  <button onClick={() => setFile(null)} className={`text-white ${!file ? "hidden" : ""}`}>
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
                    <div className="flex flex-wrap justify-center lg:justify-between max-w-max mx-auto ">
                      <form onSubmit={submitForm} method="POST" encType="miltipart/form-data">
                        <div className={`m-6 relative border border-dashed border-gray-400 p-12 ${ !file ? "" : "hidden"}`}>
                            <img alt="Upload Icon" className="mx-auto w-12 mb-2 invert"  src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAACXBIWXMAAAsTAAALEwEAmpwYAAAE90lEQVR4nO2cXYzdQxTAf92liFXUZyhFwiJBhCZeZMULLfXQ0qRNSJTS6KPgQcQKD42kQZcH9UA0jY8obzwgUQ0Sqk2Jb6HtIlIlEQ0WvSOTnE1uNnfmf+/c/38+9p5fct7unTlzznycOTPzB0VRFEVRFEVRFEVRFEVRFEVRFEVRFEVRBpqFwK3AY8BbwLfAfuBv4D/gN+B74B3gGWAtcAkwJ7XiJXMm8DDwKWACZRJ4CliUujElcTnwqvRsU6N8DNwIDKVuYK6cDbwAtGo2/EzZCYylbmxu3AL80bDhZ8rzwDEMOMcDr0c2fLvYxfxiBpRzga+6NJRdD7YBDwHLgQuAk4EjgGFx5IXAUuBRme8PdVn2QeAGBoxLgV+7MM5nwJ3ACQF12P+sk15eVc+/wM0MCHbIH6gwyJfSm+uI423Us6yLcNaOspuYRSyQHvgG8IUMdWv43z1GmALuBQ5vQJ+5wCPS2331X0nhnAZsqmhoJ/ku0obpMmCPR4+fgdMplOsrerhLdgGnRB6dn3v0ebvENMZdgbvXj4BjE+h7kkRLLr1se4rh2kDj/yC9MRV21P3o0M0m+E6kkDk/ZNr5UzKWqRnzrFdPUACbKoy8QRbXo2XDdAVwD7CCfLjfo/+pZMwCT+/ZI7vTEjjSExnZ0DVb1nl6TinGb08IdmqLXSMOI1NciTQ77ZTGkKQ+OrXnTVkP7gAuIiNcybRST6Du6zKAsNPVeuCs1Aq7cvh2wS31GLTVQyRn17+nU4SrNtP4okexeZTL+wEh9X65NBAFG0b+VKFQVvNkjzwY4IBpeVaSfo2xXCKcKkVsKrlUru7DAUYCExvW1s7SLjKcXwN3A8cRh3GROpkrIfQ5cupm17NR4BpgI7C3Cye8Uvfti0UVPd+mkldFvvIx3lZ/3U7wMSzz/WSFEx6oq0J7c+AbT0VbEiy64x30iOkEywiwtSJCsnec+uZJTyUbEuTNxz36xHbCHLGBS58P+rXPecA/jsJtGEpGxjcidoMUE2vglzz6XNdP4c85Ct0rQzA345uE09Gk53QteO4/6Ch0Jfka3yRywmqHHodCD51WOgrcJ5FAzsY3iaKjfQ49bq9z8V1fiPFNAidMeO6h9syHjsKWUI7xTWQnLHbUvyOkMNeicgZlGd9EdMKoo+5fQgr7y1HYUZRnfBNp+hxx1GufUvXMlKOw2OFnJ1wGTs28Oh3gukBrN2epMZk6YNRzXtAzOx2F2UtYqTGZOmBJnYvwFkdhNiWbGpOpA1xh6OaQwtZ60hAxN2KlOMC3EVsT+mrRdUAd7fyzIAfc5tCpJYf9QbzrKHQycTRkMnPAiFw07qSTfb0fzApPY19L+OjZZOQAm45+2aOTfR4VzFDF26oUBzI5OaDqQGZ3HZ10rOKy0tYE05HJwAEj8kkFly6tOt+bbfRUNL0mrI4YHZmEDhiWBdc150/L43VWah9Ev1dRoZEwbEKyguc3ODJMRAeMSFsWS4reFWq2y/YmLmjN7/PTMSHioq7fNyGfiK0aYX7g3clBccD2Jo3fPh1NRPisjAkwaK+/r0taMuc3ei90JldFmJJKcMDulK/rh+QrVNsaGhG5OqAlO9xlOX2Ba6E84dks6dcDnkOdkhwwJUeKO6Rta/rJ7cwWTI8OUNQBswujI0AdMNAYHQHqAEVRFEVRFEVRFEVRFEVRFEWhEP4HJLF96pRWp/4AAAAASUVORK5CYII="></img>
                            <input
                              type="file"
                              name="file"
                              onChange={handleFileChange}
                              className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
                            />
                            <div className="mb-2">
                              <label htmlFor="file" className="flex justify-center text-center block inline-block font-extrabold text-lg tracking-wider">Select or drug file here</label>
                              <span className="text-center block text-gray-600">*.wav, .mp3, .ogg, .aac</span>
                            </div>
                         </div>
                      </form>
                      <form onSubmit={submitForm} method="POST" encType="miltipart/form-data">
                            <div  className={`ml-4 mr-8 w-full ${ !file ? "hidden" : ""} `}>
                                <div className="m-1">
                                  <label htmlFor="id" className="inline-block  font-extrabold text-sm my-1 tracking-wider ">
                                  <span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'>*</span>
                                    Title of beat (name, bpm, key)
                                  </label>
                                    <Input
                                        id="title"
                                        type="text"
                                        placeholder="title 153bpm F#"
                                        value={title}
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
                                <label htmlFor="co_prod" className="inline-block  font-extrabold text-sm my-1 tracking-wider ">
                                <span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'></span>
                                Co-prods
                                </label>
                                    <Input  
                                        id="co_prod"
                                        type="text"
                                        placeholder="Co-prod"
                                        value={co_prod}
                                        onChange={(e) => setCo_prod(e.target.value)}
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
                                  Picture 
                                  
                                </label>
                                  <div className="tracking-tighter block p-2.5 z-20 text-sm rounded-md font-bold  border-neutral-800 rounded-s-2 border bg-zinc-800/30 placeholder-neutral-700 text-white">
                                    <input
                                      type="file"
                                      name="picture"
                                      onChange={handlePictureChange}
                                      className="opacity-0 cursor-pointer w-full"
                                    />                      
                                  </div>
                                </div>
                                <label htmlFor="descritpion" className="inline-block  font-extrabold text-sm my-1 tracking-wider ">
                                  <span className='mr-1 bg-clip-text text-transparent bg-gradient-to-r from-emerald-800 to-emerald-500'></span>
                                  Preview 
                                </label>
                                <div className="p-1 mb-2">
                                  <Song name={title} author={`prod by ${prod_by}`} link="nah" picture={picture} isActive={false} />
                                </div>
                                <div className='m-1 my-2'>
                                  <SubmitButton title="Publish" />
                                </div>
                            </div>
                          </form>
                    </div>
                  </div>
                  <button
                    onClick={onClose}
                    type="button"
                    className="p-2 "
                    >
                    {/* Кнопка закрытия модального окна */}
                    <svg className='hover:bg-gray-800 rounded-full'
                     xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <line x1="18" y1="6" x2="6" y2="18"></line>
                                <line x1="6" y1="6" x2="18" y2="18"></line>
                                </svg>

                    </button>

                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default PostingBeatModal;