# Sistema P2P para Intercambio de Archivos

Este proyecto implementa una red peer-to-peer (P2P) diseñada para la simulación del intercambio de archivos entre nodos. La arquitectura emplea API REST para la comunicación con un servidor central y gRPC para la comunicación directa entre los peers.

## Objetivo

El sistema tiene como objetivo facilitar el intercambio eficiente de archivos entre usuarios predefinidos, proporcionando autenticación segura, búsqueda avanzada de archivos y descarga mediante comunicaciones optimizadas.

## Características

- **Red P2P Funcional**: Implementación de una red distribuida que permite la comunicación directa entre los peers.
- **API REST**: Gestiona la autenticación y la indexación de archivos a través de un servidor central.
- **gRPC**: Optimiza la transferencia de archivos entre los peers, minimizando la latencia.
- **Autenticación Segura**: Solo los usuarios predefinidos pueden acceder al sistema.
- **Simulación de Transferencia de Archivos**: El intercambio de archivos se simula mediante la transferencia de nombres de archivos entre peers.

## Funcionalidades Principales

1. **Inicio de Sesión**: Autenticación de usuarios predefinidos mediante credenciales.
2. **Cierre de Sesión**: Terminación segura de la sesión activa del usuario.
3. **Indexación de Archivos**: Actualización de los archivos disponibles para compartir en la red.
4. **Búsqueda de Archivos**: Búsqueda de archivos distribuidos en la red P2P.
5. **Descarga de Archivos**: Descarga de archivos desde otros peers conectados en la red.

## Requisitos Funcionales

- **Autenticación de Usuarios**: El sistema debe verificar credenciales contra una lista de usuarios predefinidos.
- **Gestión de Sesiones**: Permite que un usuario tenga solo una sesión activa simultáneamente.
- **Mantenimiento de Listas de Archivos**: Cada peer debe tener una lista actualizada de los archivos disponibles para compartir.

## Requisitos Técnicos

- **Lenguaje de Programación**: Python.
- **Framework REST**: Flask para la implementación del servidor central.
- **Comunicación Peer-to-Peer**: gRPC para conexiones rápidas y eficientes.
- **Almacenamiento**: Los datos de usuarios y archivos se almacenan en formato JSON.

## Requisitos No Funcionales

- **Escalabilidad**: El sistema debe poder manejar la adición de nuevos peers sin degradar significativamente el rendimiento.
- **Concurrencia**: El sistema debe soportar múltiples conexiones simultáneas entre peers utilizando gRPC.
- **Eficiencia**: Las comunicaciones entre peers deben ser optimizadas para reducir la latencia en la transferencia de archivos.

## Instrucciones de Instalación

### 1. Configuración del Servidor Central

1. En una terminal, navegue al directorio principal del proyecto.
2. Ejecute el siguiente comando para iniciar el servidor:

    ```bash
    python api_server.py
    ```

3. El servidor estará disponible en `http://127.0.0.1:5000`.

### 2. Configuración de los Peers

Para cada peer, siga los siguientes pasos:

1. Abra una nueva terminal y navegue al directorio correspondiente del peer (`/peer_n`, donde `n` es el número del peer).
2. Ejecute el servidor P2P con el siguiente comando:

    ```bash
    python p2p_server.py
    ```

### 3. Configuración del Cliente P2P

Para iniciar el cliente P2P:

1. Abra una nueva terminal y navegue al directorio del peer.
2. Ejecute el cliente con el siguiente comando:

    ```bash
    python p2p_client.py
    ```

3. Se mostrará el menú principal para interactuar con el sistema.

## Uso del Cliente

1. **Iniciar Sesión**: Seleccione la opción `1. Login` en el menú principal, luego ingrese el nombre de usuario y contraseña.
2. **Indexar Archivos**: Seleccione `3. Indexar Archivos` para actualizar la lista de archivos disponibles en la red.
3. **Buscar Archivos**: Seleccione `4. Buscar Archivo` e ingrese el nombre del archivo deseado.
4. **Descargar Archivos**: Tras una búsqueda exitosa, seleccione `5. Descargar Archivo` y elija el peer desde el cual descargar.
5. **Cerrar Sesión**: Seleccione `2. Logout` para cerrar su sesión de forma segura.

## Gestión de Archivos Compartidos

- **Añadir Archivos**: Para añadir nuevos archivos, edite el array `files` en el archivo `peer_config.json`. Reinicie el servidor P2P e indexe los archivos nuevamente.
- **Eliminar Archivos**: Para eliminar archivos, modifique el array `files` en `peer_config.json`, reinicie el servidor P2P e indexe nuevamente.

---
