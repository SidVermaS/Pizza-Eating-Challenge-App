import React from 'react';
import { CardPropsI } from './types';

const Card: React.FC<React.PropsWithChildren<CardPropsI>> = ({ children, handleClick, id }) => {
  return (
    <div
      onClick={handleClick && id ? handleClick?.bind(this, id) : undefined}
      className="lg:w-42 lg:h-42 flex h-60 w-72 cursor-pointer items-center justify-center overflow-hidden rounded-xl shadow shadow-gray-500 sm:h-40 sm:w-72 md:h-52 md:w-48"
    >
      {children}
    </div>
  );
};

export default Card;
