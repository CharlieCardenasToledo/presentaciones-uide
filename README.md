# Presentaciones de clase

Presentaciones animadas de las clases de la Universidad Internacional del Ecuador, campus Loja, de Charlie Cárdenas Toledo. Cada diapositiva es una escena que se construye por pasos, pensada para proyectar en el aula.

Sitio: https://charliecardenastoledo.github.io/presentaciones-uide/

| Curso | Semana | Presentación |
| --- | --- | --- |
| CC05A_IFT200 Estructura, modelado y almacenamiento de BD | 1. Enfoque de bases de datos, modelos de datos, esquemas y DBMS | [bd-semana-01](https://charliecardenastoledo.github.io/presentaciones-uide/bd-semana-01/) |
| LTI_05A_INS Ingeniería del Software | 1. Ingeniería de software hoy, ética y descubrimiento inicial del proyecto | [ins-semana-01](https://charliecardenastoledo.github.io/presentaciones-uide/ins-semana-01/) |
| LTI_05U_IHC Interacción Hombre Computadora | 1. HCI como ciencia de sistemas interactivos | [hci-semana-01](https://charliecardenastoledo.github.io/presentaciones-uide/hci-semana-01/) |
| LTI_05U_ESD Estructura de Datos | 1. Big-O, TDA y representación en memoria | [esd-semana-01](https://charliecardenastoledo.github.io/presentaciones-uide/esd-semana-01/) |
| CC05A_IFT202 Fundamentos de la Seguridad | 1. Principios de ciberseguridad: tríada CIA, riesgo y ética | [ift202-semana-01](https://charliecardenastoledo.github.io/presentaciones-uide/ift202-semana-01/) |
| CC05A_IFT202 Fundamentos de la Seguridad | 2. Introducción al marco NIST: funciones, perfiles y niveles | [ift202-semana-02](https://charliecardenastoledo.github.io/presentaciones-uide/ift202-semana-02/) |

## Cómo se usa

- Las flechas del teclado avanzan y retroceden. Cada avance revela una idea.
- La tecla `P` abre el modo presentador: una segunda pestaña para el público y las notas de la clase en la pestaña del docente. Las notas se pueden editar y se guardan en el navegador.
- Funciona en Chrome y en Edge. Para proyectar, compartir o arrastrar la pestaña del público a la pantalla del proyector.

## Cómo está hecho

Cada presentación es una composición de [HyperFrames](https://hyperframes.heygen.com) generada con un script propio, que se exportó a archivos estáticos. La carpeta `vendor/` contiene el reproductor (hyperframes 0.8.150). No hay servidor ni dependencias de compilación; la animación usa GSAP desde jsDelivr.

Para ver el sitio en local basta cualquier servidor de archivos estáticos:

```bash
python -m http.server 8080
```

## Aviso

El logotipo de la UIDE y de Arizona State University pertenece a sus titulares. El material es de uso docente.
