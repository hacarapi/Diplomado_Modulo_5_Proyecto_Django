
# **Diplomado FullStack USIP**
## *Módulo V: Desarrollo Backend con Django*
## **Proyecto: Administración de Parqueo de Automóviles**
### **Integrantes**
- Huber Acarapi Mamani

## **Descripción del Proyecto**
Este proyecto es una solución desarrollada en Django para gestionar un sistema de parqueo de automóviles. Proporciona las siguientes funcionalidades:

- Verificar la disponibilidad de espacios en el parqueo.
- Registrar vehículos al ingresar y salir del parqueo.
- Calcular el costo total basado en el tiempo de estacionamiento y las tarifas por hora.
- Exponer una API RESTful para interactuar con el sistema.

El proyecto utiliza **Django Rest Framework (DRF)** para la creación de las API y está diseñado para ser modular y extensible.

---

## **Estructura del Proyecto**
- **Aplicación principal:** `estacionamiento`
- **Modelos principales:**
  - Vehículo
  - Espacio
  - Tarifa
  - Registro
- **Vistas:** ModelViewSet para CRUD básico y una Custom API para verificar disponibilidad.
- **Validaciones personalizadas:** Para datos como la placa de los vehículos.

---

## **Instalación**

1. Clona este repositorio:
   ```bash
   git clone https://github.com/hacarapi/Diplomado_Modulo_5_Proyecto_Django.git
   cd parqueo
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Realiza las migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

---

## **Descripción de las Clases y Modelos**

### **1. Vehículo**
Representa un vehículo que utiliza el parqueo.

- **Atributos:**
  - `placa (CharField)`: Placa del vehículo. Validación personalizada para un mínimo de 6 caracteres.
  - `marca (CharField)`: Marca del vehículo.
  - `modelo (CharField)`: Modelo del vehículo.

- **Validaciones Personalizadas:**
  - La **placa** debe tener al menos 6 caracteres. Si no cumple, lanza un `ValidationError`.

```python
def validar_placa(placa):
    if len(placa) < 6:
        raise ValidationError('La placa debe tener al menos 6 caracteres.')
```

---

### **2. Espacio**
Define los espacios disponibles en el parqueo.

- **Atributos:**
  - `numero (IntegerField)`: Número único que identifica el espacio.
  - `disponible (BooleanField)`: Indica si el espacio está disponible (True) o no (False).

---

### **3. Tarifa**
Define el costo por hora de uso del parqueo.

- **Atributos:**
  - `precio_hora (DecimalField)`: Costo por hora con precisión de hasta 2 decimales.

---

### **4. Registro**
Registra la entrada, salida y costo asociado a un vehículo estacionado.

- **Atributos:**
  - `vehiculo (ForeignKey)`: Relación con el modelo Vehículo.
  - `espacio (ForeignKey)`: Relación con el modelo Espacio.
  - `hora_entrada (DateTimeField)`: Fecha y hora de entrada.
  - `hora_salida (DateTimeField)`: Fecha y hora de salida (puede ser nula mientras el vehículo esté estacionado).
  - `costo (DecimalField)`: Costo total calculado.

- **Métodos:**
  - `calcular_costo()`: Calcula el costo del estacionamiento basado en la duración y la tarifa por hora.
  - **Validaciones Automáticas:** Si hay una `hora_salida`, se calcula automáticamente el costo al guardar.

---

## **Vistas (ModelViewSet y Custom API)**

### **ModelViewSet**
Se implementan cuatro `ModelViewSet` para gestionar CRUD de cada modelo:

1. **Vehículo (VehiculoViewSet)**
   - Permite registrar, actualizar y listar vehículos.
2. **Espacio (EspacioViewSet)**
   - Gestiona los espacios disponibles en el parqueo.
3. **Tarifa (TarifaViewSet)**
   - Define y actualiza tarifas por hora.
4. **Registro (RegistroViewSet)**
   - Registra entradas y salidas, y calcula automáticamente los costos.

---

### **Custom API**
Ruta personalizada para verificar si hay espacios disponibles.

- **Ruta:** `/api/verificar-espacio/`
- **Método:** `GET`
- **Funcionalidad:**
  Devuelve un JSON indicando si hay al menos un espacio disponible.

```python
@api_view(['GET'])
def verificar_espacio_disponible(request):
    disponible = Espacio.objects.filter(disponible=True).exists()
    return Response({'espacio_disponible': disponible})
```

Ejemplo de Respuesta:
```json
{
    "espacio_disponible": true
}
```

---

## **Uso de la API**
### **Endpoints Principales:**
- **Vehículos:** `/api/vehiculos/`
- **Espacios:** `/api/espacios/`
- **Tarifas:** `/api/tarifas/`
- **Registros:** `/api/registros/`
- **Custom API:** `/api/verificar-espacio/`

Utiliza herramientas como **Postman** o **cURL** para interactuar con estas API.

---

## **Pruebas**
1. Agrega espacios disponibles en el administrador de Django.
2. Define tarifas en el sistema.
3. Usa el endpoint de **Registros** para registrar entradas y salidas de vehículos.
4. Verifica la disponibilidad con el endpoint `/api/verificar-espacio/`.

---

## **Licencia**
Este proyecto está bajo la licencia [MIT](https://opensource.org/licenses/MIT).
