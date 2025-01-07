'use client';
import React from 'react';
import { fetchUsers } from '@/services/user/users';
import Table from '@/components/Table';
import { UserI } from '@/types/users';
import { TablePaginationI } from '@/types/common';

const ManagePlayersPage = () => {
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
        const result = await fetchUsers(pagination);
        setUsers(result.data);
        if (result?.data?.length) {
          setPagination(result);
          setUsers(result.data);
        }
      } catch (_error) {}
    });
  };
  return <></>;
};

export default ManagePlayersPage;
