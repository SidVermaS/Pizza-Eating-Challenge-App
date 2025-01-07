import React from 'react';
import { TitlePropsI } from './types';

const Title = (props: TitlePropsI) => {
  return <div className="mb-6 text-center text-2xl sm:text-3xl">{props.text}</div>;
};

export default Title;
