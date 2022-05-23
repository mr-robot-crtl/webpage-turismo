from django.shortcuts import render, HttpResponse

# Create your views here.

def places(request):
     return render(request, "Places/places.html")
def place_cat_aventu(request):
    return render(request, "cat_aventura/place_cat_aventu.html")
def lug_cat_aventu_lug_01(request):
    return render(request, "cat_aventura/lug_cat_aventu_lug_01.html")
def lug_cat_aventu_lug_02(request):
    return render(request, "cat_aventura/lug_cat_aventu_lug_02.html")
def lug_cat_aventu_lug_03(request):
    return render(request, "cat_aventura/lug_cat_aventu_lug_03.html")
#categorias de turismo
def lug_cat_turismo(request):
    return render(request, "cat_Turismo/lug_cat_turismo.html")
def lug_cat_turismo_lug_01(request):
    return render(request, "cat_Turismo/lug_cat_turismo_lug_01.html")
def lug_cat_turismo_lug_02(request):
    return render(request, "cat_Turismo/lug_cat_turismo_lug_02.html")
#categorias comida
def lug_cat_comid(request):
    return render(request, "cat_comida/lug_cat_comid.html")
def lug_cat_comid_lug_01(request):
    return render(request, "cat_comida/lug_cat_comid_lug_01.html")
def lug_cat_comid_lug_02(request):
    return render(request, "cat_comida/lug_cat_comid_lug_02.html")
#categorias seguridad
def lug_cat_seguri(request):
    return render(request, "cat_seguridad/lug_cat_seguri.html")
def lug_cat_seguri_lug_01(request):
    return render(request, "cat_seguridad/lug_cat_seguri_lug_01.html")
def lug_cat_seguri_lug_02(request):
    return render(request, "cat_seguridad/lug_cat_seguri_lug_02.html")

#categorias educacion
def lug_cat_educac(request):
    return render(request, "cat_educacion/lug_cat_educac.html")
def lug_cat_educac_lug_01(request):
    return render(request, "cat_educacion/lug_cat_educac_lug_01.html")
def lug_cat_educac_lug_02(request):
    return render(request, "cat_educacion/lug_cat_educac_lug_02.html")

#categorias salud
def lug_cat_salud(request):
    return render(request, "cat_salud/lug_cat_salud.html")
def lug_cat_salud_lug_01(request):
    return render(request, "cat_salud/lug_cat_salud_lug_01.html")
def lug_cat_salud_lug_02(request):
    return render(request, "cat_salud/lug_cat_salud_lug_02.html")

#categorias banco
def lug_cat_banco(request):
    return render(request, "cat_banco/lug_cat_banco.html")
def lug_cat_banco_lug_01(request):
    return render(request, "cat_banco/lug_cat_banco_lug_01.html")
def lug_cat_banco_lug_02(request):
    return render(request, "cat_banco/lug_cat_banco_lug_02.html")


#categorias zona recreativas
def lug_cat_zoRecre(request):
    return render(request, "cat_zonaRecreativa/lug_cat_zoRecre.html")
def lug_cat_zoRecre_lug_01(request):
    return render(request, "cat_zonaRecreativa/lug_cat_zoRecre_lug_01.html")
def lug_cat_zoRecre_lug_02(request):
    return render(request, "cat_zonaRecreativa/lug_cat_zoRecre_lug_02.html")