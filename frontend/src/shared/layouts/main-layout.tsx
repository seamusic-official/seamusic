'use client';
import React, { useRef } from 'react';
import { Sidebar } from '@/widgets/sidebar';
import { NavBar } from '@/widgets/navbar';
import { Footer } from '@/widgets/footer';
import { RouterLayoutWithStaticPlayer } from './router-layout';

type MyComponentProps = React.PropsWithChildren;

export function MainLayout({ children }: MyComponentProps) {
	return (
		<div className="w-screen max-w-screen-xl overflow-y-auto ">
			<main className="tracking-tighter">
				<Sidebar />
				<div className="text-center lg:text-left w-full md:w-4/5 md:absolute md:right-0 relative place-items-center ">
					<div className="p-4">
						<NavBar reference="" />
						{children}
						<Footer />
					</div>
				</div>
				<RouterLayoutWithStaticPlayer auth={true} />
			</main>
		</div>
	);
}
