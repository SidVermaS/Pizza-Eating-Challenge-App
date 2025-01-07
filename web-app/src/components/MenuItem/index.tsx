import React from 'react';
import { MenuItemPropsI } from './types';
import Card from '../Card';

const MenuItem = ({ icon, title }: MenuItemPropsI) => {
  return (
    <div className="text-center">
      <div className="text-8xl">{icon}</div>
      <div className="mt-7 text-xl text-primary-light">{title}</div>
    </div>
  );
};

export default MenuItem;
