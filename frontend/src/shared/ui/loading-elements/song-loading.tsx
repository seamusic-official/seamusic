import React from 'react';

export function SongLoading() {
	return (
		<tr className="flex cursor-pointer justify-around items-center text-gray-400 transition hover:bg-gray-200 bg-gray-200 bg-opacity-5 hover:bg-opacity-10 rounded-lg my-2 ">
			<td className="flex justify-start items-center">
				<div className="flex p-1">
					<div className="min-w-12 h-12 mr-1 animate-pulse bg-gray-300 bg-opacity-10 rounded-md" />
				</div>
				<div className="">
					<a>
						<p className="text-white w-12 h-4 rounded-md animate-pulse bg-gray-300 bg-opacity-10 truncate text-lg lg:w-56"></p>
					</a>
					<p className="mt-1 text-md font-semibold w-12 h-4 rounded-md animate-pulse bg-gray-300 bg-opacity-10 hover:text-white hover:cursor-pointer"></p>
				</div>
			</td>
			<td className="text-sm items-center w-12 h-4 rounded-md animate-pulse bg-gray-300 bg-opacity-10 font-semibold text-center"></td>
			<td className="text-sm items-center w-12 h-4 rounded-md animate-pulse bg-gray-300 bg-opacity-10 font-semibold text-center"></td>
			<td className="text-sm items-center w-12 h-4 rounded-md animate-pulse bg-gray-300 bg-opacity-10 font-semibold text-center"></td>
		</tr>
	);
}
