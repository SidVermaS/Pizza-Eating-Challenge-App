'use client';
import React from 'react';
import { fetchUsers } from '@/services/user/users';
import Table from '@/components/Table';
import { UserI } from '@/types/users';
import { TablePaginationI } from '@/types/common';
import TableRow from '@/components/TableRow';
import TableCell from '@/components/TableCell';
import { GenderE } from '@/consts/users';
import { headings } from './useLeaderboardPage';

const LeaderboardPage = () => {
  const [users, setUsers] = React.useState<UserI[]>([]);
  const [pagination, setPagination] = React.useState<TablePaginationI>({
    current_page: 0,
    pages: 0,
    total: 0,
    page: 1,
    per_page: 15,
  });
  const [isPending, startTransition] = React.useTransition();
  React.useEffect(() => {
    fetchData();
  }, []);
  const fetchData = () => {
    startTransition(async () => {
      try {
        const result = await fetchUsers({ ...pagination, sort_by: 'rank' });
        setUsers(result.data);
        if (result?.data?.length) {
          setPagination(result);
          setUsers(result.data);
        }
      } catch (_error) {}
    });
  };
  return (
    <>
      <div className="mb-6 text-center text-2xl sm:text-3xl">Champions 🏆</div>
      <Table headings={headings}>
        {users.map((user) => (
          <TableRow key={user.id}>
            <TableCell className="px-3" align="right" text={user.rank.toString()} />
            <TableCell className="px-3" text={user.name} />
            <TableCell className="px-3" align="right" text={user.age.toFixed()} />
            <TableCell className="px-3" text={GenderE[user.gender]} />
            <TableCell className="px-3" align="right" text={user.consumed_count.toString()} />
          </TableRow>
        ))}
      </Table>
    </>
  );
};

export default LeaderboardPage;
