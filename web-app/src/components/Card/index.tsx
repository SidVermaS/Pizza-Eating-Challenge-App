import React from 'react';
import { CardPropsI } from './types';

const Card = (props: CardPropsI) => {
  return (
    <div
      onClick={props.handleClick.bind(this, props.title)}
      className="lg:w-42 lg:h-42 flex h-60 w-72 cursor-pointer items-center justify-center overflow-hidden rounded-xl shadow shadow-gray-500 sm:h-40 sm:w-72 md:h-52 md:w-48"
    >
      <div className="text-center">
        <div className="text-8xl">{props.icon}</div>
        <div className="mt-7 text-xl text-primary-light">{props.title}</div>
      </div>
    </div>
  );
};

export default Card;
