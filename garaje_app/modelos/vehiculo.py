class Vehiculo:
    """Representa los datos de un vehículo en el garaje."""
    
    def __init__(self, placa: str, marca: str, propietario: str):
        self.placa = placa
        self.marca = marca
        self.propietario = propietario
    
    @property
    def placa(self):
        return self._placa
    
    @placa.setter
    def placa(self, value):
        self._placa = value.strip()
    
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, value):
        self._marca = value.strip()
    
    @property
    def propietario(self):
        return self._propietario
    
    @propietario.setter
    def propietario(self, value):
        self._propietario = value.strip()
    
    def __repr__(self):
        return f"Vehiculo(placa={self.placa}, marca={self.marca}, propietario={self.propietario})"