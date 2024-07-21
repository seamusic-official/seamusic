import Link from 'next/link';
import { PictureLinkType } from './type';

export function PictureLink({ link, image, title, artist }: PictureLinkType) {
	return (
		<Link href={link}>
			<div className="p-4">
				<img src={image} alt={title} className="rounded-lg w-32 h-32" />
				<p className="w-32 text-gray-300 font-bold text-lg leading-tight truncate ">
					{title}
				</p>
				<p className="w-32 text-gray-300 font-semibold text-sm break-all">
					{artist}
				</p>
			</div>
		</Link>
	);
}
