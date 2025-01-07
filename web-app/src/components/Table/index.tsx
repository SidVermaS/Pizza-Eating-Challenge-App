import React from 'react';
import { TablePropsI } from './types';

const Table: React.FC<React.PropsWithChildren<TablePropsI>> = ({ headings, children }) => {
  return (
    <div className="overflow-hidden sm:rounded-2xl border border-tertiary-light lg:w-1/2">
      <table className="table-fixed lg:w-full">
        <thead>
          <tr>
            {headings.map((heading) => (
              <th
                key={heading.text}
                className={`px-3 py-3 align-baseline text-sm font-bold text-secondary-light md:align-middle ${heading.className ?? ''}`}
              >
                {heading.text}
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
