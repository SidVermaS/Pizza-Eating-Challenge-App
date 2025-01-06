'use client';

import { PaginationI, TablePaginationDataI } from '@/types/common';
import api from '@/services/api';
import { TablePaginationI } from '@/types/common';
import { UserI } from '@/types/users';

export const fetchUsers = async (
  pagination: PaginationI,
): Promise<TablePaginationDataI<UserI[]>> => {
  const response = await api.get(`/api/v1/users`, {
    params: {
      ...pagination,
    },
    headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
  });
  return response.data;
};
