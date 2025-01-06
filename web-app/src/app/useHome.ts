'use client';
import { CardPropsI } from '@/components/Card/types';
import { useRouter } from 'next/navigation';
// import { useRouter } from 'next/router';

export type MenuI = Pick<CardPropsI, 'title' | 'icon'> & {
  path: string;
};
const menu: MenuI[] = [
  {
    title: 'Add user',
    path: '/add-user',
    icon: '👤',
  },
  {
    title: 'Leaderboard',
    path: '/leaderboard',
    icon: '🏆',
  },
  {
    title: 'Manage Players',
    path: '/manage-player',
    icon: '⚙️',
  },
];
const useHome = () => {
  const router = useRouter();
  const handleCardClick = (title: string) => {
    router.push(menu.find((item) => item.title === title)!.path);
  };
  return { handleCardClick, menu };
};

export default useHome;
