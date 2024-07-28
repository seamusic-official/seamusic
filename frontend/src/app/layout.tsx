'use client';

import { Inter } from 'next/font/google';
import StoreProvider from './store-provider';
import { HelloLayout } from '@/shared/layouts';
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
				<StoreProvider>
					<HelloLayout>{children}</HelloLayout>
				</StoreProvider>
			</body>
		</html>
	);
};

export default RootLayout;
