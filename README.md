# Skinloot Marketplace 
## Integrantes:
- Josué Arbulú Pastor
- Salvador Córdoba
- Denzel Bautista
- Joel Jimenez
## Descripción del proyecto:
Los videojuegos han evolucionado enormemente en las últimas décadas, y con ellos, la forma en que se consumen y se comercializan objetos virtuales, como las skins. Las skins son objetos que permiten a los jugadores personalizar la apariencia de sus personajes o armas dentro del juego, y pueden ser una fuente importante de satisfacción y competitividad para los jugadores.
Sin embargo, el proceso de adquirir, vender o intercambiar skins puede ser difícil, ya que a menudo requiere la navegación de diversas plataformas de comercio electrónico, la negociación con otros jugadores y la exposición a posibles estafas. Además, muchos jugadores enfrentan problemas de seguridad y privacidad al proporcionar información personal y financiera en línea.

En respuesta a esta necesidad, surge Skinloot, una plataforma de mercado en línea que permite a los jugadores comprar, vender y negociar skins de manera segura y eficiente. Al vincular sus cuentas de juego existentes a su cuenta de Skinloot, los usuarios pueden acceder a una amplia selección de skins y realizar transacciones con otros jugadores de manera sencilla y segura.

## Objetivos principales 
El objetivo principal de Skinloot es proporcionar a los usuarios de todo el mundo una plataforma segura y confiable para comprar, vender y negociar skins de manera eficiente. Este objetivo se divide en los siguientes objetivos secundarios:

### *Ofrecer una experiencia de usuario fácil e intuitiva*: 
Uno de los principales objetivos de Skinloot es ofrecer a los usuarios una experiencia de usuario fácil e intuitiva. Para lograr esto, la plataforma ha sido diseñada con una interfaz de usuario limpia y sencilla que permite a los usuarios navegar y realizar transacciones de manera rápida y fácil.

### *Proteger la seguridad de los usuarios*: 
La seguridad de los usuarios es una preocupación constante para Skinloot. Por lo tanto, la plataforma utiliza medidas de seguridad avanzadas para proteger la información personal y financiera de los usuarios. Además, los usuarios pueden confiar en la seguridad de las transacciones realizadas a través de la plataforma.

### *Proporcionar una amplia selección de skins*: 
Skinloot se esfuerza por proporcionar a los usuarios una amplia selección de skins de diferentes juegos para que puedan encontrar fácilmente lo que están buscando. Para lograr esto, la plataforma trabaja en estrecha colaboración con una amplia red de vendedores y compradores en todo el mundo.

### *Mantener una reputación confiable*: 
La reputación de Skinloot es fundamental para el éxito de la plataforma. Por lo tanto, la plataforma se esfuerza constantemente por mantener una reputación confiable en la industria de comercio de skins de videojuegos.

## Misión
La misión de Skinloot es proporcionar una plataforma de comercio de skins segura, confiable y eficiente para los jugadores de todo el mundo. La plataforma se esfuerza por ofrecer una experiencia de usuario fácil y proteger la seguridad de los usuarios mientras proporciona una amplia selección de skins para que los usuarios encuentren lo que están buscando.

## Visión
La visión de Skinloot es convertirse en la plataforma líder en línea para el comercio de skins de videojuegos en todo el mundo. Para lograr esto, la plataforma se esfuerza por mantener altos estándares de seguridad y confiabilidad, proporcionar una experiencia de usuario superior y mantener una amplia selección de skins en su plataforma a través del . Además, Skinloot busca ser reconocida como una plataforma líder en la industria de comercio de skins de videojuegos por su reputación confiable, sus altos estándares de calidad y su expansión a la mayor cantidad de juegos disponibles en el mercado.

## Información acerca de las librerías/frameworks/plugins utilizadas en Front-end, Back-end y Base de datos:

### Front-end
Para el Front-end de Skinloot, se utilizarán las siguientes herramientas:

- *HTML*: HTML es el lenguaje de marcado utilizado para crear la estructura de las páginas web. Se utilizará para definir la estructura y el contenido de la página web de Skinloot.

- *Bootstrap*: Bootstrap es un marco de trabajo CSS y JavaScript que se utiliza para crear sitios web adaptables y responsivos. Se utilizará para proporcionar una apariencia atractiva y consistente en todas las páginas web de Skinloot, así como para hacer que el sitio sea fácilmente adaptable a diferentes tamaños de pantalla.

- *JavaScript*: JavaScript es un lenguaje de programación que se utiliza para crear aplicaciones web interactivas y dinámicas. Se utilizará en Skinloot para proporcionar funcionalidades avanzadas, como la carga dinámica de contenido y la validación de formularios.

### Back-end
Para el Back-end de Skinloot, se utilizarán las siguientes herramientas:

- *Flask*: Flask es un marco de trabajo de Python para construir aplicaciones web. Se utilizará para construir la arquitectura de la aplicación y para manejar solicitudes y respuestas.

- *Flask SQLAlchemy*: Flask SQLAlchemy es una extensión de Flask que proporciona una capa de abstracción de la base de datos. Se utilizará para interactuar con la base de datos de Skinloot de manera eficiente.

- *Flask Migrate*: Flask Migrate es una extensión de Flask SQLAlchemy que proporciona una forma fácil de realizar migraciones de bases de datos. Se utilizará para actualizar la base de datos de Skinloot de manera ordenada y sin problemas.

### Base de datos
Para la Base de datos de Skinloot, se utilizará lo siguiente:
- *PostgreSQL*: PostgreSQL es un sistema de gestión de bases de datos relacional de código abierto y gratuito. Se utilizará como la base de datos principal de Skinloot, donde se almacenará toda la información relacionada con los usuarios y las transacciones.

# Endpoints

## Registro
### Método: GET

#### Descripción:
Esta ruta se utiliza para mostrar el formulario de registro en el sitio web.

#### Parámetros:
Ninguno.

#### Retorna:
La plantilla HTML "register0.html" renderizada.

## Registrar Usuario
### Método: POST

#### Descripción:
Esta ruta se utiliza para registrar un nuevo usuario en la base de datos. Se esperan los siguientes datos del usuario: nickname, e_mail y password. El usuario se crea en la base de datos, se crea una carpeta para el usuario en el sistema de archivos y se guarda un archivo de texto vacío dentro de esa carpeta. Luego, se establecen algunas propiedades adicionales del usuario, como la ruta del archivo de texto y la imagen de perfil. Finalmente, se inicia sesión con el nuevo usuario y se redirige a la página "market".

#### Parámetros:
Ninguno.

#### Retorna:
- Redirección a la página "market" en caso de éxito.
- JSON con los siguientes campos en caso de error:
  - success: False
  - message: "Error al crear el usuario"

## Iniciar sesión
### Método: GET

#### Descripción:
Esta ruta se utiliza para mostrar el formulario de inicio de sesión en el sitio web.

#### Parámetros:
Ninguno.

#### Retorna:
La plantilla HTML "login0.html" renderizada.

## Teoría
### Método: GET, POST

#### Descripción:
Esta ruta se utiliza para realizar el inicio de sesión de un usuario. Se esperan los siguientes datos del usuario: e_mail y password. Se realiza una búsqueda en la base de datos del usuario con el correo electrónico proporcionado. Si se encuentra un usuario con el correo electrónico y la contraseña coincidentes, se inicia sesión con ese usuario y se redirige a la página "market". De lo contrario, se devuelve un JSON indicando que el usuario no está registrado.

#### Parámetros:
Ninguno o los siguientes campos en el cuerpo de la solicitud:
- e_mail: Correo electrónico del usuario.
- password: Contraseña del usuario.

#### Retorna:
- Redirección a la página "market" en caso de éxito.
- JSON con los siguientes campos en caso de error:
  - success: False
  - message: "User not registered"

## Mercado
### Método: GET

#### Descripción:
Esta ruta se utiliza para mostrar la página del mercado en el sitio web. Solo los usuarios autenticados pueden acceder a esta página.

#### Parámetros:
Ninguno.

#### Retorna:
La plantilla HTML "market2.html" renderizada.


## Mostrar Publicaciones
### Método: GET

#### Descripción:
Esta ruta se utiliza para obtener todas las publicaciones disponibles en venta. Se recuperan todas las instancias de `Postventa` de la base de datos que tienen la propiedad `on_sale` establecida como `True`. Luego, se serializan las publicaciones y se devuelven en un objeto JSON.

#### Parámetros:
Ninguno.

#### Retorna:
Un objeto JSON con los siguientes campos:
- success: True si se realizó correctamente la operación.
- serialized: Una lista de objetos JSON que representan las publicaciones serializadas.

## Mostrar Skins Actuales
### Método: GET

#### Descripción:
Esta ruta se utiliza para obtener todas las skins pertenecientes al usuario actualmente autenticado. Se recuperan todas las instancias de `Skin` de la base de datos que tienen `user_id` igual al `id` del usuario actual. Luego, se serializan las skins y se devuelven en un objeto JSON.

#### Parámetros:
Ninguno.

#### Retorna:
Un objeto JSON con los siguientes campos:
- success: True si se realizó correctamente la operación.
- serialized: Una lista de objetos JSON que representan las skins serializadas.

## Comprar Skin
### Método: POST

#### Descripción:
Esta ruta se utiliza para realizar la compra de una skin. Se espera que se envíen los siguientes datos en el cuerpo de la solicitud: `skin_on_sale` (ID de la skin en venta), `seller_uid` (ID del vendedor) y `precio` (precio de la skin). Si el usuario actual está autenticado, se verifica el saldo disponible en su cuenta. Si el saldo es suficiente, se crea una nueva transacción y se actualiza el saldo del usuario. Finalmente, se confirma la transacción y se devuelve un objeto JSON con el resultado de la operación.

#### Parámetros:
Los siguientes campos en el cuerpo de la solicitud:
- skin_on_sale: ID de la skin en venta.
- seller_uid: ID del vendedor.
- precio: Precio de la skin.

#### Retorna:
Un objeto JSON con los siguientes campos:
- success: True si se realizó correctamente la operación.
- message: Mensaje informativo sobre el resultado de la operación.

## Mostrar Skins
### Método: GET

#### Descripción:
Esta ruta se utiliza para mostrar las skins del usuario en una página HTML. Solo los usuarios autenticados pueden acceder a esta página.

#### Parámetros:
Ninguno.

#### Retorna:
La plantilla HTML "show_skins.html" renderizada.

## Configuración de Usuario
### Método: GET

#### Descripción:
Esta ruta se utiliza para mostrar la página de configuración de usuario en el sitio web. Solo los usuarios autenticados pueden acceder a esta página.

#### Parámetros:
Ninguno.

#### Retorna:
La plantilla HTML "usuario.html" renderizada.

## Actualizar Usuario
### Método: POST

#### Descripción:
Esta ruta se utiliza para actualizar los datos del usuario. Se esperan los siguientes datos del formulario: `username` (nombre de usuario), `profile-picture` (imagen de perfil) y `balance` (saldo). Se actualizan los datos del usuario en la base de datos de acuerdo a los valores proporcionados. Si el usuario está autenticado, se actualiza su nombre de usuario, saldo y/o imagen de perfil. Luego, se redirige a la página "market".

#### Parámetros:
Los siguientes campos en el cuerpo de la solicitud:
- username: Nombre de usuario.
- profile-picture: Imagen de perfil (archivo).
- balance: Saldo.

#### Retorna:
- Redirección a la página "market" en caso de éxito.
- JSON con los siguientes campos en caso de error:
  - success: False
  - message: "Error updating user data"
