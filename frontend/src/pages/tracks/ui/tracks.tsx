import { useEffect, useState } from 'react';
import { Song } from '@/entities/song';
import { SongLoading } from '@/shared/ui/loading-elements';
import { TrackService } from '@/services';
import { LicenseLink } from '@/shared/ui/links';
import Comments from '@/shared/ui/comments/comments';
import { TrackResponseType } from '@/shared/types/Track-response';

export function Tracks() {
	const [Tracks, setTracks] = useState<TrackResponseType[]>([]);
	const [loading, setLoading] = useState(true);

	useEffect(() => {
		const fetchData = async () => {
			try {
				const response = await TrackService.all();
				const responseData = response.data;
				setTracks(responseData);
				setLoading(false);
			} catch (error) {
				console.error(error);
			}
		};

		fetchData();
	}, []);

	return (
		<>

		</>
	);
}
