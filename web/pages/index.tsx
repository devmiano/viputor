import type { NextPage } from 'next';
import Head from 'next/head';

const Home: NextPage = () => {
	return (
		<div className=''>
			<Head>
				<title>Viputor</title>
				<meta name='description' content='Social Media App' />
				<link rel='icon' href='/favicon.ico' />
			</Head>

			<main className='prose'>
				<h1 className=''>
					Welcome to <a href='https://nextjs.org'>Viputor</a>
				</h1>
			</main>
		</div>
	);
};

export default Home;
