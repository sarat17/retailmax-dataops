-- V002: agrega el correo electrónico
ALTER TABLE usuarios
    ADD COLUMN email VARCHAR(255);

-- El correo, si existe, debe tener un formato válido
ALTER TABLE usuarios
    ADD CONSTRAINT ck_usuarios_email
    CHECK (email IS NULL OR email ~* '^[^@\s]+@[^@\s]+\.[^@\s]+$');
