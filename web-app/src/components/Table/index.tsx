import React from 'react';
import { TablePropsI } from './types';

const Table: React.FC<React.PropsWithChildren<TablePropsI>> = ({ headings, children }) => {
  return (
    <div className="overflow-hidden border border-tertiary-light sm:rounded-2xl lg:w-1/2 dark:border-tertiary-dark">
      <table className="table-fixed lg:w-full">
        <thead>
          <tr>
            {headings.map((heading) => (
              <th
                className={`py-3 align-baseline text-sm font-normal text-gray-600 md:align-middle dark:text-secondary-dark`}
              >
                {heading}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>{children}</tbody>
      </table>
    </div>
  );
};

export default Table;
