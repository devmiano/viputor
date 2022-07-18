import { FaUsers } from 'react-icons/fa';

export default {
	title: 'Comment',
	name: 'comment',
	icon: FaUsers,
	type: 'document',

	fields: [
		{
			title: 'Posted By',
			name: 'postedBy',
			type: 'postedBy',
		},
		{
			title: 'Comment',
			name: 'comment',
			type: 'string',
		},
	],
};
