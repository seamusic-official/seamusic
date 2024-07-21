import Link from 'next/link';
import des from '@/shared/assets/everydesigner.png';
import { DecorText } from '@/shared/ui/decor-text';

export function Sidebar() {
	return (
		<div className="border-r px-6 hidden md:w-1/5 md:block px-6 py-4 h-full fixed backdrop-blur-lg left-0 border-neutral-800 lg:p-2 bg-gray-200 bg-opacity-5">
			<div className="text-gray-100 my-2 cursor-pointer">
				<h2
					className="flex items-center mt-1 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter"
					id="">
					<div className="p-2 rounded-full w-8 h-8 mr-2 animate-pulse rounded-full bg-opacity-10 bg-gray-300" />
					<Link href="/">SeaMusic</Link>
				</h2>
			</div>
			<div className="p-2 rounded-lg w-full h-24 mr-2 animate-pulse rounded-full bg-opacity-10 bg-gray-300" />
			<button className="text-white hover:text-white flex items-center mt-4">
				<svg
					className="mr-4"
					viewBox="0 0 512 512"
					width="24"
					height="24"
					xmlns="http://www.w3.org/2000/svg">
					<path
						d="M 256.274 60.84 L 84.324 166.237 L 84.324 443.063 L 193.27 443.063 L 193.27 293.73 L 320.228 293.73 L 320.228 443.063 L 428.222 443.063 L 428.222 165.476 L 256.274 60.84 Z M 256.274 35.95 L 448.452 149.145 L 448.452 464.395 L 300 464.395 L 300 315.062 L 213.499 315.062 L 213.499 464.395 L 64.095 464.395 L 64.095 150.161 L 256.274 35.95 Z"
						fill="currentColor"></path>
				</svg>
				<Link href="/home">
					<h2 className="text-white text-md font-bold hover:text-white capitalize">
						Home
					</h2>
				</Link>
			</button>
			<button className="text-white hover:text-white flex items-center mt-4">
				<svg
					className="mr-4"
					viewBox="0 0 512 512"
					width="24"
					height="24"
					xmlns="http://www.w3.org/2000/svg">
					<path
						d="M349.714 347.937l93.714 109.969-16.254 13.969-93.969-109.969q-48.508 36.825-109.207 36.825-36.826 0-70.476-14.349t-57.905-38.603-38.603-57.905-14.349-70.476 14.349-70.476 38.603-57.905 57.905-38.603 70.476-14.349 70.476 14.349 57.905 38.603 38.603 57.905 14.349 70.476q0 37.841-14.73 71.619t-40.889 58.921zM224 377.397q43.428 0 80.254-21.461t58.286-58.286 21.461-80.254-21.461-80.254-58.286-58.285-80.254-21.46-80.254 21.46-58.285 58.285-21.46 80.254 21.46 80.254 58.285 58.286 80.254 21.461z"
						fill="currentColor"
						fillRule="evenodd"></path>
				</svg>
				<Link href="/search">
					<h2 className="text-white text-md font-bold hover:text-white capitalize">
						Search
					</h2>
				</Link>
			</button>
			<button className="text-white hover:text-white flex items-center mt-4">
				<svg
					className="mr-4"
					viewBox="0 0 512 512"
					width="24"
					height="24"
					xmlns="http://www.w3.org/2000/svg">
					<path
						d="M291.301 81.778l166.349 373.587-19.301 8.635-166.349-373.587zM64 463.746v-384h21.334v384h-21.334zM192 463.746v-384h21.334v384h-21.334z"
						fill="currentColor"></path>
				</svg>
				<Link href="/messages">
					<h2 className="text-white text-md font-bold hover:text-white capitalize">
						Messages
					</h2>
				</Link>
			</button>
			<button className="text-white hover:text-white flex items-center mt-4">
				<svg
					className="mr-4"
					viewBox="0 0 512 512"
					width="24"
					height="24"
					xmlns="http://www.w3.org/2000/svg">
					<path
						d="M291.301 81.778l166.349 373.587-19.301 8.635-166.349-373.587zM64 463.746v-384h21.334v384h-21.334zM192 463.746v-384h21.334v384h-21.334z"
						fill="currentColor"></path>
				</svg>
				<Link href="/dashboard">
					<h2 className="text-white text-md font-bold hover:text-white capitalize">
						Dashboard
					</h2>
				</Link>
			</button>
			<div className="border-t mt-4 border-neutral-800">
				<button className="text-white hover:text-white flex items-center mt-4">
					<svg
						className="mr-4"
						viewBox="0 0 512 512"
						width="24"
						height="24"
						xmlns="http://www.w3.org/2000/svg">
						<path
							d="M291.301 81.778l166.349 373.587-19.301 8.635-166.349-373.587zM64 463.746v-384h21.334v384h-21.334zM192 463.746v-384h21.334v384h-21.334z"
							fill="currentColor"></path>
					</svg>
					<Link href="/squads">
						<h2 className="text-white text-md font-bold hover:text-white capitalize">
							Squads
						</h2>
					</Link>
				</button>
				<button className="text-white hover:text-white flex items-center mt-4">
					<svg
						className="mr-4"
						viewBox="0 0 512 512"
						width="24"
						height="24"
						xmlns="http://www.w3.org/2000/svg">
						<path
							d="M291.301 81.778l166.349 373.587-19.301 8.635-166.349-373.587zM64 463.746v-384h21.334v384h-21.334zM192 463.746v-384h21.334v384h-21.334z"
							fill="currentColor"></path>
					</svg>
					<Link href="/dashboard">
						<h2 className="text-white text-md font-bold hover:text-white capitalize">
							Beats
						</h2>
					</Link>
				</button>
				<button className="text-white hover:text-white flex items-center mt-4">
					<svg
						className="mr-4"
						viewBox="0 0 512 512"
						width="24"
						height="24"
						xmlns="http://www.w3.org/2000/svg">
						<path
							d="M291.301 81.778l166.349 373.587-19.301 8.635-166.349-373.587zM64 463.746v-384h21.334v384h-21.334zM192 463.746v-384h21.334v384h-21.334z"
							fill="currentColor"></path>
					</svg>
					<Link href="/soundkits">
						<h2 className="text-white text-md font-bold hover:text-white capitalize">
							Soundkits
						</h2>
					</Link>
				</button>
				<button className="text-white hover:text-white flex items-center mt-4">
					<svg
						className="mr-4"
						viewBox="0 0 512 512"
						width="24"
						height="24"
						xmlns="http://www.w3.org/2000/svg">
						<path
							d="M291.301 81.778l166.349 373.587-19.301 8.635-166.349-373.587zM64 463.746v-384h21.334v384h-21.334zM192 463.746v-384h21.334v384h-21.334z"
							fill="currentColor"></path>
					</svg>
					<Link href="/beatpacks">
						<h2 className="text-white text-md font-bold hover:text-white capitalize">
							Beatpacks
						</h2>
					</Link>
				</button>
			</div>
			<div className="mt-10 mb-4 border-b border-neutral-800">
				<button className="flex items-center text-green-500 my-3 hover:text-white">
					<svg
						className="fill-emerald-600 mr-4"
						role="img"
						height="24"
						width="24"
						viewBox="0 0 16 16"
						color="#fff">
						<path fill="none" d="M0 0h16v16H0z"></path>
						<path d="M13.797 2.727a4.057 4.057 0 00-5.488-.253.558.558 0 01-.31.112.531.531 0 01-.311-.112 4.054 4.054 0 00-5.487.253c-.77.77-1.194 1.794-1.194 2.883s.424 2.113 1.168 2.855l4.462 5.223a1.791 1.791 0 002.726 0l4.435-5.195a4.052 4.052 0 001.195-2.883 4.057 4.057 0 00-1.196-2.883z"></path>
					</svg>
					<Link href="/liked">
						<h2 className="text-white text-md font-bold hover:text-white capitalize">
							Liked songs
						</h2>
					</Link>
				</button>
			</div>

			<div>
				<h2 className="font-semibold text-md ">
					Project TGC - <DecorText font="semibold">@seamusicmgmt</DecorText>
				</h2>
				<h2 className="font-semibold text-md ">
					I ♥ (developer) - <DecorText font="extrabold">@whyspacy</DecorText>
				</h2>
			</div>
		</div>
	);
}
