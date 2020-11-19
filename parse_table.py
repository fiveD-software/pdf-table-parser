
import os
import camelot
import pandas as pd
import matplotlib.pyplot as plt


def lattice(pdf, dv=False, dp=0, dk='joint',
            pages='all', password=None,
            areas=None, line_scale=15,
            copy_txt=None, shift_txt=['l', 't'],
            line_tol=3, joint_tol=3,
            strip_txt='\n'):

    # Read the PDF file
    tables = camelot.read_pdf(filepath=pdf, pages=pages, password=password,
                              flavor='lattice',
                              table_areas=areas, line_scale=line_scale,
                              copy_txt=copy_txt, shift_text=shift_txt,
                              line_tol=line_tol, joint_tol=joint_tol,
                              strip_text=strip_txt)

    # Visual Debugging Option
    if dv:
        page = dp
        if dk in ['text', 'grid', 'contour', 'line', 'joint']:
            camelot.plot(tables[page], kind=dk)
            plt.show()

    return tables


def stream(pdf, dv=False, dp=0, dk='grid',
           pages='all', password=None,
           areas=None, regions=None,
           columns=None,
           row_tol=6, col_tol=9,
           edge_tol=50, strip_txt='\n'):

    # Read the PDF file
    tables = camelot.read_pdf(filepath=pdf, pages=pages, password=password,
                              flavor='stream',
                              table_areas=areas, table_regions=regions,
                              columns=columns,
                              row_tol=row_tol, column_tol=col_tol,
                              edge_tol=edge_tol, strip_text=strip_txt)

    # Visual Debugging Option
    if dv:
        page = dp
        if dk in ['text', 'grid', 'contour', 'textedge']:
            camelot.plot(tables[page], kind=dk)
            plt.show()

    return tables


def drop_columns(tables: camelot.core.Table, cols: list):
    for table in tables:
        for c in cols:
            if c in table.df.columns:
                del table.df[c]
            else:
                raise Exception('Invalid column label supplied - "{}"'.format(c))


def fix_whitespaces(tables: camelot.core.Table):
    for table in tables:
        for i, row in table.df.iterrows():
            for col in table.df:
                v = row[col]
                if isinstance(v, str):
                    row[col] = ' '.join(v.split())
                else:
                    pass


def simplify_single_column(tables: camelot.core.Table, col: int):
    for table in tables:
        df = []
        ov = None
        s = ''
        for i, row in table.df.iterrows():
            v = row[col]
            if v != '':
                s = ''.join([s, v, ' '])
            else:
                if ov == '':
                    continue

                df.append(s)
                s = ''

            ov = v

        if s:
            df.append(s)

        # Replaces the table's dataframe (witn a non-indexed, single column)
        table.df = pd.DataFrame(df)
