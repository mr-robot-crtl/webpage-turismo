def importe_total_carro(request):
    total=0
    #ver si el usuario esta auntenticado
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total=total+float(value["precio"])
    else:
        total="Debes hacer login :v"
    return {"importe_total_carro":total}