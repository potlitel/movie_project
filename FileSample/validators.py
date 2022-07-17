from django.core.validators import RegexValidator

propietario = RegexValidator(r'^[a-zA-Z]*$', 'El campo "Propietario" contiene caracteres no permitidos.')
title = RegexValidator(r'^[a-zA-Z]*$', 'El campo "Titulo" contiene caracteres no permitidos.')