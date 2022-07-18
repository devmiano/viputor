import { FaUsers } from 'react-icons/fa';

export default {
	title: 'User',
	name: 'user',
	icon: FaUsers,
	type: 'document',

	fields: [
		{
			title: 'User Name',
			name: 'username',
			type: 'string',
		},
		{
			title: 'Photo',
			name: 'photo',
			type: 'string',
		},
	],
};
