import re, glob, os, nbformat as nbf
judul = {
 '01':'Program 1 - Suhu ruangan dengan AC dinyalakan jam 2-7 (ODEINT)','02':'Program 2 - AC dikendalikan termostat 24-26 C (ODEINT)',
 '03':'Program 3 - Contoh 1: peluruhan selisih suhu (ODEINT)','04':'Program 4 - Contoh 1 (GEKKO)',
 '05':'Program 5 - Contoh 2: variasi k dengan args (ODEINT)','06':'Program 6 - Contoh 2 (GEKKO)',
 '07':'Program 7 - Contoh 3: input step AC (ODEINT)','08':'Program 8 - Contoh 3 (GEKKO)',
 '09':'Program 9 - Contoh 4: dua persamaan ekivalen (ODEINT)','10':'Program 10 - Contoh 4 (GEKKO)',
 '11':'Program 11 - Contoh 5: model 2 state udara-dinding (ODEINT)','12':'Program 12 - Contoh 5 (GEKKO)',
 '13':'Program 13 - Studi kasus: setpoint termostat dan energi AC (ODEINT)','14':'Program 14 - Contoh Pemodelan: AC jam 2-7 (GEKKO)',
 '15':'Program 15 - Contoh Pemodelan: variasi koefisien AC k (ODEINT)'}
nb = nbf.v4.new_notebook(); c = []
c.append(nbf.v4.new_markdown_cell("# Dinamic System Modelling: Pemodelan dan Simulasi Suhu Ruangan dengan AC\n**Nama:** Soni Moch Leviansyah  \n**NIM:** 301240030  \n**Mata kuliah:** Pemodelan Sistem Dinamik\n\nModel utama: $\\frac{dT}{dt}=\\frac{T_{out}-T}{\\tau}-k\\,u(t)$"))
c.append(nbf.v4.new_markdown_cell("## 0. Instalasi library"))
c.append(nbf.v4.new_code_cell("!pip install gekko -q"))
for f in sorted(glob.glob('src/program*.py')):
    n = os.path.basename(f)[7:9]
    if n == '00': continue
    c.append(nbf.v4.new_markdown_cell('## ' + judul[n]))
    c.append(nbf.v4.new_code_cell(open(f).read().replace("GEKKO(remote=False)", "GEKKO(remote=False)")))
c.append(nbf.v4.new_markdown_cell("## Perhitungan manual (Euler) vs analitik vs ODEINT"))
c.append(nbf.v4.new_code_cell(open('src/hitung_manual_euler.py').read()))
nb.cells = c
nb.metadata = {"colab": {"provenance": []}, "kernelspec": {"name": "python3", "display_name": "Python 3"}, "language_info": {"name": "python"}}
nbf.write(nb, 'notebook/Pemodelan_AC_Soni_301240030.ipynb')
