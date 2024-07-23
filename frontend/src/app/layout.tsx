'use client';

import { Inter } from 'next/font/google';
import { Provider } from 'react-redux';
import { store } from '@/store/store';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

const RootLayout = ({
	children,
}: Readonly<{
	children: React.ReactNode;
}>) => {
	return (
		<html lang="ru">
			<body>
				<Provider store={store}>{children}</Provider>
			</body>
		</html>
	);
};

export default RootLayout;
