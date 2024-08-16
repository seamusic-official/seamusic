import React from 'react'

export default function SubmitButton({ title }) {
  return (
    <div>
        <button 
          className="p-2 border-emerald-600 border hover:border-emerald-800  font-bold rounded-xl from-zinc-200 backdrop-blur-2xl border-neutral-900 bg-zinc-800/30 from-inherit" 
          type="submit"
        >
            {title}
        </button>
    </div>
  )
}
