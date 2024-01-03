import React from 'react'
import MainLayout from '../../components/layouts/MainLayout'
import des from '../../assets/everydesigner.png'
import { Song } from '../../components/Song'

export default function Studio() {
  return (
    <MainLayout>
        <div className="p-2">
          <h1 className="text-gray-200 font-bold text-xl leading-tight ">Your albums: </h1>
          <div className="flex justify-start items-center">
            <div className="p-4">
              <img src={des} alt="" className="rounded-lg w-32 h-32" />
              <p className="w-32 text-gray-300 font-bold text-lg leading-tight truncate ">Съешь еще этих мягких французских булок</p>
              <p className="w-32 text-gray-300 font-semibold text-sm break-all">Listens: 2 234 543 453</p>
            </div>
            <div className="p-4">
              <img src={des} alt="" className="rounded-lg w-32 h-32" />
              <p className="w-32 text-gray-300 font-bold text-lg leading-tight truncate ">Nevermind</p>
              <p className="w-32 text-gray-300 font-semibold text-sm break-all">Listens: 2 234 543 453</p>
            </div>
            <div className="p-4">
              <img src={des} alt="" className="rounded-lg w-32 h-32" />
              <p className="w-32 text-gray-300 font-bold text-lg leading-tight truncate ">In utero</p>
              <p className="w-32 text-gray-300 font-semibold text-sm break-all">Listens: 2 234 543 453</p>
            </div>
          </div>
          
          <h1 className="text-gray-200 font-bold text-xl leading-tight ">Your tracks: </h1>
          <Song name="Каждый из дизайнеров" picture={des} author="xxxmanera" album="Каждый из дизайнеров" date="02.01.2023"/>
          <Song name="Каждый из дизайнеров" picture={des} author="xxxmanera" album="Каждый из дизайнеров" date="02.01.2023"/>
          <Song name="Каждый из дизайнеров" picture={des} author="xxxmanera" album="Каждый из дизайнеров" date="02.01.2023"/>
 
        </div>
    </MainLayout>
  )
}
