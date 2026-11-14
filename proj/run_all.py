"""Menjalankan semua program, menyimpan grafik ke folder figures/ (dipakai pada laporan)."""
import glob, os, sys, io, contextlib
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
os.makedirs('figures', exist_ok=True)
for f in sorted(glob.glob('src/program*.py')):
    name = os.path.basename(f)[:-3]
    code = open(f).read()
    buf = io.StringIO()
    def show(*a, **k):
        plt.savefig('figures/%s.png' % name, dpi=150, bbox_inches='tight'); plt.close('all')
    plt.show = show
    with contextlib.redirect_stdout(buf):
        exec(compile(code, f, 'exec'), {'__name__': '__main__'})
    print('==', name, '->', buf.getvalue().strip().replace('\n', ' | '))
