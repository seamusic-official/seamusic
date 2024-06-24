import React from 'react'


export default function Input({ children, props, placeholder, onChange, type}) {
  // const handleSubmit = (event) => {
  //   event.preventDefault();
  // };


  return (
    <div className="">
          <div className="relative w-full">
              <input 
                    {...props}
                    type={type}
                    placeholder={placeholder}
                    onChange={onChange}
                    className="tracking-tighter block p-2.5 w-full text-sm rounded-md font-bold  border-neutral-800 rounded-s-2 border bg-zinc-800/30 placeholder-neutral-700 text-white"
                    required 
                    />
              <button type="submit" className="tracking-tighter shadow font-bold absolute top-0 end-0 p-2.5 h-full text-sm text-white bg-emerald-700 rounded-e-md hover:bg-emerald-900 focus:ring-4 focus:ring-emerald-300 focus:ring-emerald-800">
                {children}
              </button>
          </div>
    </div>
  )
}
