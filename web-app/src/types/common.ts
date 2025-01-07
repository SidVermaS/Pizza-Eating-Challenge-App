export type StrVoidFnI = (id: string) => void;

export type PaginationI = {
  page: number;
  per_page: number;
};
export type TablePaginationI = PaginationI & {
  total: number;
  pages: number;
  current_page: number;
  per_page: number;
};
export type TablePaginationDataI<T> = TablePaginationI & {
  data: T;
};
export type StrClassI ={
  text:string;
  className: string
}