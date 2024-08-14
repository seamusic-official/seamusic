import { useEffect, useState } from 'react';
import { Song } from '@/entities/song';
import { SongLoading } from '@/shared/ui/loading-elements';
import { BeatService } from '@/services';
import { LicenseLink } from '@/shared/ui/links';
import Comments from '@/shared/ui/comments/comments';
import { BeatResponseType } from '@/shared/types/beat-response';

export function Beats() {
	const [beats, setBeats] = useState<BeatResponseType[]>([]);
	const [loading, setLoading] = useState(true);

	useEffect(() => {
		const fetchData = async () => {
			try {
				const response = await BeatService.all();
				const responseData = response.data;
				setBeats(responseData);
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
