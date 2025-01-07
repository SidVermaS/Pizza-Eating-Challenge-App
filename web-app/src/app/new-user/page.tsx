import CardForm from '@/components/CardForm';
import Title from '@/components/Title';
import type { Metadata } from 'next';
import React from 'react';
import useNewUserPage from './useNewUserPage';

export const metadata: Metadata = {
  title: 'New User',
  description: 'New user',
};
const NewUserPage = () => {
  // const {} = useNewUserPage();
  return (
    <>
      <Title text="Add User 👤" />
      <CardForm />
    </>
  );
};

export default NewUserPage;
