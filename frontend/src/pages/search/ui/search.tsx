import React, {
	ChangeEvent,
	ChangeEventHandler,
	useEffect,
	useState,
} from 'react';
import { MainLayout } from '@/shared/layouts';
import { Input } from '@/shared/ui/input';
import { ArtistLink } from '@/shared/ui/links';
import { SpotifyService } from '@/services';
import { Song } from '@/entities/song';
import { SongLink } from '@/shared/ui/links';
import { PictureLink } from '@/shared/ui/links';
import msToMin from '@/shared/utils/ms-to-min';
import { ArtistLinkLoading } from '@/shared/ui/loading-elements';
import { PictureLinkLoading } from '@/shared/ui/loading-elements';
import { SongLoading } from '@/shared/ui/loading-elements';
import { useAppSelector, useAppDispatch } from '@/shared/hooks/redux';
import { setSearchQuery } from '@/store/reducers/searchSlice';

export function Search() {
	const dispatch = useAppDispatch();
	const { query } = useAppSelector((state) => state.search);

	const [data, setData] = useState([]);
	const [loading, setLoading] = useState(true);
	const [status, setStatus] = useState(false);

	const handleInputChange: ChangeEventHandler<HTMLInputElement> = (event) => {
		dispatch(setSearchQuery(event.target.value));
	};

	useEffect(() => {
		const get_response = async () => {
			try {
				const response = await SpotifyService.search(query);
				const responseData = response.data;
				setData(responseData);
				setLoading(false);
				setStatus(true);
				console.log('THIS IS RESPONSE', response);
			} catch (error) {
				setLoading(false);
				console.error();
			}
		};

		get_response();
	}, [query]);

	return (
		<MainLayout>
			<form>
				<Input
					type="text"
					buttonText="Search"
					placeholder="xxxmanera.."
					value={query}
					onChange={(e) => handleInputChange(e)}
				/>
			</form>
			<div>
				{status ? (
					!loading ? (
						<div>
							<h2
								className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter"
								id="playlist-title">
								Artists:
							</h2>
							<div className="flex overflow-auto justify-start items-center">
								{data.map(
									(item) =>
										item.type === 'artist' && (
											<div key={item.id}>
												<ArtistLink
													key={item.id}
													link="/profile/1"
													image={item.image_url}
													title={item.name}
												/>
											</div>
										)
								)}
							</div>
							<h2
								className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter"
								id="playlist-title">
								Albums:
							</h2>
							<div className="flex overflow-auto justify-start items-center">
								{data.map(
									(item) =>
										item.type === 'album' && (
											<div className="m-1" key={item.id}>
												<PictureLink
													link={`/albums/${item.id}`}
													artist={item.artist}
													image={item.image_url}
													title={item.name}
												/>
											</div>
										)
								)}
							</div>
							<h2
								className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter"
								id="playlist-title">
								Tracks:
							</h2>
							<div>
								{data.map(
									(item) =>
										item.type === 'track' && (
											<div key={item.id}>
												<Song
													id={item.id}
													name={item.name}
													date={item.release_date}
													duration={msToMin(item.duration_ms)}
													author={item.artist}
													picture={item.image_url}
													album={item.name}
												/>
											</div>
										)
								)}
							</div>
						</div>
					) : (
						<div>
							<h2
								className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter"
								id="playlist-title">
								Artists:
							</h2>
							<div className="flex overflow-auto justify-start items-center">
								<ArtistLinkLoading />
								<ArtistLinkLoading />
								<ArtistLinkLoading />
								<ArtistLinkLoading />
								<ArtistLinkLoading />
							</div>
							<h2
								className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter"
								id="playlist-title">
								Albums:
							</h2>
							<div className="flex overflow-auto justify-start items-center">
								<PictureLinkLoading />
								<PictureLinkLoading />
								<PictureLinkLoading />
								<PictureLinkLoading />
							</div>
							<h2
								className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter"
								id="playlist-title">
								Tracks:
							</h2>
							<div>
								<SongLoading />
								<SongLoading />
								<SongLoading />
								<SongLoading />
							</div>
						</div>
					)
				) : (
					<h2
						className="mt-4 mb-2 text-white text-3xl capitalize font-extrabold tracking-tighter"
						id="playlist-title">
						Search on Seamusic
					</h2>
				)}
			</div>
		</MainLayout>
	);
}
