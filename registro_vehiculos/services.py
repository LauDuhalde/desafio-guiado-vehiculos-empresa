from registro_vehiculos.models import Vehiculo, Chofer, RegistroContabilidad
from datetime import date

def crear_vehiculo(patente, marca, modelo, year, activo=False):
    try:
        # Verificar si ya existe un vehículo con la misma patente
        if Vehiculo.objects.filter(patente=patente).exists():
            print("Ya existe un vehículo con esta patente.")
            return None
        
        # Crear un nuevo vehículo
        vehiculo = Vehiculo(patente=patente, marca=marca, modelo=modelo, year=year, activo=activo)
        vehiculo.save()
        
        print("Vehículo creado exitosamente.")
        return vehiculo
    except Exception as e:
        print(f"Error al crear el vehículo: {e}")
        return None

def crear_chofer(rut, nombre, apellido, activo=False):
    try:
        # Verificar si ya existe un chofer con el mismo Rut
        if Chofer.objects.filter(rut=rut).exists():
            print("Ya existe un chofer con este Rut.")
            return None
        
        # Crear un nuevo chofer
        chofer = Chofer(rut=rut, nombre=nombre, apellido=apellido, activo=activo)
        chofer.save()
        
        print("Chofer creado exitosamente.")
        return chofer
    except Exception as e:
        print(f"Error al crear el chofer: {e}")
        return None
    
def crear_registro_contable(fecha_compra_str,valor,vehiculo):
    try:
        # Dividir la cadena de fecha en año, mes y día
        año, mes, dia = map(int, fecha_compra_str.split('-'))
        # Crear un objeto date
        fecha_compra = date(año, mes, dia)
        
        if RegistroContabilidad.objects.filter(vehiculo=vehiculo).exists():
            print("Ya existe un registro con esta fecha.")
            return None
        
        registro_contable = RegistroContabilidad(fecha_compra=fecha_compra, valor=valor, vehiculo=vehiculo)
        registro_contable.save()
        
        print("Registro contable creado exitosamente.")
        return registro_contable
    
    except ValueError:
        print("Fecha con formato inválido. Por favor, ingrese en este formato: date(2000, 02, 28)") 
        return None
    except Exception as e:
        print(f"Error al crear el registro contable: {e}")
        return None
def obtener_chofer(rut_chofer):
    try:
        # Buscar el chofer por su Rut
        chofer = Chofer.objects.get(rut=rut_chofer)
        print(f"Chofer encontrado: {chofer.nombre} {chofer.apellido}")
        return chofer
    except Chofer.DoesNotExist:
        print("No se encontró ningún chofer con ese Rut.")
        return None
    except Exception as e:
        print(f"Error al obtener el chofer: {e}")
        return None

def deshabilitar_chofer(chofer):
    try:
        # Verificar si el chofer ya está deshabilitado
        if not chofer.activo:
            print("El chofer ya está deshabilitado.")
            return None
        
        # Deshabilitar al chofer
        chofer.activo = False
        chofer.save()
        
        print("Chofer deshabilitado correctamente.")
        return chofer
    except Exception as e:
        print(f"Error al deshabilitar el chofer: {e}")
        return None


def habilitar_chofer(chofer):
    try:
        # Verificar si el chofer ya está habilitado
        if chofer.activo:
            print("El chofer ya está habilitado.")
            return None
        
        # Habilitar al chofer
        chofer.activo = True
        chofer.save()
        
        print("Chofer habilitado correctamente.")
        return chofer
    except Exception as e:
        print(f"Error al habilitar el chofer: {e}")
        return None


def obtener_vehiculo(patente):
    try:
        # Buscar el vehículo por su patente
        vehiculo = Vehiculo.objects.get(patente=patente)
        print(f"Vehículo encontrado: {vehiculo}")
        return vehiculo
    except Vehiculo.DoesNotExist:
        print("No se encontró ningún vehículo activo con esa patente.")
        return None
    except Exception as e:
        print(f"Error al obtener el vehículo: {e}")
        return None

def deshabilitar_vehiculo(vehiculo):
    try:
        # Verificar si el vehículo ya está deshabilitado
        if not vehiculo.activo:
            print("El vehículo ya está deshabilitado.")
            return None
        
        # Deshabilitar el vehículo
        vehiculo.activo = False
        vehiculo.save()
        
        print("Vehículo deshabilitado correctamente.")
        return vehiculo
    except Exception as e:
        print(f"Error al deshabilitar el vehículo: {e}")
        return None

def habilitar_vehiculo(vehiculo):
    try:
        # Verificar si el vehículo ya está habilitado
        if vehiculo.activo:
            print("El vehículo ya está habilitado.")
            return None
        
        # Habilitar el vehículo
        vehiculo.activo = True
        vehiculo.save()
        
        print("Vehículo habilitado correctamente.")
        return vehiculo
    except Exception as e:
        print(f"Error al habilitar el vehículo: {e}")
        return None

def asignar_chofer_a_vehiculo(chofer, vehiculo):
    try:
        # Verificar si el vehículo ya tiene un chofer asignado
        if chofer.vehiculo:
            print("El vehículo ya tiene un chofer asignado.")
            return None
        
        # Asignar el chofer al vehículo
        #chofer.vehiculo=vehiculo
        vehiculo.chofer = chofer
        vehiculo.save()
        chofer.save()
        
        print("Chofer asignado al vehículo correctamente.")
    except Exception as e:
        print(f"Error al asignar chofer al vehículo: {e}")
        
def imprimir_datos_vehiculos(): 
    vehiculos = Vehiculo.objects.all() 
    for v in vehiculos: 
        print(f"Vehiculo:{v.patente}/{v.marca}/{v.modelo}/" + f"{v.year}/activo:{v.activo}") 
        if hasattr(v, "chofer"): 
            print(f"\tChofer[{v.chofer.rut}]:{v.chofer.nombre} " + f"{v.chofer.apellido}/activo:{v.chofer.activo}") 
        if hasattr(v, "contabilidad"): 
            print(f"\tContabilidad:[{v.contabilidad.id}]:fecha_compra:" + f"{v.contabilidad.fecha_compra}/valor:{v.contabilidad.valor}")

#Se usan para pruebas
def eliminar_vehiculo(patente):
    try:
        vehiculo = Vehiculo.objects.get(patente=patente)
        
        # Verificar si hay registros asociados al vehículo
        if Chofer.objects.filter(vehiculo=vehiculo).exists() or RegistroContabilidad.objects.filter(vehiculo=vehiculo).exists():
            respuesta = input("Hay registros asociados a este vehículo. ¿Desea eliminarlos también? (s/n): ")
            if respuesta.lower() == 's':
                # Eliminar chofer asociado
                if Chofer.objects.filter(vehiculo=vehiculo).exists():
                    chofer = Chofer.objects.get(vehiculo=vehiculo)
                    eliminar_chofer(chofer.rut)
                
                # Eliminar registro contable asociado
                if RegistroContabilidad.objects.filter(vehiculo=vehiculo).exists():
                    registro_contabilidad = RegistroContabilidad.objects.get(vehiculo=vehiculo)
                    eliminar_registro_contabilidad(registro_contabilidad)
                print("Registros asociados eliminados correctamente.")
            else:
                print("No se eliminaron los registros asociados.")
                return
        
        # Si no hay choferes asociados, podemos eliminar el vehículo directamente
        vehiculo.delete()
        print("Vehículo eliminado correctamente.")
    except Vehiculo.DoesNotExist:
        print("No se encontró ningún vehículo con esa patente.")
    except Exception as e:
        print(f"Error al eliminar el vehículo: {e}")

def eliminar_chofer(rut):
    try:
        chofer = Chofer.objects.get(rut=rut)
        chofer.delete()
        print("Chofer eliminado correctamente.")
    except Chofer.DoesNotExist:
        print("No se encontró ningún chofer con ese Rut.")
    except Exception as e:
        print(f"Error al eliminar el chofer: {e}")

def eliminar_registro_contabilidad(registro_contable):
    try:
        registro_contable.delete()
        print("Registro contable eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar el registro contable: {e}")

def obtener_registro_contabilidad_por_vehiculo(vehiculo):
    try:
        registro_contabilidad = RegistroContabilidad.objects.get(vehiculo=vehiculo)
        return registro_contabilidad
    except RegistroContabilidad.DoesNotExist:
        print("No se encontró ningún registro contable para este vehículo.")
        return None
    except Exception as e:
        print(f"Error al obtener el registro contable: {e}")
        return None
