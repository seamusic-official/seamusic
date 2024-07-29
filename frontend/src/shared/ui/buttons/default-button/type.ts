import { LinkProps } from 'next/link';
import { Url } from 'url';

export type DefaultButtonType = {
	title: string;
	ref?: string;
	onClick?: () => void;
	className?: string;
};
