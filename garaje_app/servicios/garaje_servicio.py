from modelos.vehiculo import Vehiculo

class GarajeServicio:
    """Contiene la lógica del negocio: agregar, listar y eliminar vehículos."""
    
    def __init__(self):
        self._vehiculos: list[Vehiculo] = []
    
    def agregar_vehiculo(self, placa: str, marca: str, propietario: str) -> tuple[bool, str]:
        """
        Registra un nuevo vehículo en el garaje.
        Retorna (éxito: bool, mensaje: str).
        """
        placa = placa.strip()
        marca = marca.strip()
        propietario = propietario.strip()
        
        if not placa or not marca or not propietario:
            return False, "Todos los campos son obligatorios."
        
        if any(v.placa == placa for v in self._vehiculos):
            return False, f"Ya existe un vehículo con la placa {placa}."
        
        vehiculo = Vehiculo(placa, marca, propietario)
        self._vehiculos.append(vehiculo)
        return True, "Vehículo registrado correctamente."
    
    def listar_vehiculos(self) -> list[Vehiculo]:
        """Retorna la lista completa de vehículos registrados."""
        return list(self._vehiculos)
    
    def total_vehiculos(self) -> int:
        """Retorna el número total de vehículos registrados."""
        return len(self._vehiculos)
    
    def eliminar_vehiculo(self, placa: str) -> tuple[bool, str]:
        """
        Elimina un vehículo por su placa.
        Retorna (éxito: bool, mensaje: str).
        """
        for i, vehiculo in enumerate(self._vehiculos):
            if vehiculo.placa == placa:
                self._vehiculos.pop(i)
                return True, f"Vehículo con placa {placa} eliminado correctamente."
        return False, f"No se encontró un vehículo con la placa {placa}."