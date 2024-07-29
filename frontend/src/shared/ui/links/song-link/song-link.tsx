import Link from 'next/link';
import { SongLinkType } from './type';

export function SongLink({ link, image, title }: SongLinkType) {
	return (
		<Link href={link}>
			<div className="">
				<img src={image} alt={title} className="rounded-lg w-24 h-24" />
				<p className="w-24 text-gray-300 font-bold text-lg leading-tight truncate">
					{title}
				</p>
			</div>
		</Link>
	);
}
