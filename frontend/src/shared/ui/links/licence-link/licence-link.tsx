import React from 'react';
import Link from 'next/link';
import { LicenseLinkType } from './type';

export function LicenseLink({
	link,
	image,
	title,
	price,
	description,
}: LicenseLinkType) {
	return (
		<Link href={link}>
			<div className="p-4 m-2 transition hover:bg-gray-200 bg-gray-200 bg-opacity-5 hover:bg-opacity-10 rounded-lg">
				<img src={image} alt={title} className="rounded-lg lg:w-48 w-36" />
				<div>
					<p className="lg:w-48 w-36 mt-2 text-gray-100 font-bold text-lg leading-tight whitespace-normal">
						{title}
					</p>
					<p className="lg:w-48 w-36 text-gray-200 font-medium text-md leading-tight whitespace-normal">
						{price}
					</p>
					<p
						id="playlist-description"
						className="text-white lg:w-48 w-36 mt-1 line-clamp-2 text-sm font-normal whitespace-normal opacity-70">
						{description}
					</p>
				</div>
			</div>
		</Link>
	);
}
