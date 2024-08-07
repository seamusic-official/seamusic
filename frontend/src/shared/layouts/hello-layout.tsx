'use client';

import React, { useRef } from 'react';
import { Footer } from '@/widgets/footer';
import { DropdownMenu } from '@/entities/menu';
import Link from 'next/link';
import bg1 from "@/assets/bg-one.jpg"

export const HelloLayout = ({ children }: { children: React.ReactNode }) => {
	return (
		<div className="relative overflow-hidden">
   			<div className="fixed inset-0 bg-cover bg-center" style={{ backgroundImage: "url('/assets/shared/bg-one.jpg')", height: '100vh', width: '100vw' }}></div>
			<div className="p-4">
				<div className="p-2 fixed top-0 right-0 left-0 backdrop-blur-md z-20 border-neutral-800 border-b">
					<div className="flex justify-between mx-4 items-center">
						<div className="text-gray-100 my-2 cursor-pointer">
							<h2
								className="flex items-center mt-1 mb-1 text-white text-3xl capitalize font-extrabold tracking-tighter"
								id="">
								<div className="p-2 rounded-full w-8 h-8 mr-2 animate-pulse rounded-full bg-opacity-10 bg-gray-300" />
								<Link href="/">SeaMusic</Link>
							</h2>
						</div>
						<ul className="hidden lg:relative w-full flex justify-center items-center font-semibold p-2 p-0 border border-gray-100  flex-row mt-0 border-0">
							<li>
								<a
									href="#"
									className="block px-5 text-white rounded hover:text-gray-100">
									<Link href="/">Home</Link>
								</a>
							</li>
							<li>
								<a
									href="#"
									className="block px-5 text-white rounded hover:text-gray-100">
									Services
								</a>
							</li>
							<li>
								<a
									href="#"
									className="block px-5 text-white rounded hover:text-gray-100">
									Pricing
								</a>
							</li>
							<li>
								<a
									href="#"
									className="block px-5 text-white rounded hover:text-gray-100">
									Contact
								</a>
							</li>
						</ul>
						<div className="flex justify-between items-center">
							<DropdownMenu />
						</div>
					</div>
				</div>
				<div className="">{children}</div>
				<div>
					<Footer />
				</div>
			</div>
	</div>
	);
};
