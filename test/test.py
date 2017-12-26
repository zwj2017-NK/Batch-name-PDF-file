from pyPdf import PdfFileReader
import os

for fileName in os.listdir('/home/zhuwenjun/Documents/test/'):
    os.chdir('/home/zhuwenjun/Documents/test/')
    actfile = file(fileName, "rb")
    try:
        if fileName.lower()[-3:] != "pdf":
            continue
        input1 = PdfFileReader(actfile)
        print '  ##1', fileName, '##2', input1.getDocumentInfo().title
    except:
        print '  ##1', fileName, '##2'

    try:
        timeofpdf = input1.getDocumentInfo()['/ModDate'][2:6]
        trgtfilename = timeofpdf + '-' + input1.getDocumentInfo().title + ".pdf"
    except:
        print "\n## ERROR ## %s Title could not be extracted. PDF file may be encrypted!" % fileName
        continue

    del input1
    actfile.close()
    print 'Trying to rename from:', fileName, 'to', trgtfilename
    print '\n'

    try:
        os.rename(fileName, trgtfilename)
    except:
        print fileName,  'could not be renamed!'
        print '## ERROR ## Maybe the filename already exists or the document is already opened!'
