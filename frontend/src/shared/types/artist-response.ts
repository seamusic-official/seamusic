export type ArtistResponseType = {
	id: string;
	name: string;
	genres: string[];
	followers: {
		total: number;
	};
	images: {
		url: string;
		height: number;
		width: number;
	}[];
};
