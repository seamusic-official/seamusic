'use client';

import { Montserrat } from 'next/font/google';
import StoreProvider from './store-provider';
import './globals.css';

const montserrat = Montserrat({ subsets: ['latin'] });

const RootLayout = ({
	children,
}: Readonly<{
	children: React.ReactNode;
}>) => {
	return (
		<html lang="ru">
			<body className={montserrat.className}>
				<StoreProvider>
					{children}
				</StoreProvider>
			</body>
		</html>
	);
};

export default RootLayout;
