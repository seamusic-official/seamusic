export type TrackResponseType = {
	id: string;
	name: string;
	album: {
		name: string;
		images: {
			url: string;
			height: number;
			width: number;
		}[];
	};
	artists: {
		id: string;
		name: string;
	}[];
	duration_ms: number;
	preview_url: string;
};
