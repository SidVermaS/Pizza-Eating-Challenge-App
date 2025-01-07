import { GenderI } from '@/consts/users';
import { PaginationI } from './common';

export type UserI = {
  id: string;
  name: string;
  age: number;
  gender: GenderI;
  coins: number;
  consumed_count: number;
  rank: number;
};
export type FetchUsersParamsI = PaginationI & {
  sort_by?: 'rank';
};
