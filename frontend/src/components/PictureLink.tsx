import { Link } from 'react-router-dom'

interface IPictureLink {
    link: string,
    image: string,
    title: string
}

export default function PictureLink(props: IPictureLink) {
  return (
            <Link to={props.link}>
                <img src={props.image} alt={props.title} className="border-lg h-24 w-24 " />
                <p className="font-semibold mt-2">{props.title}</p>
            </Link>
  )
}
