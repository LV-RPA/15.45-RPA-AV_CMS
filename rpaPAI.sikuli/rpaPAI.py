import os 
import glob

user_CMS = "MPAUCA10"
pass_CMS = "Miguel02201"
user_inguz = "74590179"
pass_inguz = "jarvis"
link_inguz = "http://www.anovo.pe/inguz"
link_carga = "http://www.anovo.pe/inguz/formRutinas/frmCargarOrdenes.aspx"
pai = r'\\10.10.1.250\desarrollo\CargaInguz_Otros\PAI'
delete_files = r'\\10.10.1.250\desarrollo\CargaInguz_Otros\PAI\*'

print("cerrar procesos")
os.system('taskkill /f /im cms.exe')
os.system('taskkill /f /im te_envot.exe')
os.system('taskkill /f /im te_banpai.exe')
os.system('taskkill /f /im te_manot.exe')
os.system('taskkill /f /im firefox.exe')
sleep(2)

print("Eliminar Archivos")
files = glob.glob(delete_files) 
for f in files:
    os.remove(f)
sleep(2)

print("Abrir CMS")
App.open("C:\\Gescab\\cms.exe")
sleep(2)

print("Esperar CMS")
wait(Pattern("1557418414969.png").similar(0.80),240)

print("modulo encontrado")
paste(Pattern("1557418673300.png").targetOffset(-24,3), user_CMS)
sleep(2)
type(Key.TAB)
sleep(2)
paste(pass_CMS)
sleep(2)
type(Key.ENTER)
sleep(2)
wait(Pattern("1555191558075.png").similar(0.80),240)
sleep(2)
click("1555191572231.png")
sleep(2)
click("1555191587121.png")
sleep(2)
click(Pattern("1555191605081.png").targetOffset(6,11))
sleep(2)
click("1555191630786.png")
sleep(2)
wait(Pattern("1555191646245.png").similar(0.80),1800)
sleep(2)

print("listo, cable mágico")
def cambiarusuario():
    type("u",KEY_ALT)
    sleep(1)
    type("s",KEY_ALT)
    sleep(1)

cambiarusuario()
cambiarusuario()
cambiarusuario()
cambiarusuario()
cambiarusuario()

print("abrir modulo")
doubleClick(Pattern("1555191664304.png").targetOffset(-68,2))
sleep(10)
click(Pattern("1555191664304.png").targetOffset(-68,2))
sleep(2)
wait("1555191780299.png")
sleep(2)

print("salio en proceso")
click(Pattern("1555191795518.png").targetOffset(-59,0))
sleep(2)

print("Inicio exportar PAI")
doubleClick(Pattern("1558390212483.png").targetOffset(-96,1))
sleep(2)
wait(Pattern("1558390280139.png").similar(0.80),240)
sleep(2)
print("Comenzamos exportar")
click(Pattern("1558390431086.png").targetOffset(0,1))
sleep(2)
wait(Pattern("1558390484350.png").similar(0.80),180)
sleep(2)

print("Filtramos Pendientes")
click(Pattern("1561655014818.png").similar(0.80).targetOffset(203,-24))
sleep(2)
click(Pattern("1558391707216.png").targetOffset(-1,8))
sleep(2)
click("1558391624735.png")
sleep(2)
type(Key.ENTER)
sleep(2)
wait(Pattern("1558391919980.png").similar(0.80),1800)

print("Guardar el archivo PAI")
sleep(2)
click(Pattern("1558391979490.png").targetOffset(-1,1))
sleep(2)
wait(Pattern("1558392053943.png").similar(0.80),3600)
sleep(2)
click(Pattern("1558392053943.png").targetOffset(48,43))
sleep(5)
click(Pattern("1558392201575.png").targetOffset(-1,0))
sleep(2)
click(Pattern("1558392234856.png").targetOffset(120,1))
sleep(2)
print("selecciona la carpeta")

click(Pattern("1560611428725.png").targetOffset(-55,1))
sleep(2)
doubleClick("1558392451920.png")
sleep(2)
type(Pattern("1558392511334.png").targetOffset(29,2), "devoluciones_pai")
sleep(2)
type(Key.ENTER)
sleep(2)

print("Guardar archivo pendiente_pai")
sleep(15)
click(Pattern("1581347862360.png").targetOffset(13,2))
sleep(3)

#------DESCARGA DE LLAMADAS PAI
click(Pattern("1558390431086-1.png").targetOffset(0,1))
sleep(2)
wait(Pattern("1558390484350-1.png").similar(0.80),220)
sleep(2)

print("Filtramos Pendientes")
click(Pattern("1561655014818-1.png").similar(0.80).targetOffset(203,-24))
sleep(2)
click(Pattern("1558391707216-1.png").targetOffset(-1,8))
sleep(2)
click(Pattern("1580922950611.png").targetOffset(-27,0))
sleep(2)
type(Key.ENTER)
sleep(2)
wait(Pattern("1558391919980-1.png").similar(0.80),1800)

print("Guardar el archivo PAI")
sleep(2)
click(Pattern("1558391979490-1.png").targetOffset(-1,1))
sleep(2)
wait(Pattern("1558392053943-1.png").similar(0.80),120)
sleep(2)
click(Pattern("1558392053943-1.png").targetOffset(48,43))
sleep(5)
click(Pattern("1558392201575-1.png").targetOffset(-1,0))
sleep(2)
click(Pattern("1558392234856-1.png").targetOffset(120,1))
sleep(2)
print("selecciona la carpeta")

click(Pattern("1560611428725-1.png").targetOffset(-55,1))
sleep(2)
doubleClick("1558392451920-1.png")
sleep(2)
type(Pattern("1558392511334-1.png").targetOffset(29,2), "pai_llamadas")
sleep(2)
type(Key.ENTER)
sleep(2)

print("Guardar archivo llamadas_pai")
sleep(15)
click(Pattern("1558392684034-1.png").targetOffset(12,-1))

print("Cerrar CMS")
sleep(3)
click(Pattern("1558394215166.png").targetOffset(-1,1))
sleep(2)
wait(Pattern("1558394264145.png").similar(0.80),240)
sleep(2)
click(Pattern("1558394264145.png").targetOffset(23,55))

print("fin de la tarea exportacion")
sleep(5)

#//******************FIREFOX******************\\#
App.open("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
sleep(15)

print("iniciar sesion")
paste(Pattern("1564075651269.png").targetOffset(-224,-12), user_inguz)
sleep(5)
type(Key.TAB)
sleep(3)
paste(pass_inguz)
sleep(5)
type(Key.ENTER)
sleep(2)
wait("1571943619402.png",120)
sleep(2)

print("ingresar al link de carga")
type("l",KEY_CTRL)
sleep(2)
paste(link_carga)
sleep(2)
type(Key.ENTER)
sleep(5)
click(Pattern("1559077079121-2.png").targetOffset(23,0))
sleep(2)
click(Pattern("1559149471473-1.png").targetOffset(-33,15))
sleep(3)

print("buscar el archivo")
type("l",KEY_CTRL)
sleep(2)
paste(pai)
sleep(2)
type(Key.ENTER)
sleep(2)
click(Pattern("1559150237248-1.png").targetOffset(-64,1))
type(Key.ENTER)
sleep(2)
click(Pattern("1563232770542.png").targetOffset(333,-1))
sleep(2)
wait(Pattern("1563232909280.png").similar(0.80),1800)
sleep(2)

print("ingresar al link de carga")
type("l",KEY_CTRL)
sleep(2)
paste(link_carga)
sleep(2)
type(Key.ENTER)
sleep(5)
click(Pattern("1559077079121-3.png").targetOffset(23,0))
sleep(2)
click(Pattern("1559149471473-2.png").targetOffset(-33,15))
sleep(3)

print("buscar el archivo")
type("l",KEY_CTRL)
sleep(2)
paste(pai)
sleep(2)
type(Key.ENTER)
sleep(2)
click(Pattern("1580946842435.png").targetOffset(-50,-1))
sleep(2)
type(Key.ENTER)
sleep(2)
click(Pattern("1581348366823.png").similar(0.80).targetOffset(340,19))
sleep(2)
wait(Pattern("1563232909280-1.png").similar(0.80),1800)
sleep(2)

print("fin de la carga")
type("w",KEY_CTRL)
print("FIN RPA")