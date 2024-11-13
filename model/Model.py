class Model:
    def create(self, data: dict[str: str | int | bool | float]):
        raise NotImplementedError("Metódo não implementado")
    
    
    def delete(self, id: int):
        raise NotImplementedError("Metódo não implementado")
    
    
    def update(self, data: dict[str: str | int | bool | float], id: int):
        raise NotImplementedError("Metódo não implementado")
    
    
    def get(id: int | None = None):
        raise NotImplementedError("Metódo não implementado")