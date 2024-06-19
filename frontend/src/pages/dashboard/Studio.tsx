import React, { useEffect, useRef, useState } from 'react'
import MainLayout from '../../components/layouts/MainLayout'
import { Song } from '../../components/Song'
import PostingBeatModal from '../../components/modals/beats/PostingBeatModal';
import BeatService from '../../services/BeatService';
import DefaultButton from '../../components/buttons/DefaultButton';
import { SongLoading } from '../../components/loadingElements/SongLoading';
import KitLinkLoading from '../../components/loadingElements/KitLinkLoading';

export default function Studio() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [beats, setBeats] = useState([])
  const [loading, setLoading] = useState(true)

  const openModal = () => {
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };


  useEffect(() => {
    const get_all_beats = async () => {
      try {
          const response = await BeatService.all();
          const responseData = response.data
          setBeats(responseData)
          setLoading(false)
          console.log("THIS IS RESPONSE", response);
        } catch(error){
          setLoading(false)
          console.error()
        }
      };

    get_all_beats()
  }, []);

  return (
    <MainLayout>
        <div className="p-2">
        <div className="flex mb-4 ">
          <div className="mr-2 ">
            <DefaultButton title="Upload beats" onClick={openModal}/>
          </div>
          <div className="mr-2 ">
            <DefaultButton title="Upload beatpacks" href="/beatpacks/add"/>
          </div>
          <div className="mr-2 ">
            <DefaultButton title="Publish sound kits" href="/kits/add"/>
          </div>
        </div>

        <PostingBeatModal isOpen={isModalOpen} onClose={closeModal} />
             <h2 className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter" id="playlist-title">
                Your beatpacks:
              </h2>
            <div className="flex overflow-auto justify-start items-center  m-1">
              <KitLinkLoading />
              <KitLinkLoading />
              <KitLinkLoading />
              <KitLinkLoading />
            </div>
          
            <h2 className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter" id="playlist-title">
                Your tracks:
              </h2>
          <table className="w-full">
                  <thead>
                    <tr
                      className="flex justify-around items-center text-gray-400 border-b border-gray-400 border-opacity-30 uppercase h-8"
                    >
                      <th className="text-md">
                        #<span className="text-xs ml-2">Picture</span>
                      </th>
                      <th className="text-md">
                        #<span className="text-xs ml-2">Title</span>
                      </th>
                      <th className="text-xs">Album</th>
                      <th className="text-xs">Date Added</th>
                      <th className="">
                        <svg
                          width="16"
                          height="16"
                          viewBox="0 0 16 16"
                          fill="none"
                        >
                          <path
                            d="M7.999 3H6.999V7V8H7.999H9.999V7H7.999V3ZM7.5 0C3.358 0 0 3.358 0 7.5C0 11.642 3.358 15 7.5 15C11.642 15 15 11.642 15 7.5C15 3.358 11.642 0 7.5 0ZM7.5 14C3.916 14 1 11.084 1 7.5C1 3.916 3.916 1 7.5 1C11.084 1 14 3.916 14 7.5C14 11.084 11.084 14 7.5 14Z"
                            fill="currentColor"
                          ></path>
                        </svg>
                      </th>
                      <th className="text-xs">
                        Action
                      </th>
                    </tr>
                  </thead>
                  <tbody>

          {!loading ? 
            (
              beats.map((beat) => (
                <Song 
                  id={beat.id}
                  name={beat.title} 
                  picture={beat.picture} 
                  author={beat.prod_by} 
                  src={beat.file_path} 
                  album="Каждый из дизайнеров" 
                  date={beat.created_at}
                  type={beat.type}
                  isAction={true}
                />
              ))
            ) 
            : (
              <>
                <SongLoading />
                <SongLoading />
                <SongLoading />
                <SongLoading />
                <SongLoading />
              </>
            )
          }
                            </tbody>
                </table>
        </div>
    </MainLayout>
  )
}
