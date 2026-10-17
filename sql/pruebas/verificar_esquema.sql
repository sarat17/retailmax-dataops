-- Prueba de esquema: falla si falta alguna columna esperada
DO $$
BEGIN
  IF (SELECT COUNT(*) FROM information_schema.columns
      WHERE table_name = 'usuarios'
        AND column_name IN ('id_usuario','tipo_documento','numero_documento','nombre','pais','estado','fecha_registro','email')) <> 8 THEN
    RAISE EXCEPTION 'La tabla usuarios no tiene las 8 columnas esperadas';
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_indexes WHERE indexname = 'idx_usuarios_email') THEN
    RAISE EXCEPTION 'Falta el índice idx_usuarios_email';
  END IF;
  RAISE NOTICE 'Esquema de usuarios correcto';
END $$;
