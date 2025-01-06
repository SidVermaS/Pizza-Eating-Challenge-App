import type { Config } from 'tailwindcss';
import colors from 'tailwindcss/colors';
export default {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        background: 'var(--background)',
        foreground: 'var(--foreground)',
        primary: {
          light: colors.white,
          dark: '#181a1b',
        },
        secondary: {
          light: colors.purple['500'],
          dark: colors.purple['500'],
        },
        tertiary: {
          light: colors.gray['200'],
          dark: colors.gray['700'],
        },
        loiter: {
          light: colors.purple['100'],
          dark: colors.purple['900'],
        },
      },
      textColor: {
        primary: { light: colors.gray['800'], dark: colors.white },
        secondary: { light: colors.gray['500'], dark: colors.gray['400'] },
        loiter: {
          light: colors.purple['100'],
          dark: colors.white,
        },
      },
    },
  },
  plugins: [],
} satisfies Config;
