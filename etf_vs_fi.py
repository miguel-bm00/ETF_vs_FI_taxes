def calcular_patrimonio(capital_inicial, aportacion_mensual, rentabilidad_anual,
                         comision_anual, impuesto_plusvalias, periodo_inversion,exencion_fiscal=False):
    patrimonio = capital_inicial
    total_aportado = capital_inicial
    for i in range(periodo_inversion):
        patrimonio = patrimonio*(1 + rentabilidad_anual - comision_anual)
        print("año ",i, " | capital: ",patrimonio)
        patrimonio += aportacion_mensual* 12
        total_aportado += aportacion_mensual * 12
        if not exencion_fiscal:
            if patrimonio > total_aportado:
                retencion = impuesto_plusvalias * (patrimonio - total_aportado)
                total_aportado += patrimonio - total_aportado - retencion # Actualizamos el total aportado con la retención
                patrimonio -= retencion
        aportacion_mensual *= 1.02 # Aumento de la aportación mensual en un 2% anual

    if exencion_fiscal:
        patrimonio -= (patrimonio - total_aportado) * (impuesto_plusvalias)

    print(patrimonio, total_aportado)
    return patrimonio

def start():
    capital_inicial = 10_000
    aportacion_mensual = 200
    rentabilidad_anual = 0.065
    tipo_efectivo_impuesto = 0.21
    años_inversion = 25

    comision_etf = 0.0015
    # Escenario A - fondo inversión
    patrimonio_A = calcular_patrimonio(capital_inicial, aportacion_mensual, rentabilidad_anual,
                                        comision_etf*3, tipo_efectivo_impuesto, años_inversion, True)

    # Escenario B - etf
    patrimonio_B = calcular_patrimonio(capital_inicial, aportacion_mensual*(1-0.0015), rentabilidad_anual,
                                        comision_etf,tipo_efectivo_impuesto, años_inversion)

    print("Escenario A - FONDOS INVERSION")
    # visualizar cifra patrimonio final separado cada 3 cifras y con 2 decimales
    print("{:,.2f}".format(patrimonio_A))
    print("Escenario B - ETFS")
    # visualizar cifra patrimonio final separado cada 3 cifras y con 2 decimales
    print("{:,.2f}".format(patrimonio_B))

    


if __name__ == "__main__":
    start()