import { Link } from "react-router-dom"
import { ISong } from "../interfaces"
import rsvg from "../assets/react.svg"

export const Song = (props: ISong) => {
    return (
            <tr
            className="flex justify-around items-center text-gray-400 m-2 hover:bg-gray-200 hover:bg-opacity-10 rounded-md py-2"
            key={props.id}
        >
            <td className="flex justify-start items-center">
            <div className="relative flex inline-block">
                <img
                    src={props.picture}
                    alt={props.name}
                    className="w-12 h-12 rounded-lg transition duration-300 filter brightness-100 hover:brightness-50"
                />
                <div className="absolute top-1/2 left-1/2 hidden transform -translate-x-1/2 -translate-y-1/2 group-hover:block">
                    <svg className="text-white w-12 h-12" fill="currentColor">
                        <use xlinkHref={rsvg} />
                    </svg>
                </div>
            </div>
            <div className="ml-3">
                <p className="text-white font-bold">{props.name}</p>
                <Link to="">
                    <a
                    className="text-xs font-semibold text-gray-400 hover:text-white hover:cursor-pointer"
                    ><span>{props.author}</span></a>
                </Link>
                
            </div>
            </td>
            <Link to="">
                <td className="text-sm items-center font-semibold text-center">{props.album}</td>
            </Link>
            <td className="text-sm items-center font-semibold text-center">{props.date}</td>
            <td className="text-sm items-center font-semibold text-center">2:05 minuts</td>
        </tr>
        )
}