import { GenderI } from '@/consts/users';

export type UserI = {
  id: string;
  name: string;
  age: number;
  gender: GenderI;
  coins: number;
  consumed_count: number;
};
