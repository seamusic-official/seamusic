import React from 'react';

export function PictureLinkLoading() {
	return (
		<div className="p-4">
			<div className="animate-pulse rounded-lg bg-opacity-10 bg-gray-300 w-32 h-32" />
			<p className="w-32 mt-1h-4 rounded-md animate-pulse bg-gray-300 bg-opacity-10"></p>
			<p className="w-32 mt-1 h-4 rounded-md animate-pulse bg-gray-300 bg-opacity-10"></p>
		</div>
	);
}
