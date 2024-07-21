export function MainMenu() {
	return (
		<div className="p-2 lg:hidden xl:hidden fixed left-0 bottom-0 right-0">
			<div className="flex justify-around mt-2 text-gray-200 text-xs hover:text-white">
				<button className="flex flex-col items-center">
					<svg
						className=""
						viewBox="0 0 512 512"
						width="20"
						height="20"
						xmlns="http://www.w3.org/2000/svg">
						<path
							d="M 256.274 60.84 L 84.324 166.237 L 84.324 443.063 L 193.27 443.063 L 193.27 293.73 L 320.228 293.73 L 320.228 443.063 L 428.222 443.063 L 428.222 165.476 L 256.274 60.84 Z M 256.274 35.95 L 448.452 149.145 L 448.452 464.395 L 300 464.395 L 300 315.062 L 213.499 315.062 L 213.499 464.395 L 64.095 464.395 L 64.095 150.161 L 256.274 35.95 Z"
							fill="currentColor"></path>
					</svg>
					Home
				</button>
				<button className="flex flex-col items-center">
					<svg
						className=""
						viewBox="0 0 512 512"
						width="20"
						height="20"
						xmlns="http://www.w3.org/2000/svg">
						<path
							d="M349.714 347.937l93.714 109.969-16.254 13.969-93.969-109.969q-48.508 36.825-109.207 36.825-36.826 0-70.476-14.349t-57.905-38.603-38.603-57.905-14.349-70.476 14.349-70.476 38.603-57.905 57.905-38.603 70.476-14.349 70.476 14.349 57.905 38.603 38.603 57.905 14.349 70.476q0 37.841-14.73 71.619t-40.889 58.921zM224 377.397q43.428 0 80.254-21.461t58.286-58.286 21.461-80.254-21.461-80.254-58.286-58.285-80.254-21.46-80.254 21.46-58.285 58.285-21.46 80.254 21.46 80.254 58.285 58.286 80.254 21.461z"
							fill="currentColor"
							fill-rule="evenodd"></path>
					</svg>
					Search
				</button>
				<button className="flex flex-col items-center">
					<svg
						className=""
						viewBox="0 0 512 512"
						width="20"
						height="20"
						xmlns="http://www.w3.org/2000/svg">
						<path
							d="M291.301 81.778l166.349 373.587-19.301 8.635-166.349-373.587zM64 463.746v-384h21.334v384h-21.334zM192 463.746v-384h21.334v384h-21.334z"
							fill="currentColor"></path>
					</svg>
					Library
				</button>
				<button className="flex flex-col items-center">
					<svg
						className="fill-current"
						role="img"
						height="20"
						width="20"
						viewBox="0 0 24 24">
						<path d="M11.5 0C5.149 0 0 5.148 0 11.5 0 17.851 5.149 23 11.5 23S23 17.851 23 11.5C23 5.148 17.851 0 11.5 0zm0 22C5.71 22 1 17.29 1 11.5S5.71 1 11.5 1 22 5.71 22 11.5 17.29 22 11.5 22zm.499-6.842V5h-1v10.149l-3.418-3.975-.758.652 4.678 5.44 4.694-5.439-.757-.653-3.439 3.984z"></path>
					</svg>
					Get App
				</button>
			</div>
		</div>
	);
}
