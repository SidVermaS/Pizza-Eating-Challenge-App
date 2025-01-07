'use client';
import { CardPropsI } from '@/components/Card/types';
import { MenuItemPropsI } from '@/components/MenuItem/types';
import { useRouter } from 'next/navigation';

export type MenuI = Pick<MenuItemPropsI, 'title' | 'icon'> & {
  path: string;
};
const menu: MenuI[] = [
  {
    title: 'Add user',
    path: '/new-user',
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
