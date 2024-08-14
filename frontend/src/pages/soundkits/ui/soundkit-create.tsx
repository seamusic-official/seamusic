import { MainLayout } from '@/shared/layouts';
import dess from '@/shared/assets/everydesigner.png';
import { Song } from '@/entities/song';

export function SoundkitCreate() {
	return (
		<MainLayout>
			<div className="mt-8">
				<div className="flex  flex-col justify-center items-center md:hidden">
					<img
						src={dess}
						alt="alan walker artist image "
						className="w-40 h-40 rounded-full "
					/>
					<h1 className="text-white capitalize font-semibold text-2xl mt-2">
						This is Alan Walker
					</h1>
					<p className="text-xs uppercase text-gray-100 mt-1">
						1,308,405 likes
					</p>
				</div>
				<div className="hidden  flex items-center md:flex">
					<div className="relative">
						<img
							id="playlist-thumbnail"
							src="https://ugc.production.linktr.ee/e463406b-3ceb-4c69-9576-b9693c699bd1_photo-2024-01-06-19-09-46.jpeg?io=true&size=avatar-v3_0"
							alt="alan walker artist"
							className="w-72 h-72 mr-6 rounded-xl"
						/>

						<div className="m-1">
							<h2 className="text-gray-50 uppercase text-md overflow-wrap break-all w-64 font-bold tracking-tighter">
								contributers of this kit: <br />
							</h2>
							<p
								id="playlist-description"
								className="text-white text-md font-medium leading-none opacity-80">
								preview: @whyspacy
							</p>
						</div>
					</div>

					<div className="">
						<h2 className="text-gray-50 uppercase text-md font-bold tracking-tighter">
							Stash kit & Drum kit by @whyspacy x @nevermindaboutme
						</h2>
						<span className="text-white text-6xl tracking-tighter font-extrabold">
							<h1 id="playlist-title">/NEWERA</h1>
						</span>
						<div className="mr-1 mb-4 mt-4">
							<a
								className="p-2 m-1 font-semibold rounded-xl from-zinc-200 backdrop-blur-2xl border-neutral-900 bg-zinc-800/30 from-inherit"
								href="">
								Opium
							</a>
							<a
								className="p-2 m-1 font-semibold rounded-xl from-zinc-200 backdrop-blur-2xl border-neutral-900 bg-zinc-800/30 from-inherit"
								href="">
								Newjazz
							</a>
							<a
								className="p-2 m-1 font-semibold rounded-xl from-zinc-200 backdrop-blur-2xl border-neutral-900 bg-zinc-800/30 from-inherit"
								href="">
								Trap
							</a>
						</div>
						<p
							id="playlist-description"
							className="text-white mt-6 text-md font-medium leading-none opacity-80">
							+666 sounds for opium/hardrock, rage, jersey club, detroit/flint{' '}
							<br />
							invite in private channel by @whyspacy
							<br />
							my old kits - FOREVER, 2093STYLE etc.
							<br />
							<br />
							<br />
							discount on all beats (detail after receiving this pack)
							<br />
							and you will be added to the draw database (next post in my tgc)
							<br />
							<br />
							<br />
							to get:
							<br />
							sub to me (https://t.me/whyspacy) and nevermindaboutme
							(https://t.me/nevermindaboutme)
							<br />
							repost this post in your channel or friends
							<br />
							send proofs me (https://t.me/prodbyspxcyyy)
							<br />
						</p>
					</div>
				</div>
			</div>
			<div className="w-full ">
				<div className="w-full p-4">
					<div className="flex items-center text-white w-1/2 mx-4 my-2 md:flex">
						<svg
							className="bg-emerald-600 rounded-full w-12 h-12 p-3 text-white"
							role="img"
							height="24"
							width="24"
							viewBox="0 0 24 24"
							aria-hidden="true">
							<polygon
								points="21.57 12 5.98 3 5.98 21 21.57 12"
								fill="currentColor"></polygon>
						</svg>

						<div className="text-emerald-500">
							<svg
								className="mx-2 my-2 fill-current"
								role="img"
								height="38"
								width="38"
								viewBox="0 0 32 32">
								<path d="M27.319 5.927a7.445 7.445 0 00-10.02-.462s-.545.469-1.299.469c-.775 0-1.299-.469-1.299-.469a7.445 7.445 0 00-10.02 10.993l9.266 10.848a2.7 2.7 0 004.106 0l9.266-10.848a7.447 7.447 0 000-10.531z"></path>
							</svg>
						</div>
						<div className="text-gray-300">
							<svg
								className="fill-current"
								role="img"
								height="32"
								width="32"
								viewBox="0 0 32 32">
								<path d="M5.998 13.999A2 2 0 105.999 18 2 2 0 005.998 14zm10.001 0A2 2 0 1016 18 2 2 0 0016 14zm10.001 0A2 2 0 1026.001 18 2 2 0 0026 14z"></path>
							</svg>
						</div>
					</div>
					<h1 className="flex items-center text-white font-extrabold text-2xl mt-6">
						/NEWERA PREVIEW
					</h1>
					<div className="my-1 mx-2 h-72 overflow-y-auto md:h-full md:overflow-hidden">
						<table className="w-full cursor-default">
							<thead>
								<tr className="flex justify-around items-center text-gray-400 border-b border-gray-400 border-opacity-30 uppercase h-8">
									<th className="text-md">
										#<span className="text-xs ml-2">Picture</span>
									</th>
									<th className="text-md">
										#<span className="text-xs ml-2">Title</span>
									</th>
									<th className="text-xs">Album</th>
									<th className="text-xs">Date Added</th>
									<th className="">
										<svg width="16" height="16" viewBox="0 0 16 16" fill="none">
											<path
												d="M7.999 3H6.999V7V8H7.999H9.999V7H7.999V3ZM7.5 0C3.358 0 0 3.358 0 7.5C0 11.642 3.358 15 7.5 15C11.642 15 15 11.642 15 7.5C15 3.358 11.642 0 7.5 0ZM7.5 14C3.916 14 1 11.084 1 7.5C1 3.916 3.916 1 7.5 1C11.084 1 14 3.916 14 7.5C14 11.084 11.084 14 7.5 14Z"
												fill="currentColor"></path>
										</svg>
									</th>
								</tr>
							</thead>
							<tbody>
								<Song
									src={som}
									name="Каждый из дизайнеров"
									picture={dess}
									author="whyspacy?"
									album="Каждый из дизайнеров"
									date="02.01.2023"
								/>
							</tbody>
						</table>
					</div>

					<h1 className="flex items-center text-white font-extrabold text-2xl mt-6">
						OTHER KITS
					</h1>
				</div>
			</div>
		</MainLayout>
	);
}
