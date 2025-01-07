import React from 'react';
import { TableCellI } from './types';

const TableCell: React.FC<React.PropsWithChildren<TableCellI>> = ({
  children,
  align = 'light',
  className,
  text,
}) => {
  return text?.length ? (
    <td
      className={`py-1 pr-1 text-${align} text-sm font-normal md:py-3 md:pr-3 ${className ?? ''}`}
    >
      {text}
    </td>
  ) : (
    children
  );
};

export default TableCell;
