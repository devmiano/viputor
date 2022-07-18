/** @type {import('tailwindcss').Config} */

const defaultTheme = require('tailwindcss/defaultTheme');

module.exports = {
	content: [
		'./pages/**/*.{html,js,ts,tsx,jsx}',
		'./components/**/*.{html,js,ts,tsx,jsx}',
	],
	theme: {
		daisyui: {
			themes: ['night'],
		},
		extend: {
			fontFamily: {
				sans: ['Urbanist', ...defaultTheme.fontFamily.sans],
				serif: ['Space Grotesk', ...defaultTheme.fontFamily.serif],
				mono: ['Space Mono', ...defaultTheme.fontFamily.mono],
			},
		},
	},
	plugins: [
		require('@tailwindcss/forms'),
		require('@tailwindcss/line-clamp'),
		require('@tailwindcss/typography'),
		require('daisyui'),
	],
};
