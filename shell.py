from registro_vehiculos.services import crear_vehiculo,crear_chofer,crear_registro_contable,obtener_vehiculo,obtener_chofer,asignar_chofer_a_vehiculo,eliminar_chofer,imprimir_datos_vehiculos,eliminar_vehiculo

vehiculo=crear_vehiculo('ABCD12', 'Toyota', 'Corolla', 2020, True)
vehiculo_existente=crear_vehiculo('ABCD12', 'Toyota', 'Corolla', 2020, True)
vehiculo_inactivo=crear_vehiculo('IJKL56','Modelo2','Marca2',2024) 

chofer=crear_chofer('1234567890', 'Juan', 'Pérez', True)
chofer_existente=crear_chofer('1234567890', 'Juan', 'Pérez', True)
chofer_inactivo=crear_chofer('987456321','Pepito','Concha',False)

vehiculo = obtener_vehiculo('ABCD12')
chofer=obtener_chofer('1234567890')

registro_contable=crear_registro_contable('2022-12-01',10000000,vehiculo)
eliminar_chofer('1234567890')

asignar_chofer_a_vehiculo(chofer, vehiculo)

imprimir_datos_vehiculos()

eliminar_vehiculo('ABCD12')