'use client';

import { PaginationI } from '@/types/services';
import api from '@/services/api';

export const fetchUsers = async (pagination: PaginationI) => {
  const response = await api.get(`/api/v1/users`, {
    params: {
      ...pagination,
    },
    headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
  });
  return response.data;
};
