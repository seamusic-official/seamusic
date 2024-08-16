import React from 'react'
import { Link } from 'react-router-dom'

export default function DefaultButton({ title, href, onClick, className }) {
  return (
    <div className={className}>
        <Link
          className="p-2.5 border border-zinc-800/30 hover:border-emerald-800 transition cursor-pointer font-bold rounded-lg from-zinc-200 backdrop-blur-2xl bg-zinc-800/30 from-inherit" 
          to={href}
          onClick={onClick}
        >
            {title}
        </Link>
    </div>
  )
}
