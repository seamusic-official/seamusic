import React from 'react';
import Link from 'next/link';
import { MessagePreviewType } from './type';

export function MessagePreview({
	username,
	message,
	image_url,
	href,
}: MessagePreviewType) {
	return (
		<Link href={href}>
			<div className="flex items-center transition hover:bg-gray-200 bg-gray-200 bg-opacity-5 hover:bg-opacity-10 rounded-lg m-2 pl-2 cursor-pointer">
				<div className="relative">
					<img
						className="w-10 h-10 rounded-full dark:border-gray-800"
						src={image_url}
						alt=""
					/>
					<span className="bottom-0 left-7 absolute  w-3 h-3 bg-green-400 rounded-full"></span>
				</div>
				<div className="p-1 pl-2">
					<p className="font-semibold">{username}</p>
					<p className="text-sm font-semibold text-gray-300">{message}</p>
				</div>
			</div>
		</Link>
	);
}
