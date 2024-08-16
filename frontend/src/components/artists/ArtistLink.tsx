import { Link } from 'react-router-dom'

export default function ArtistLink(props) {
  return (
      <Link to={props.link}>
              <div className="p-2">
                <img src={props.image} alt={props.title} className="m-1 rounded-full w-32 h-32" />
                <p className="w-32 text-gray-300 flex justify-center items-center font-bold text-lg leading-tight truncate ">{props.title}</p>
              </div>
      </Link>
  )
}
