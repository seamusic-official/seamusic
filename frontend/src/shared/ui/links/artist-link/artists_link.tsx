import Link from 'next/link';
import Image from 'next/image';
import { ArtistLinkType } from './type';

export function ArtistLink({ link, image, title }: ArtistLinkType) {
	return (
		<Link href={link}>
			<div className="p-2">
				<Image src={image} alt={title} className="m-1 rounded-full w-32 h-32" />
				<p className="w-32 text-gray-300 flex justify-center items-center font-bold text-lg leading-tight truncate ">
					{title}
				</p>
			</div>
		</Link>
	);
}
