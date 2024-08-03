import React, { useEffect, useRef, useState } from 'react';
import { MainLayout } from '@/shared/layouts';
import { Song } from '@/entities/song';
import { PostingBeatModal } from '@/entities/modals/beat-modal';
import { BeatService } from '@/services';
import { DefaultButton } from '@/shared/ui/buttons';
import { SongLoading } from '@/shared/ui/loading-elements';
import { KitLinkLoading } from '@/shared/ui/loading-elements';
import { DecorText } from '@/shared/ui/decor-text';
import { useAppSelector } from '@/shared/hooks/redux';
import { BeatResponseType } from '@/shared/types/beat-response';
import { SongType } from '@/shared/types';

export function Studio() {
	const [isModalOpen, setIsModalOpen] = useState<boolean>(false);
	const [beats, setBeats] = useState<BeatResponseType[]>();
	const [loading, setLoading] = useState<boolean>(true);
	const { user } = useAppSelector((state) => state.auth);

	const openModal = () => {
		setIsModalOpen(true);
	};

	const closeModal = () => {
		setIsModalOpen(false);
	};

	useEffect(() => {
		const get_all_beats = async () => {
			try {
				const response = await BeatService.all();
				const responseData = response.data;
				setBeats(responseData);
				setLoading(false);
				console.log('THIS IS RESPONSE', response);
			} catch (error) {
				setLoading(false);
				console.error();
			}
		};

		get_all_beats();
	}, []);

	return (
			<div className="p-2">
				<div className="flex mb-4 ">
					<div className="mr-2 ">
						<DefaultButton title="Upload beats" onClick={openModal} />
					</div>
					<div className="mr-2 ">
						<DefaultButton title="Upload beatpacks" ref="/beatpacks/add" />
					</div>
					<div className="mr-2 ">
						<DefaultButton title="Publish sound kits" ref="/soundkits/add" />
					</div>
					<div className="mr-2 ">
						<DefaultButton title="Add & Create squad" ref="" />
					</div>
					<div className="mr-2 ">
						<DefaultButton title="Add license" ref="" />
					</div>
				</div>

				<PostingBeatModal isOpen={isModalOpen} onClose={closeModal} />
				<h2
					className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter"
					id="playlist-title">
					Information:
				</h2>
				<h2 className="mt-2 mb-1 text-white text-lg capitalize font-semibold tracking-tighter flex items-center">
					You're a member of span
					<img
						className="w-8 rounded-full m-2"
						src={user.picture_url}
						alt=""
					/>{' '}
					<DecorText font="extrabold">REVENGE SQUAD</DecorText>
				</h2>
				<h2 className="mb-1 text-white text-lg capitalize font-semibold ">
					You're a member of span{' '}
				</h2>

				<h2
					className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter"
					id="playlist-title">
					Your beatpacks:
				</h2>
				<div className="flex overflow-auto justify-start items-center  m-1">
					<KitLinkLoading />
					<KitLinkLoading />
					<KitLinkLoading />
					<KitLinkLoading />
				</div>

				<h2
					className="mt-2 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter"
					id="playlist-title">
					Your tracks:
				</h2>
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
							<th className="text-xs">Action</th>
						</tr>
					</thead>
					<tbody>
						{!loading ? (
							beats?.map((beat) => (
								<Song
									id={beat.id}
									name={beat.title}
									picture={beat.picture_url}
									author={beat.prod_by}
									src={beat.file_url}
									album="Каждый из дизайнеров"
									date={beat.created_at}
									isAction={true}
									type="beat"
								/>
							))
						) : (
							<>
								<SongLoading />
								<SongLoading />
								<SongLoading />
								<SongLoading />
								<SongLoading />
							</>
						)}
					</tbody>
				</table>
			</div>
	);
}
