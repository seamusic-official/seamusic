import React from 'react';
import { SubmitButtonType } from '../submit-button/type';

export function SubmitButton({ title }: SubmitButtonType) {
	return (
		<div>
			<button
				className="p-2 border-emerald-600 border hover:border-emerald-800  font-bold rounded-xl from-zinc-200 backdrop-blur-2xl border-neutral-900 bg-zinc-800/30 from-inherit"
				type="submit">
				{title}
			</button>
		</div>
	);
}
