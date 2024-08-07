import React from 'react';

export function ArtistLinkLoading() {
	return (
		<div className="p-2 ">
			<div className="m-1 animate-pulse rounded-full bg-opacity-10 bg-gray-300 w-32 h-32"></div>
			<p className="w-32 flex justify-center h-4 rounded-md animate-pulse bg-gray-300 bg-opacity-10"></p>
		</div>
	);
}
