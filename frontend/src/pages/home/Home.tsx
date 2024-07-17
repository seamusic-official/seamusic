import React, { useEffect, useState } from 'react'
import MainLayout from '../../components/layouts/MainLayout'
import SpotifyService from '../../services/SpotifyService'
import AuthService from '../../services/AuthService'
import BeatpackService from '../../services/BeatpackServise'
import PictureLink from '../../components/PictureLink'
import PictureLinkLoading from '../../components/loading-elements/PictureLinkLoading'
import SongLink from '../../components/songs/SongLink'
import SongLinkLoading from '../../components/loading-elements/SongLinkLoading'
import ArtistLink from '../../components/artists/ArtistLink'
import ArtistLinkLoading from '../../components/loading-elements/ArtistLinkLoading'
import useAuth from '../../hooks/useAuth'

const Home = () => {
	const [albums, setAlbums] = useState([])
	const [beatpacks, setBeatpacks] = useState([])
	const [loading, setLoading] = useState(true)
	// const [beats, setBeats] = useState([]);
	const [tracks, setTracks] = useState([])
	// const [artists, setArtists] = useState([]);
	const [producers, setProducers] = useState([])

	const searchParams = new URLSearchParams(window.location.search)
	const code = searchParams.get('code')
	useAuth(code)

	// const user = useAppSelector((state) => state.auth.user);

	useEffect(() => {
		const fetchData = async () => {
			try {
				const response = await SpotifyService.get_albums()
				const responseData = response.data
				setAlbums(responseData)
				setLoading(false)
			} catch (error) {
				setLoading(true)
				console.error(error)
			}
		}

		fetchData()
	}, [])

	useEffect(() => {
		const fetchData = async () => {
			try {
				const response = await AuthService.get_producers()
				const responseData = response.data
				setProducers(responseData)
				setLoading(false)
			} catch (error) {
				setLoading(true)
				console.error(error)
			}
		}

		fetchData()
	}, [])

	useEffect(() => {
		const fetchData = async () => {
			try {
				const response = await BeatpackService.all()
				const responseData = response.data
				setBeatpacks(responseData)
				setLoading(false)
			} catch (error) {
				setLoading(true)
				console.error(error)
			}
		}

		fetchData()
	}, [])

	useEffect(() => {
		const fetchData = async () => {
			try {
				const response = await SpotifyService.get_all()
				const responseData = response.data
				setTracks(responseData)
			} catch (error) {
				console.error(error)
			}
		}

		fetchData()
	}, [])

	return (
		<MainLayout>
			<div className='mb-4 ml-2 mt-4'>
				<a
					className='p-2 m-1 border-emerald-600 border hover:border-emerald-800 font-semibold rounded-xl from-zinc-200 backdrop-blur-2xl border-neutral-900 bg-zinc-800/30 from-inherit'
					href=''
				>
					Beats
				</a>
				<a
					className='p-2 m-1 border-emerald-600 border hover:border-emerald-800 font-semibold rounded-xl from-zinc-200 backdrop-blur-2xl border-neutral-900 bg-zinc-800/30 from-inherit'
					href=''
				>
					Artists
				</a>
				<a
					className='p-2 m-1 border-emerald-600 border hover:border-emerald-800 font-semibold rounded-xl from-zinc-200 backdrop-blur-2xl border-neutral-900 bg-zinc-800/30 from-inherit'
					href=''
				>
					Tracks
				</a>
			</div>

			<h2
				className='mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter'
				id='playlist-title'
			>
				Playlists:
			</h2>
			<div>
				{!loading ? (
					albums ? (
						<div className='flex overflow-hidden justify-start items-center'>
							{albums.map(item => (
								<div>
									<PictureLink
										link={`/albums/${item.id}`}
										image={item.image_url}
										title={item.name}
									/>
								</div>
							))}
						</div>
					) : (
						<PictureLinkLoading />
					)
				) : (
					<div className='flex overflow-hidden justify-start items-center'>
						<PictureLinkLoading />
						<PictureLinkLoading />
						<PictureLinkLoading />
						<PictureLinkLoading />
						<PictureLinkLoading />
						<PictureLinkLoading />
					</div>
				)}
			</div>
			<h2
				className='mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter'
				id='playlist-title'
			>
				Tracks:
			</h2>
			{!loading ? (
				tracks ? (
					<div className='p-4'>
						<div className='flex justify-start items-center gap-4 flex-wrap'>
							{tracks.map(item => (
								<div>
									<SongLink
										link={`/albums/${item.id}`}
										image={item.image_url}
										title={item.name}
									/>
								</div>
							))}
						</div>
					</div>
				) : (
					<div className='p-4'>
						<div className='flex justify-start items-center gap-4 flex-wrap'>
							<SongLinkLoading />
						</div>
					</div>
				)
			) : (
				<div className='p-4'>
					<div className='flex justify-start items-center gap-4 flex-wrap'>
						<SongLinkLoading />
						<SongLinkLoading />
						<SongLinkLoading />
						<SongLinkLoading />
						<SongLinkLoading />
						<SongLinkLoading />
						<SongLinkLoading />
						<SongLinkLoading />
						<SongLinkLoading />
						<SongLinkLoading />
						<SongLinkLoading />
						<SongLinkLoading />
						<SongLinkLoading />
					</div>
				</div>
			)}
			<h2
				className='mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter'
				id='playlist-title'
			>
				Producers:
			</h2>
			<div className='flex overflow-auto justify-start items-center m-1'>
				{!loading ? (
					<div>
						{producers.map(producer => (
							<ArtistLink title={producer.name} image={producer.picture_url} />
						))}
					</div>
				) : (
					<div>
						<ArtistLinkLoading />
						<ArtistLinkLoading />
						<ArtistLinkLoading />
						<ArtistLinkLoading />
					</div>
				)}

				<ArtistLinkLoading />
			</div>
			<h2
				className='mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter'
				id='playlist-title'
			>
				Artists:
			</h2>
			<div className='flex overflow-auto justify-start items-center m-1'>
				<ArtistLinkLoading />
				<ArtistLinkLoading />
				<ArtistLinkLoading />
				<ArtistLinkLoading />
				<ArtistLinkLoading />
			</div>

			<h2
				className='mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter'
				id='playlist-title'
			>
				Beatpacks:
			</h2>
			{!loading ? (
				beatpacks ? (
					<div className='flex overflow-auto justify-start items-center'>
						{beatpacks.map(item => (
							<div>
								<PictureLink
									link={`/beatpacks/${item.id}`}
									image={item.picture}
									title={item.title}
								/>
							</div>
						))}
					</div>
				) : (
					<PictureLinkLoading />
				)
			) : (
				<div className='flex overflow-auto justify-start items-center'>
					<PictureLinkLoading />
					<PictureLinkLoading />
					<PictureLinkLoading />
					<PictureLinkLoading />
					<PictureLinkLoading />
					<PictureLinkLoading />
				</div>
			)}
		</MainLayout>
	)
}

export default Home
