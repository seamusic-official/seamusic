export type PlaylistResponseType = {
	id: string;
	name: string;
	owner: {
		id: string;
		display_name: string;
	};
	tracks: {
		total: number;
		items: {
			track: {
				id: string;
				name: string;
			};
		}[];
	};
};
