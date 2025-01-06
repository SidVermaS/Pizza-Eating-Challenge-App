'use client';
import React from 'react';
import { fetchUsers } from '@/services/user/users';
import { GetServerSideProps } from 'next';
import { PaginationI } from '@/types/services';
``;
const LeaderboardPage = () => {
  const [users, setUsers] = React.useState([]);
  const [pagination, setPagination] = React.useState<PaginationI>({ page: 1, per_page: 15 });
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
          setUsers(result.data);
        }
      } catch (_error) {}
    });
  };
  return (
    <>
     
    </>
  );
};

export default LeaderboardPage;
