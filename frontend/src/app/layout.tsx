'use client';

import { Inter } from 'next/font/google';
import StoreProvider from './store-provider';
import { HelloLayout } from '@/shared/layouts';
import './globals.css';
import Head from 'next/head';

const inter = Inter({ subsets: ['latin'] });

const RootLayout = ({
	children,
}: Readonly<{
	children: React.ReactNode;
}>) => {
	return (
		<html lang="ru">
			<Head>
				<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400&display=swap" rel="stylesheet" />
			</Head>
			<body style={{fontFamily: "Montserrat"}}>
				<StoreProvider>
					{children}
				</StoreProvider>
			</body>
		</html>
	);
};

export default RootLayout;
