import { Link } from 'react-router-dom'

interface IPictureLink {
    link: string,
    image: string,
    title: string
}

export default function KitLink(props: IPictureLink) {
  return (
      <Link to={props.link}>
              <div className="p-4 m-2 pr-36 flex transition hover:bg-gray-200 bg-gray-200 bg-opacity-5 hover:bg-opacity-10 rounded-lg">
                <img src={props.image} alt={props.title} className="rounded-lg w-32 h-32 mr-2" />
                <div>
                  <p className="w-48 text-gray-200 font-semibold text-lg leading-tight whitespace-normal">{props.title}</p>
                  <p
                  id="playlist-description"
                  className="text-white mt-1 line-clamp-2 text-sm font-normal whitespace-normal opacity-70"
                >
                ☆ 100+ drum sound's (fav)
                ☆ 9 loop's made by me
                ☆ 300+ preset's for effectrix, looperator, mixer, portal, shaperbox 3, analog lab & thermal 
                </p>

                  <p className="w-48 text-gray-300 font-medium text-sm break-all truncate">@whyspacy x @axietic x @whiteprince</p>
                </div>
              </div>
      </Link>
  )
}
