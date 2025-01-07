import React from 'react';
import { TableRowI } from './types';

const TableRow: React.FC<React.PropsWithChildren<TableRowI>> = ({ children, className }) => {
  return (
    <tr className={`text-primary-light hover:bg-loiter-light ${className ?? ''} `}>{children}</tr>
  );
};

export default TableRow;
