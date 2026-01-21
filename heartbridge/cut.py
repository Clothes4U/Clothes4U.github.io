import PythonMagick
from PyPDF2 import PdfFileReader

##reader = PdfFileReader(open(pdffile, "rb"))
##npage = reader.getNumPages()
for i in range(1,52):
    if i<10:i0='0'+str(i)
    else:i0=str(i)
    pdffile = 'HB_'

    im = PythonMagick.Image(pdffile +i0+'.pdf[0]')
    im.density("300")
    im.magick("JPG")
    im.resize("1000x1000")
    im.write('HB_'+i0+ '.jpg')
