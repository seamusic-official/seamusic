import React from 'react';

export function KitLinkLoading() {
	return (
		<div className="p-4 m-2 pr-36 flex transition hover:bg-gray-200 bg-gray-200 bg-opacity-5 hover:bg-opacity-10 rounded-lg">
			<div className="rounded-lg w-32 h-32 mr-2 animate-pulse rounded-full bg-opacity-10 bg-gray-300" />
			<div>
				<p className="w-48 h-4 rounded-md animate-pulse bg-gray-300 bg-opacity-10"></p>
				<p
					id="playlist-description"
					className="mt-1 h-4 rounded-md animate-pulse bg-gray-300 bg-opacity-10"></p>

				<p className="mt-4 w-48 h-8 rounded-md animate-pulse bg-gray-300 bg-opacity-10"></p>
			</div>
		</div>
	);
}
