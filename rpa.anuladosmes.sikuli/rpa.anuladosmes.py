import datetime
desde = datetime.datetime.now() + datetime.timedelta(days=-29)
hasta = datetime.datetime.now()
user_CMS = "MPAUCA10"
pass_CMS = "Miguel0719"
user_inguz = "74590179"
pass_inguz = "jarvis"
link_inguz = "http://www.anovo.pe/inguz"
link_carga = "http://www.anovo.pe/inguz/formRutinas/frmCargarOrdenes.aspx"
anulados = r'\\10.10.1.250\desarrollo\CargaInguz_Otros\Anulados'
delete_files = r'del /S /Q \\10.10.1.250\desarrollo\CargaInguz_Otros\Anulados\*'
print(desde)
print(hasta)

print("cerrar procesos")
type("r",KeyModifier.WIN)
sleep(2)
type("cmd")
type(Key.ENTER)
sleep(2)
paste(r'taskkill /F /IM cms.exe')
type(Key.ENTER)
sleep(1)
paste(r'taskkill /F /IM te_envot.exe')
type(Key.ENTER)
sleep(1)
paste(r'taskkill /F /IM te_manot.exe')
type(Key.ENTER)
sleep(1)
paste(r'taskkill /F /IM te_rreot.exe')
type(Key.ENTER)
sleep(1)
paste(r'taskkill /F /IM te_alav.exe')
type(Key.ENTER)
sleep(1)
paste(r'taskkill /F /IM firefox.exe')
type(Key.ENTER)
sleep(1)
type("exit")
type(Key.ENTER)
sleep(1)

print("Eliminar Archivos")
type("r",KeyModifier.WIN)
sleep(2)
type("cmd")
type(Key.ENTER)
sleep(2)
paste(delete_files)
type(Key.ENTER)
sleep(3)
type("exit")
type(Key.ENTER)
sleep(1)

print("Abrir CMS")
type("r",KeyModifier.WIN)
sleep(2)
paste(r'C:\Gescab\cms.exe')
sleep(1)
type(Key.ENTER)
sleep(2)

print("Esperar CMS")
wait(Pattern("1557418414969.png").similar(0.80),3600)

print("modulo encontrado")
paste("1557418673300.png", user_CMS)
paste("1557418022576.png", pass_CMS)
type(Key.ENTER)
sleep(1)
wait(Pattern("1555191558075.png").similar(0.80),3600)
click("1555191572231.png")
click("1555191587121.png")
click(Pattern("1555191605081.png").targetOffset(6,11))
click("1555191630786.png")
sleep(2)
wait(Pattern("1555191646245.png").similar(0.80),3600)
sleep(2)

print("listo, cable mágico")
type("u",KEY_ALT)
sleep(1)
type("s",KEY_ALT)
sleep(1)
type("u",KEY_ALT)
sleep(1)
type("s",KEY_ALT)
sleep(1)
type("u",KEY_ALT)
sleep(1)
type("s",KEY_ALT)
sleep(1)
type("u",KEY_ALT)
sleep(1)
type("s",KEY_ALT)
sleep(1)
type("u",KEY_ALT)
sleep(1)
type("s",KEY_ALT)
sleep(10)

print("abrir modulo")
doubleClick(Pattern("1555191664304.png").targetOffset(-68,2))
sleep(10)
click(Pattern("1555191664304.png").targetOffset(-68,2))
wait("1560621237856.png")
sleep(2)
click(Pattern("1560621258261.png").targetOffset(-55,1))
sleep(2)
click(Pattern("1560621306279.png").targetOffset(-83,1))
sleep(2)
doubleClick(Pattern("1560621342992.png").targetOffset(-109,1))
sleep(2)

print("inicio exportar anulados")
wait(Pattern("1560621517474.png").similar(0.80),3600)
click(Pattern("1560621517474.png").similar(0.80).targetOffset(-16,16))
sleep(1)
click(Pattern("1560621620815.png").targetOffset(-41,8))
sleep(1)
click(Pattern("1560621666277.png").similar(0.80).targetOffset(-35,1))
sleep(1)
click(Pattern("1560621712385.png").targetOffset(19,9))

print("seleccionar contrata anovo")
for step in range(12):
    click(Pattern("1560622333544.png").targetOffset(-33,27))
   
click(Pattern("1560622460676.png").targetOffset(-20,1))
sleep(1)
type(Pattern("1560621945672.png").targetOffset(54,4), desde.strftime("%d%m"))
type(Pattern("1560622009514.png").targetOffset(53,7), hasta.strftime("%d%m"))
sleep(2)

print("exportar anulados")
click(Pattern("1560622638932.png").targetOffset(-4,1))
sleep(2)
wait(Pattern("1560623979775.png").similar(0.80),3600)
sleep(1)
click(Pattern("1560624020922.png").targetOffset(5,-11))
sleep(1)
click(Pattern("1561413763631.png").targetOffset(-15,1))
sleep(1)
click(Pattern("1561413793566.png").targetOffset(-54,1))
sleep(1)
doubleClick(Pattern("1560624189302.png").targetOffset(-29,2))
sleep(2)

print("guardar archivo")
type(Pattern("1560624255197.png").targetOffset(37,1), "anulados")
sleep(1)
type(Key.ENTER)
wait(Pattern("1560624436538.png").similar(0.80),3600)
sleep(1)
click(Pattern("1560624436538.png").similar(0.80).targetOffset(90,55))
sleep(2)
click(Pattern("1560624551447.png").targetOffset(-3,-2))

print("Cerrar CMS")
sleep(5)
click(Pattern("1558394215166.png").targetOffset(-1,1))
wait(Pattern("1558394264145.png").similar(0.80),3600)
click(Pattern("1558394264145.png").targetOffset(23,55))
sleep(2)

#//******************FIREFOX******************\\#
print("abrir firefox")
type("r",KeyModifier.WIN)
sleep(2)
paste(r'C:\Program Files\Mozilla Firefox\firefox.exe')
sleep(1)
type(Key.ENTER)
sleep(10)

print("Pagina encontrada")
type("l",KEY_CTRL)
sleep(1)
paste(link_inguz)
sleep(1)
type(Key.ENTER)
sleep(5)

print("iniciar sesion")
paste(user_inguz)
type(Key.TAB)
paste(pass_inguz)
sleep(1)
type(Key.ENTER)
sleep(5)
type("l",KEY_CTRL)
sleep(1)

print("ingresar al link de carga")
paste(link_carga)
type(Key.ENTER)
sleep(5)
click(Pattern("1559077079121-2.png").targetOffset(23,0))
sleep(2)
click(Pattern("1560624805320.png").targetOffset(2,5))
sleep(2)
click(Pattern("1560624849005.png").similar(0.80).targetOffset(-20,-14))
sleep(2)

print("buscar el archivo")
type("l",KEY_CTRL)
sleep(1)
paste(anulados)
sleep(1)
type(Key.ENTER)
sleep(1)
click(Pattern("1560624944272.png").targetOffset(-34,1))
type(Key.ENTER)
sleep(2)
click(Pattern("1561592425007.png").targetOffset(234,3))
sleep(2)
wait(Pattern("1560625035541.png").similar(0.80),3600)
sleep(2)

print("fin de la carga")
click(Pattern("1560625059578.png").targetOffset(96,1))
sleep(3)

print("cerrar procesos")
type("r",KeyModifier.WIN)
sleep(2)
type("cmd")
type(Key.ENTER)
sleep(2)
paste(r'taskkill /F /IM cms.exe')
type(Key.ENTER)
sleep(1)
paste(r'taskkill /F /IM te_envot.exe')
type(Key.ENTER)
sleep(1)
paste(r'taskkill /F /IM te_banpai.exe')
type(Key.ENTER)
sleep(1)
paste(r'taskkill /F /IM te_rreot.exe')
type(Key.ENTER)
sleep(1)
paste(r'taskkill /F /IM firefox.exe')
type(Key.ENTER)
sleep(1)
type("exit")
type(Key.ENTER)
sleep(1)

print("Eliminar Archivos")
type("r",KeyModifier.WIN)
sleep(2)
type("cmd")
type(Key.ENTER)
sleep(2)
paste(delete_files)
sleep(1)
type(Key.ENTER)
sleep(3)
type("exit")
type(Key.ENTER)
sleep(1)
print("Fin de la Carga")