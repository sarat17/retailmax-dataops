-- V001: crea la tabla de usuarios
CREATE TABLE usuarios (
    id_usuario       BIGSERIAL     PRIMARY KEY,
    tipo_documento   VARCHAR(5)    NOT NULL,
    numero_documento VARCHAR(20)   NOT NULL,
    nombre           VARCHAR(150)  NOT NULL,
    pais             CHAR(2)       NOT NULL,
    estado           VARCHAR(10)   NOT NULL DEFAULT 'activo',
    fecha_registro   TIMESTAMP     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_usuarios_documento UNIQUE (tipo_documento, numero_documento, pais),
    CONSTRAINT ck_usuarios_estado CHECK (estado IN ('activo', 'inactivo', 'historico'))
);
