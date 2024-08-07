import React from 'react';
import Image from 'next/image';
import { Input } from '../input';
import { useAppSelector } from '@/shared/hooks/redux';

export default function Comments() {
	const user = useAppSelector((state) => state.auth);

	return (
		<div className="mt-4">
			<Input placeholder="Write a comment">Send</Input>

			<div className="left mt-4">
				<div className="flex items-center bg-zinc-800/30 dark:from-inherit border-neutral-900 border rounded-md bg-opacity-5 backdrop-blur-md w-2/3 ">
					<Image
						className="m-2 w-10 h-10 rounded-full"
						src={user.user.picture_url}
						alt=""
					/>
					<div className="">
						<h1 className="text-md font-semibold">xxxmanera | 12:32</h1>
						<p className="text-gray-100 text-md font-normal">
							слушай братан может давай пойдем в телеграм отсюда?)
						</p>
					</div>
				</div>
			</div>
		</div>
	);
}
