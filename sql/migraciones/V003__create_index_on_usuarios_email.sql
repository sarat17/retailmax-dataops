-- V003: índice para buscar usuarios por correo más rápido
-- y evitar que dos usuarios tengan el mismo correo
CREATE UNIQUE INDEX idx_usuarios_email
    ON usuarios (LOWER(email))
    WHERE email IS NOT NULL;
