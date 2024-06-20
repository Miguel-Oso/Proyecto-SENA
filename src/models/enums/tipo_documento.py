from enum import Enum

class TipoDocumento(Enum):
    CC = 'Cedula de Ciudadania'    
    CE = 'Cedula de Extranjeria'
    PA = 'Pasaporte'    
    NIT = 'Numero de Identificacion Tributaria'
    NUIP = 'Numero Unico de Identificacion Personal'
    # NIT_EXTRANJERO = 'Numero de Identificacion Tributaria para Extranjeros'
    # NIT_EMPRESA = 'Numero de Identificacion Tributaria para Empresas'
    # NIT_PERSONA = 'Numero de Identificacion Tributaria para Personas'
    # NIT_OTRO = 'Numero de Identificacion Tributaria para Otros'
    # NIT_SIN_IDENTIFICACION = 'Numero de Identificacion Tributaria sin Identificacion'
    # NIT_EXTRANJERO_SIN_IDENTIFICACION = 'Numero de Identificacion Tributaria para Extranjeros sin Identificacion'
    # NIT_EMPRESA_SIN_IDENTIFICACION = 'Numero de Identificacion Tributaria para Empresas sin Identificacion'
    # NIT_PERSONA_SIN_IDENTIFICACION = 'Numero de Identificacion Tributaria para Personas sin Identificacion'
    # NIT_OTRO_SIN_IDENTIFICACION = 'Numero de Identificacion Tributaria para Otros sin Identificacion'
    # NIT_SIN_IDENTIFICACION = 'Numero de Identificacion Tributaria sin Identificacion'
    # NIT_EXTRANJERO_SIN_IDENTIFICACION = 'Numero de Identificacion Tributaria para Extranjeros sin Identificacion'
    # NIT_EMPRESA_SIN_IDENTIFICACION = 'Numero de Identificacion Tributaria para Empresas sin Identificacion'
    # NIT_PERSONA_SIN_IDENTIFICACION = 'Numero de Identificacion Tributaria para Personas sin Identificacion'
    # NIT_OTRO_SIN_IDENTIFICACION = 'Numero de Identificacion Tributaria para Otros sin Identificacion'
    # NIT_SIN_IDENTIFICACION = 'Numero de Identificacion Tributaria sin Identificacion'
    # NIT_EXTRANJERO_SIN_IDENTIFICACION = 'Numero de Identificacion Tributaria para Extranjeros sin Identificacion'

    @staticmethod
    def get_value(key):
        return TipoDocumento[key].value
    
    
