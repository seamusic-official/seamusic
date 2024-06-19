import React from 'react'


export default function Input({ type, placeholder, value, onChange, buttonText, id, props }) {
  // const handleSubmit = (event) => {
  //   event.preventDefault();
  // };


  return (
    <div className="bottom-36">
          <div className=" relative w-full">
              <input 
                    {...props}
                    type={type} 
                    id={id} 
                    className="tracking-tighter block p-2.5 w-full text-sm rounded-md font-bold  border-neutral-800 rounded-s-2 border bg-zinc-800/30 placeholder-neutral-700 text-white"
                    placeholder={placeholder} 
                    required 
                    value={value}
                    onChange={onChange}
                    />
              <button type="submit" className="tracking-tighter shadow font-bold absolute top-0 end-0 p-2.5 h-full text-sm text-white bg-emerald-700 rounded-e-md hover:bg-emerald-900 focus:ring-4 focus:ring-emerald-300 focus:ring-emerald-800">
                {buttonText}
              </button>
          </div>
    </div>
  )
}
