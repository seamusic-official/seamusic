import { ISong } from "../interfaces"


export const Song = (props: ISong) => {
    return (
            <tr
            className="flex justify-around items-center text-gray-400 m-2 hover:bg-gray-200 hover:bg-opacity-10 rounded-md py-2"
            key={props.id}
        >
            <td className="flex justify-start items-center">
            
            <img
                src={props.picture}
                alt={props.name}
                height="50px"
                width="50px"
                className="rounded-lg"
            />
            <div className="ml-3">
                <p className="text-white font-bold">{props.name}</p>
                <a
                className="text-xs font-semibold text-gray-400 hover:text-white hover:cursor-pointer"
                ><span>{props.author}</span></a>
                
            </div>
            </td>
            <td className="text-sm items-center font-semibold text-center">{props.album}</td>
            <td className="text-sm items-center font-semibold text-center">{props.date}</td>
            <td className="text-sm items-center font-semibold text-center">2:05 minuts</td>
        </tr>
        )
}