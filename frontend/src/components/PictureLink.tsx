import { Link } from 'react-router-dom'

interface IPictureLink {
    link: string,
    image: string,
    title: string
}

export default function PictureLink(props: IPictureLink) {
  return (
      <Link to={props.link}>
              <div className="p-4">
                <img src={props.image} alt={props.title} className="rounded-lg w-32 h-32" />
                <p className="w-32 text-gray-300 font-bold text-lg leading-tight truncate ">{props.title}</p>
                <p className="w-32 text-gray-300 font-semibold text-sm break-all">{props.artist}</p>
              </div>
      </Link>
  )
}
