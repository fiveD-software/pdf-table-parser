
import os
import parse_table as pt

folder = 'Russia/origin/'

pdfs = ['1-enr1-01.pdf',
        '1-enr1-02.pdf',
        '1-enr1-03.pdf',
        '1-enr1-04.pdf',
        '1-enr1-05.pdf',
        '1-enr1-06.pdf',
        '1-enr1-07.pdf',
        '1-enr1-08.pdf',
        '1-enr1-09.pdf',
        '1-enr1-10.pdf',
        '1-enr1-11.pdf',
        '1-enr1-12.pdf',
        '1-enr1-13.pdf',
        '1-enr1-14.pdf',
        ]


def dual_column_area_stream(folder: str, pdf: str, pages: str, areas: list, cols: list):

    p = ''.join([folder, pdf])
    fp = os.path.abspath(p)
    tb = pt.stream(pdf=fp, dv=True, dk='contour',
                   pages=pages,
                   areas=areas,
                   columns=cols,
                   edge_tol=5000
                   )

    # Fix minor format issues
    pt.drop_columns(tb, [0])
    pt.fix_whitespaces(tb)
    pt.simplify_single_column(tb, 1)

    # Output
    ep = ''.join([fp.strip('.pdf'), '.csv'])
    ep = ep.replace('origin', 'extract')
    tb.export(path=ep, f='csv')


def combo_area_lattice(folder: str, pdf: str, pages: str, areas: list):

    p = ''.join([folder, pdf])
    fp = os.path.abspath(p)
    tb = pt.lattice(pdf=fp, dv=True, dk='contour',
                    pages=pages,
                    areas=areas,
                    )

    # Fix minor format issues
    pt.fix_whitespaces(tb)

    # Output
    ep = ''.join([fp.strip('.pdf'), '.xlsx'])
    ep = ep.replace('origin', 'extract')
    tb.export(path=ep, f='excel')


def column_area_stream(folder: str, pdf: str, pages: str, areas: list, cols: list):

    p = ''.join([folder, pdf])
    fp = os.path.abspath(p)
    tb = pt.stream(pdf=fp, dv=False, dk='contour',
                   pages=pages,
                   areas=areas,
                   columns=cols,
                   )

    # Fix minor format issues
    pt.fix_whitespaces(tb)

    # Output
    ep = ''.join([fp.strip('.pdf'), '.csv'])
    ep = ep.replace('origin', 'extract')
    tb.export(path=ep, f='csv')


if __name__ == "__main__":
    scan_area = ['50, 810, 570, 50']
    # dual_column_area_stream(folder=folder, pdf='1-enr1-01.pdf', pages='all', areas=scan_area, cols=None)
    # dual_column_area_stream(folder=folder, pdf='1-enr1-02.pdf', pages='all', areas=scan_area, cols=None)
    # dual_column_area_stream(folder=folder, pdf='1-enr1-03.pdf', pages='all', areas=scan_area, cols=None)
    # combo_area_lattice(folder=folder, pdf='1-enr1-04.pdf', pages='1', areas=None)
    # dual_column_area_stream(folder=folder, pdf='1-enr1-04.pdf', pages='2', areas=scan_area, cols=None)
    # combo_area_lattice(folder=folder, pdf='1-enr1-05.pdf', pages='1', areas=None)
    # dual_column_area_stream(folder=folder, pdf='1-enr1-05.pdf', pages='2-4', areas=scan_area, cols=None)
    # dual_column_area_stream(folder=folder, pdf='1-enr1-06.pdf', pages='1-6', areas=scan_area, cols=None)
    # column_area_stream(folder=folder, pdf='1-enr1-06.pdf', pages='7-13', areas=scan_area, cols=['205, 335, 415, 490'])
    # dual_column_area_stream(folder=folder, pdf='1-enr1-07.pdf', pages='1-2', areas=scan_area, cols=None)
    # dual_column_area_stream(folder=folder, pdf='1-enr1-07.pdf', pages='3', areas=scan_area, cols=None)
    # combo_area_lattice(folder=folder, pdf='1-enr1-07.pdf', pages='3', areas=None)
    # dual_column_area_stream(folder=folder, pdf='1-enr1-07.pdf', pages='4-7', areas=scan_area, cols=['310'])
    # dual_column_area_stream(folder=folder, pdf='1-enr1-07.pdf', pages='8-12', areas=scan_area, cols=['310'])
    # column_area_stream(folder=folder, pdf='1-enr1-07.pdf', pages='13-14', areas=scan_area, cols=['310'])
