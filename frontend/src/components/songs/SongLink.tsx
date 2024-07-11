import { Link } from 'react-router-dom'

interface IPictureLink {
    link: string,
    image: string,
    title: string
}

export default function SongLink(props: IPictureLink) {
  return (
      <Link to={props.link}>
              <div className="">
                <img src={props.image} alt={props.title} className="rounded-lg w-24 h-24" />
                <p className="w-24 text-gray-300 font-bold text-lg leading-tight truncate">{props.title}</p>
              </div>
      </Link>
  )
}
