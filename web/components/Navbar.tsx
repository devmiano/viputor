import Image from 'next/image';
import Link from 'next/link';
import React from 'react';
import Logo from '../utils/logo.png';
const Navbar = () => {
	return (
		<nav className='w-full flex justify-between items-center border-b-2 border-gray-700 py-2 px-4'>
			<Link href='/'>
				<div className='w-[120px]'>
					<Image className='cursor-pointer' src={Logo} alt='logo' />
				</div>
			</Link>
		</nav>
	);
};

export default Navbar;
