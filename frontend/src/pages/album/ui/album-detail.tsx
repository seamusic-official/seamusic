import Link from 'next/link';
import { MainLayout } from '@/shared/layouts';
import { SpotifyService } from '@/services';
import { useEffect, useState } from 'react';
import { Song } from '@/entities/song';
import msToMin from '@/shared/utils/ms-to-min';
import { SongLoading } from '@/shared/ui/loading-elements';

export function AlbumDetail() {
	const [data, setData] = useState([]);
	const id = 1;
	const [loading, setLoading] = useState(true);

	useEffect(() => {
		const fetchData = async () => {
			try {
				const response = await SpotifyService.get_album(id);
				const responseData = response.data;
				setData(responseData);
			} catch (error) {
				console.error(error);
			}
		};

		fetchData();
	}, []);

	useEffect(() => {
		const fetchData = async () => {
			try {
				const response = await SpotifyService.get_tracks_from_album(id);
				const responseData = response.data;
				setData(responseData);
				console.log(responseData);
				setLoading(false);
			} catch (error) {
				console.error(error);
			}
		};

		fetchData();
	}, []);

	return (
		<MainLayout>
			<div className="">
				<div className="flex flex-col justify-center items-center md:hidden">
					<img
						src={'data.image_url'}
						alt="alan walker artist image"
						className="w-40 h-40 rounded-lg"
					/>
					<h1 className="text-white capitalize font-semibold text-2xl mt-2 truncate">
						{'data.name'}
					</h1>
					<p className="text-xs uppercase text-gray-100 mt-1">
						1,308,405 likes
					</p>
				</div>
				<div className="hidden mt-8 flex items-center md:flex">
					{!loading ? (
						<img
							id="playlist-thumbnail"
							src={'data.picture_url'}
							alt="alan walker artist"
							className="w-56 h-56 ml-4 mr-6 rounded-lg"
						/>
					) : (
						<div className="w-56 h-56 mr-6 rounded-lg animate-pulse bg-gray-300 bg-opacity-10"></div>
					)}
					{!loading ? (
						<div className="mt-16">
							<h2 className="text-gray-50 uppercase text-md font-semibold tracking-tighter mr-2 mt-1">
								Album by
								{data.artists?.map((artist) => (
									<span className="ml-1 font-extrabold">{artist.name}</span>
								))}
							</h2>
							<span className="text-white text-6xl capitalize font-extrabold tracking-tighter">
								<h1 id="playlist-title">{'data.name'} </h1>
							</span>
							<p
								id="playlist-description"
								className="text-white mt-6 text-sm font-normal leading-none opacity-70">
								{'info'}
							</p>
							<div className="flex items-center mt-2">
								<a className="text-white font-extrabold text-md hover:text-underline cursor-pointer">
									SeaMusic
								</a>

								<div className="font-extrabold text-md text-white opacity-70 mx-1 mb-1 pb-1">
									.
								</div>
								<p className="text-white opacity-70 font-normal text-sm">
									1,308,405 likes
								</p>
								<div className="font-extrabold text-md text-white opacity-70 mx-1 mb-1 pb-1">
									.
								</div>
								<p className="text-white opacity-70 font-normal text-sm mr-1">
									{'data.total_tracks'} songs,
								</p>
								<p className="text-white opacity-70 font-normal text-sm">
									2hr 36 min
								</p>
							</div>
						</div>
					) : (
						<div className="mt-16">
							<h2 className="rounded-md text-md w-56 h-4 animate-pulse bg-gray-300 bg-opacity-10 mr-2 mt-1"></h2>
							<h1 className="rounded-md text-6xl text-sm w-full h-10 animate-pulse bg-gray-300 bg-opacity-10 mt-4"></h1>
							<p className="rounded-md  w-12 h-4 animate-pulse bg-gray-300 bg-opacity-10 mt-4">
								{'data.description'}
							</p>
							<div className="flex items-center mt-2">
								<a className="text-white font-extrabold text-md hover:text-underline cursor-pointer">
									SeaMusic
								</a>

								<div className="font-extrabold text-md text-white opacity-70 mx-1 mb-1 pb-1 m-1">
									.
								</div>
								<p className="rounded-md w-12 h-4  animate-pulse bg-gray-300 bg-opacity-10 m-1"></p>
								<div className="font-extrabold text-md text-white opacity-70 mx-1 mb-1 pb-1 m-1">
									.
								</div>
								<p className="rounded-md w-12 h-4  animate-pulse bg-gray-300 bg-opacity-10 text-sm mr-1"></p>
								<p className="rounded-md w-8 h-4  animate-pulse bg-gray-300 bg-opacity-10 text-sm m-1 "></p>
							</div>
						</div>
					)}
				</div>
			</div>
			<div className="w-full ">
				<div className="w-full p-4">
					<div className="flex justify-center items-center m-4 md:hidden">
						<button className="bg-emerald-600 text-white uppercase text-xs rounded-full font-semibold tracking-widest px-8 py-3">
							Listen it
						</button>
					</div>
					<div className="hidden flex items-center text-white w-1/2 my-2 md:flex">
						<svg
							className="bg-emerald-600 rounded-full w-12 h-12 p-3 text-white"
							height="28"
							role="img"
							width="28"
							viewBox="0 0 24 24"
							aria-hidden="true">
							<polygon
								points="21.57 12 5.98 3 5.98 21 21.57 12"
								fill="currentColor"></polygon>
						</svg>
						<div className="text-emerald-600">
							<svg
								className="mx-4 my-2 fill-current"
								role="img"
								height="32"
								width="32"
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

					<div className="my-10 h-72 md:h-full md:overflow-hidden">
						<table className="w-full">
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
								{!loading ? (
									tracks.map((song) => (
										<Song
											id={song.id}
											name={song.name}
											date={'data.release_date'}
											duration={msToMin(song.duration_ms)}
											src={song.preview_url}
											author={song.artist}
											type={song.type}
											picture={'data.image_url'}
											album={'data.name'}
											spotify_url={song.spotify_url}
										/>
									))
								) : (
									<div>
										<SongLoading />
										<SongLoading />
										<SongLoading />
										<SongLoading />
									</div>
								)}
							</tbody>
						</table>
					</div>
				</div>
			</div>
		</MainLayout>
	);
}
