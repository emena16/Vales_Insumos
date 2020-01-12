from fpdf import FPDF
import datetime
#Obtenemos la fecha
x = datetime.datetime.now()
#Creamos el objeto pdf que es quien se encargara de dibujar el PDF
pdf = FPDF()
#Solicitamos al usuariop
print("*** Generador de Vales de Insumos Tabarato, SA de CV ***")
print("por JEMD GitHub: emena16 v1.1")
print("")
folio_inicial = int(input("Ingresa folio inicial: "))
folio = folio_inicial
paginas = int(input("Numero de paginas necesarias: "))
#igualamos a 1 pagina en caso de que no se haya ingresado el numero de paginas.
if paginas < 1:
	paginas = 1
pdf.set_font('Arial', 'B', 9)
i= k = 0
#Coordenadas de los folios y las fechas en el documento
pos_x = [81.9,198.5]
pos_y = [11,61.2,128,179.5,229]
#iteramos segun las filas solicitadas
while i != paginas:
    pdf.add_page()
    pdf.image('vale_inventarios.jpg',4,7,205,265)
    for x in range(len(pos_x)):
        for y in range(len(pos_y)):
            pdf.set_xy(pos_x[x],pos_y[y])
            #print(repr(pos_x[x])+"-"+repr(pos_y[y]))
            pdf.multi_cell(40, 10, repr(folio))
            folio = folio+1
    i=i+1
pdf.output('Vales_Insumos.pdf', 'F')
#Escribimos en fichero los resultados de la generacion 
file = open('Salida_Vales.txt','a')
file.write('Se han generado '+repr(paginas)+' paginas con folio de: '+repr(folio_inicial)+' a '+repr(folio-1)+' \n')
file.write('\n')
file.close()
