preciotarifa = float(input("Introduce el precio de la tarifa: "))
preciopagado = float(input("Introduce el precio pagado: "))

descuento = ((preciotarifa - preciopagado) / preciotarifa) * 100

print("El descuento aplicado es del", descuento, "%")
