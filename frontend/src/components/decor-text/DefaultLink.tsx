import React from 'react'
import { Link } from 'react-router-dom'

export default function DefaultLink({children, props}) {
  return (
    <Link to={props.link}><span className="hover:text-emerald-600">{children}</span></Link>
  )
}
