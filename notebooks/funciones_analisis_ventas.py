def calcular_precio_venta(venta):
    return venta['precio'] * venta['unidades']

def calcular_facturacion_total(ventas):
    return sum(calcular_precio_venta(venta) for venta in ventas)

def venta_por_ciudades(ventas):
    ventas_por_ciudades = {}
    for linea in ventas:
        venta = calcular_precio_venta(linea)
        if linea['ciudad'] not in ventas_por_ciudades:
            ventas_por_ciudades[linea['ciudad']] = venta
        else:
            ventas_por_ciudades[linea['ciudad']] += venta
    return ventas_por_ciudades

def top_productos_vendidos(ventas):
    top_productos = {}
    for linea in ventas:
        if linea['producto'] not in top_productos:
            top_productos[linea["producto"]] = linea["unidades"]
        else:
            top_productos[linea["producto"]] += linea["unidades"]
    top_productos = sorted(top_productos.items(), key=lambda x: x[1], reverse=True)
    return top_productos[:3]

def calcular_ventas_anomalas(ventas, cantidad):
    ventas_anomalas = {}
    indice = 0
    for linea in ventas:
        if calcular_precio_venta(linea) > cantidad:
            ventas_anomalas[indice] = linea
            indice += 1
    return ventas_anomalas

