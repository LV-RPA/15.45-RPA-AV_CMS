import os 
import glob

link_toa = ("https://login.toadirect.com/telefonica-pe.toadirect.com")
user_toa = ("AN0621")
pass_toa = ("Lizandro01201")
link_inguz = "http://www.anovo.pe/inguz"
link_carga = "http://www.anovo.pe/inguz/formRutinas/frmCargarOrdenes.aspx"
user_inguz = "74590179"
pass_inguz = "jarvis"
ruta_toa = r'\\10.10.1.250\desarrollo\CargaInguz_Otros\TOA'
delete_files = r'\\10.10.1.250\Desarrollo\CargaInguz_Otros\TOA\*'

print("Eliminar Archivos")
files = glob.glob(delete_files) 
for f in files:
    os.remove(f)
sleep(2)

print("cerrar procesos")
os.system('taskkill /f /im cms.exe')
os.system('taskkill /f /im te_envot.exe')
os.system('taskkill /f /im te_banpai.exe')
os.system('taskkill /f /im te_manot.exe')
os.system('taskkill /f /im firefox.exe')
os.system('taskkill /f /im excel.exe')
sleep(2)
if exists("1560368012869.png"):
   (click(Pattern("1560368012869.png").targetOffset(45,0)))
   sleep(2)

try:
    #/*****************************FIREFOX******************************************/
    App.open("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    sleep(15)
    
    print("Pagina encontrada")
    type("l",KEY_CTRL)
    sleep(2)
    paste(link_toa)
    sleep(2)
    type(Key.ENTER)
    sleep(15)
    
    print("recargar pagina")
    type("l",KEY_CTRL)
    sleep(2)
    type(Key.ENTER)
    sleep(5)
    wait("1571959675157.png",240)
    sleep(2)
    
    print("login")
    paste(user_toa)
    sleep(2)
    type(Key.TAB)
    sleep(2)
    paste(pass_toa)
    sleep(2)
    type(Key.ENTER)
    sleep(3)
    
    print("ingresar al toa")    
    if exists(Pattern("1559682268838-2.png").similar(0.80)):
        paste(pass_toa)
        (click(Pattern("1559682268838-2.png").targetOffset(-174,14)))
        sleep(1)
        type(Key.ENTER)
        sleep(1)
    
    print("Ingresamos al TOA")
    type("l",KEY_CTRL)
    sleep(2)
    type(Key.ENTER)
    sleep(10)
    click(Pattern("1560186803626.png").targetOffset(-9,-1))
    click(Pattern("1560186899505.png").targetOffset(-25,0))
    type(Key.ENTER)
    sleep(10)
    
    #//*****************************MIGRACIONES*******************    
    print("exportar migraciones")
    wait(Pattern("1559935548941.png").similar(0.80),3600)
    sleep(2)
    click(Pattern("1560183675388.png").targetOffset(-14,1))
    sleep(10)
    
    print("exportamos base")
    click(Pattern("1559682937404-2.png").targetOffset(10,1))
    click(Pattern("1559682968711-2.png").targetOffset(-14,-1))
    wait(Pattern("1559934907857.png").similar(0.80),3600)
    sleep(3)
    type("Actividades-MIGRACIONES")
    sleep(1)
    type("l",KEY_CTRL)
    paste(ruta_toa)
    sleep(1)
    type(Key.ENTER)
    sleep(3)
    click(Pattern("1559935273274.png").targetOffset(-2,2))
    sleep(2)
    if exists (Pattern("1561588906120.png").targetOffset(-35,-2)):
        click(Pattern("1561588906120.png").targetOffset(-38,0))
        sleep(3)
    
    print("filtrar archivo")
    wait(Pattern(Pattern("1559767268582.png").targetOffset(-16,3)).similar(0.8),3600)
    sleep(5)
    click(Pattern("1560193408477.png").targetOffset(-15,-1))
    sleep(2)
    click(Pattern("1560193544087.png").targetOffset(-12,0))
    wait(Pattern("1560193702476.png").similar(0.80),3600)
    sleep(2)
    click(Pattern("1559767572444.png").targetOffset(14,24))
    sleep(1)
    click(Pattern("1559767628786.png").targetOffset(-24,-3))
    sleep(2)
    
    print("guardar y cerrar")
    type("g",KEY_CTRL)
    sleep(2)
    click(Pattern("1559767751527.png").targetOffset(44,0))
    sleep(2)
    
    print("abrir inguz")
    click(Pattern("1559683678668-1.png").targetOffset(0,-1))
    sleep(3)
    type("l",KEY_CTRL)
    paste(link_inguz)
    sleep(1)
    type(Key.ENTER)
    sleep(10)
    paste(Pattern("1564075651269.png").targetOffset(-224,-12), user_inguz)
    sleep(5)
    type(Key.TAB)
    sleep(3)
    paste(pass_inguz)
    sleep(5)
    type(Key.ENTER)
    sleep(2)
    wait("1571943619402.png",60)
    sleep(2)
    
    print("ruta carga")
    type("l",KEY_CTRL)
    paste(link_carga)
    sleep(1)
    type(Key.ENTER)
    sleep(2)
    wait(Pattern("1559684141878-4.png").similar(0.80),3600)
    sleep(2)
    
    print("buscar modulo")
    click(Pattern("1559684206138-4.png").targetOffset(28,0))
    click(Pattern("1560194226100.png").targetOffset(4,5))
    sleep(2)
    click(Pattern("1563575809646.png").targetOffset(-162,49))
    wait(Pattern("1559684918833-3.png").similar(0.80),3600)
    
    print("seleccionar archivo")
    type("l",KEY_CTRL)
    paste(ruta_toa)
    type(Key.ENTER)
    sleep(1)
    click(Pattern("1560194494388.png").targetOffset(-12,-1))
    type(Key.ENTER)
    sleep(2)
    click(Pattern("1562889197611.png").targetOffset(293,7))
    sleep(2)
    wait(Pattern("1559685225434-1.png").similar(0.80),1800)
    sleep(5)
    click(Pattern("1560199075621.png").targetOffset(95,-1))
    
    print("fin de la Toa Migraciones")
    sleep(2)
    
    #//*****************************RUTINAS*************************
    print("Exportar Toa Rutinas")
    click(Pattern("1560199438004.png").targetOffset(-2,0))
    sleep(10)
    
    print("exportamos base")
    click(Pattern("1559682937404-3.png").targetOffset(10,1))
    click(Pattern("1559682968711-3.png").targetOffset(-14,-1))
    wait(Pattern("1559934907857-1.png").similar(0.80),3600)
    sleep(3)
    type("Actividades-RUTINAS")
    sleep(1)
    type("l",KEY_CTRL)
    paste(ruta_toa)
    sleep(1)
    type(Key.ENTER)
    sleep(3)
    click(Pattern("1559935273274-1.png").targetOffset(-2,2))
    sleep(2)
    if exists (Pattern("1561588906120.png").targetOffset(-35,-2)):
        click(Pattern("1561588906120.png").targetOffset(-38,0))
        sleep(3)
    
    print("filtrar archivo")
    wait(Pattern(Pattern("1559767268582-1.png").targetOffset(-16,3)).similar(0.8),3600)
    sleep(5)
    click(Pattern("1560193408477-1.png").targetOffset(-15,-1))
    sleep(2)
    click(Pattern("1560200284769.png").targetOffset(-4,3))
    wait(Pattern("1560200340233.png").similar(0.80),3600)
    sleep(2)
    click(Pattern("1559767572444-1.png").targetOffset(14,24))
    sleep(1)
    click(Pattern("1559767628786-1.png").targetOffset(-24,-3))
    sleep(2)
    
    print("guardar y cerrar")
    type("g",KEY_CTRL)
    sleep(2)
    click(Pattern("1559767751527-1.png").targetOffset(44,0))
    sleep(2)
    
    print("abrir inguz")
    click(Pattern("1559683678668-2.png").targetOffset(0,-1))
    
    sleep(3)
    type("l",KEY_CTRL)
    paste(link_inguz)
    sleep(1)
    type(Key.ENTER)
    sleep(10)
    paste(Pattern("1564075651269.png").targetOffset(-224,-12), user_inguz)
    sleep(5)
    type(Key.TAB)
    sleep(3)
    paste(pass_inguz)
    sleep(5)
    type(Key.ENTER)
    sleep(2)
    wait("1571943619402.png",60)
    sleep(2)
    
    print("buscar la ruta")
    type("l",KEY_CTRL)
    paste(link_carga)
    type(Key.ENTER)
    sleep(5)
    
    print("buscar modulo")
    click(Pattern("1559684206138-5.png").targetOffset(28,0))
    click(Pattern("1560194226100-1.png").targetOffset(4,5))
    sleep(2)
    click(Pattern("1563575809646.png").targetOffset(-162,49))
    wait(Pattern("1559684918833-4.png").similar(0.80),3600)
    
    print("seleccionar archivo")
    type("l",KEY_CTRL)
    paste(ruta_toa)
    type(Key.ENTER)
    sleep(1)
    click(Pattern("1560200560448.png").targetOffset(-9,0))
    type(Key.ENTER)
    sleep(2)
    click(Pattern("1562889147748.png").targetOffset(287,2))
    
    print("fin de la carga Rutinas")
    sleep(3)
    wait(Pattern("1559685225434-2.png").similar(0.80),3600)
    sleep(6)
    click(Pattern("1560199075621-1.png").targetOffset(95,-1))
    sleep(2)
    
    #//*****************************AREQUIPA**********************
    print("Exportar Toa arequipa")
    click(Pattern("1560282800857-1.png").targetOffset(0,-1))
    sleep(30)
    
    print("exportamos base")
    click(Pattern("1559682937404-4.png").targetOffset(10,1))
    click(Pattern("1559682968711-4.png").targetOffset(-14,-1))
    wait(Pattern("1559934907857-2.png").similar(0.80),3600)
    sleep(3)
    type("Actividades-AREQUIPA")
    sleep(1)
    type("l",KEY_CTRL)
    paste(ruta_toa)
    sleep(1)
    type(Key.ENTER)
    sleep(3)
    click(Pattern("1559935273274-2.png").targetOffset(-2,2))
    sleep(2)
    if exists (Pattern("1561588906120.png").targetOffset(-35,-2)):
        click(Pattern("1561588906120.png").targetOffset(-38,0))
        sleep(3)
    
    print("filtrar archivo")
    wait(Pattern(Pattern("1559767268582-2.png").targetOffset(-16,3)).similar(0.8),3600)
    sleep(5)
    click(Pattern("1560193408477-2.png").targetOffset(-15,-1))
    sleep(2)
    click(Pattern("1560283057540.png").targetOffset(-5,0))
    wait(Pattern("1560283109844.png").similar(0.80),3600)
    sleep(2)
    click(Pattern("1559767572444-2.png").targetOffset(14,24))
    sleep(1)
    click(Pattern("1559767628786-2.png").targetOffset(-24,-3))
    sleep(2)
    
    print("guardar y cerrar")
    type("g",KEY_CTRL)
    sleep(1)
    click(Pattern("1559767751527-2.png").targetOffset(44,0))
    sleep(2)
    
    print("abrir inguz")
    click(Pattern("1559683678668-3.png").targetOffset(0,-1))
    sleep(3)
    type("l",KEY_CTRL)
    paste(link_inguz)
    sleep(1)
    type(Key.ENTER)
    sleep(10)
    paste(Pattern("1564075651269.png").targetOffset(-224,-12), user_inguz)
    sleep(5)
    type(Key.TAB)
    sleep(3)
    paste(pass_inguz)
    sleep(5)
    type(Key.ENTER)
    sleep(2)
    wait("1571943619402.png",60)
    sleep(2)
    
    print("buscar la ruta")
    type("l",KEY_CTRL)
    paste(link_carga)
    type(Key.ENTER)
    sleep(5)
    
    print("buscar modulo")
    click(Pattern("1559684206138-6.png").targetOffset(28,0))
    click(Pattern("1560194226100-2.png").targetOffset(4,5))
    sleep(2)
    click(Pattern("1563575809646.png").targetOffset(-162,49))
    wait(Pattern("1559684918833-5.png").similar(0.80),3600)
    
    print("seleccionar archivo")
    type("l",KEY_CTRL)
    paste(ruta_toa)
    type(Key.ENTER)
    sleep(1)
    click(Pattern("1560283288135.png").targetOffset(-3,2))
    type(Key.ENTER)
    sleep(2)
    click(Pattern("1562889270432.png").targetOffset(292,4))
    
    print("fin de la carga arequipa")
    sleep(2)
    wait(Pattern("1559685225434-3.png").similar(0.80),3600)
    sleep(5)
    click(Pattern("1560199075621-2.png").targetOffset(95,-1))
    sleep(2)
    
    print("cerrar firefox")
    type("w",KEY_CTRL)
    sleep(2)
    type("w",KEY_CTRL)
    sleep(2)
    
    print("fin de la tarea")

except:
    sleep(2)
    type("w",KEY_CTRL)
    print("cerrar procesos")
    os.system('taskkill /f /im cms.exe')
    os.system('taskkill /f /im te_envot.exe')
    os.system('taskkill /f /im te_banpai.exe')
    os.system('taskkill /f /im te_manot.exe')
    os.system('taskkill /f /im firefox.exe')
    os.system('taskkill /f /im excel.exe')
    sleep(2)
    if exists("1560368012869.png"):
       (click(Pattern("1560368012869.png").targetOffset(45,0)))
       sleep(2)