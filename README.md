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

- *Vue.js*: Vue.js es un framework de JavaScript que se utiliza para construir interfaces de usuario interactivas y dinámicas en aplicaciones web. Aunque Vue.js se basa en JavaScript, también se integra con HTML para definir la estructura y el contenido de las páginas web.

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

# Structure Project

- backend
  - app/
    - **init**.py
    - **authentication**.py
    - **models**.py
    - **users_controllers**.py
  - config/
    - **local**.py
    - **qa**.py
  - AppTests.py
  - static/
    - images

- frontend
  - src/
    - assets/
      - imagenes
      - logo
  - components/
    - NavbarMarket.vue
    - RegisterSkin.vue
    - ShowPosts.vue
    - ShowSkins.vue
    - TestOpen.vue
  - router/
    - index.js
  - services
    - loginuser.api.js
    - openai.api.js
    - userpost.api.js
    - users.api.js
    - userskins.api.js
  - views
    - AboutView.vue
    - HomePage.vue
    - LoginView.vue
    - MarketView.vue
    - PostSkinView.vue
    - RegisterView.vue
    - UserConfigView.vue
  - App.vue
