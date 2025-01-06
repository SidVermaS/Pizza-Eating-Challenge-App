'use client';
import React from 'react';
import useHome from './useHome';
import Card from '@/components/Card';
const HomePage = () => {
  const { handleCardClick, menu } = useHome();
  return (
    <div className="grid grid-cols-1 gap-x-14 gap-y-12 sm:grid-cols-2 md:grid-cols-2">
      {menu.map((menuItem, index) => (
        <Card
          key={index}
          icon={menuItem.icon}
          title={menuItem.title}
          handleClick={handleCardClick}
        />
      ))}
    </div>
  );
};

export default HomePage;
