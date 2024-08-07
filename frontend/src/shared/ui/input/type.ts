import { ReactNode } from 'react';

export type InputProps = {
	children?: ReactNode;
	placeholder: string;
	onChange?: () => void;
	type?: string;
	value?: string;
};
