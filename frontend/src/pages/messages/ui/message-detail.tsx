import { MainLayout } from '@/shared/layouts';
import Link from 'next/link';
import Image from 'next/image';
import { Input } from '@/shared/ui/input';
import { useAppSelector } from '@/shared/hooks/redux';
import { DefaultButton } from '@/shared/ui/buttons';
import { DecorText } from '@/shared/ui/decor-text';

export function MessagesDetail() {
	const user = useAppSelector((state) => state.auth.user);

	return (
			<div className="mt-2 ">
				<div className="flex items-center ">
					<div className="relative">
						<Image
							className="w-10 h-10 border-2 border-white rounded-full dark:border-gray-800"
							src=""
							alt=""
						/>
						<span className="bottom-0 left-7 absolute  w-3.5 h-3.5 bg-green-400 border-2 border-white dark:border-gray-800 rounded-full"></span>
					</div>
					<div className="p-2">
						<p className="font-semibold">xxxmanera</p>
						<p className="text-sm font-semibold text-gray-300">
							<DecorText>печатает..</DecorText>
						</p>
					</div>
					<DefaultButton className={'ml-2'} title="Profile" />
				</div>

				<div className="mt-4">
					<div className="left ">
						<div className="flex items-center ml-2 bg-zinc-800/30 dark:from-inherit border-neutral-900 border rounded-md bg-opacity-5 backdrop-blur-md w-1/2 ">
							<Image className="m-2 w-10 h-10 rounded-full" src="" alt="" />
							<div className="">
								<h1 className="text-md font-semibold">xxxmanera | 12:32</h1>
								<p className="text-gray-100 text-md font-normal">
									слушай братан может давай пойдем в телеграм отсюда ?)
								</p>
							</div>
						</div>
					</div>

					<div className="flex justify-end">
						<div className="flex items-center">
							<div className="m-2">
								<p className="flex text-lg font-bold justify-end">
									{user.username}
								</p>
								<p className="text-gray-300 flex text-md justify-end font-semibold">
									50$
								</p>
							</div>
							<Image
								className="w-8 h-8 border-2 border-white rounded-full dark:border-gray-800"
								src=""
								alt=""
							/>
						</div>
					</div>
				</div>
				<div className="">
					<Input placeholder="Write a message..">Send message</Input>
				</div>
			</div>
	);
}
