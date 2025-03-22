
CREATE TABLE `contexto` (
  `id` int(11) NOT NULL,
  `nombre` varchar(150) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `color` varchar(50) DEFAULT NULL,
  `icono` varchar(150) DEFAULT NULL,
  `img` longblob DEFAULT NULL,
  `letras` varchar(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


INSERT INTO `contexto` (`id`, `nombre`, `descripcion`, `color`, `icono`, `img`, `letras`) VALUES
(1, 'DESARROLLO DE SISTEMAS INTELIGENTES', NULL, '#d1751877', NULL, NULL, 'DSI'),
(2, 'FUNDAMENTOS Y DISEÑO DE REDES DE DATOS', NULL, '#ff2f2f77', NULL, NULL, 'FDR'),
(3, 'INGENIERÍA Y CALIDAD DE SOFTWARE', NULL, '#2fa8ff77', NULL, NULL, 'ICS'),
(4, 'INTELIGENCIA DE NEGOCIOS', NULL, '#333F4F77', NULL, NULL, 'IN'),
(5, 'INVESTIGACION EN INGENIERÍA', NULL, '#ffff2180', NULL, NULL, 'IEI'),
(6, 'MORAL CATOLICA', NULL, '#8a19cc77', NULL, NULL, 'MC'),
(7, 'SISTEMAS DISTRIBUIDOS', NULL, '#19a01777', NULL, NULL, 'SD'),
(8, 'FUTSAL', NULL, '#00000077', NULL, NULL, 'FUT'),
(9, 'INGLÉS B1', NULL, '#fe2cb363', NULL, NULL, 'ING'),
(10, 'AUDIT', NULL, '#00008b77', NULL, NULL, 'AUD'),
(17, 'PROYECTO', NULL, '#8700fc', NULL, NULL, 'PRJCT');


CREATE TABLE `horario` (
  `id` int(11) NOT NULL,
  `titulo` text DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `dia` int(11) DEFAULT NULL,
  `h_ini` int(11) DEFAULT NULL,
  `min_ini` int(11) DEFAULT NULL,
  `h_fin` int(11) DEFAULT NULL,
  `min_fin` int(11) DEFAULT NULL,
  `fecha_ini` date DEFAULT NULL,
  `fecha_fin` date DEFAULT NULL,
  `contextoid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


INSERT INTO `horario` (`id`, `titulo`, `descripcion`, `dia`, `h_ini`, `min_ini`, `h_fin`, `min_fin`, `fecha_ini`, `fecha_fin`, `contextoid`) VALUES
(1, NULL, NULL, 6, 7, 0, 11, 0, '2025-03-17', '2025-07-05', 1),
(2, NULL, NULL, 2, 9, 0, 11, 0, '2025-03-17', '2025-07-05', 2),
(3, NULL, NULL, 3, 7, 0, 10, 0, '2025-03-17', '2025-07-05', 2),
(4, NULL, NULL, 2, 11, 0, 14, 0, '2025-03-17', '2025-07-05', 3),
(5, NULL, NULL, 4, 7, 0, 10, 0, '2025-03-17', '2025-07-05', 3),
(6, NULL, NULL, 5, 10, 0, 13, 0, '2025-03-17', '2025-07-05', 4),
(7, NULL, NULL, 6, 11, 0, 13, 0, '2025-03-17', '2025-07-05', 4),
(8, NULL, NULL, 4, 14, 0, 19, 0, '2025-03-17', '2025-07-05', 5),
(9, NULL, NULL, 1, 16, 0, 19, 0, '2025-03-17', '2025-07-05', 6),
(10, NULL, NULL, 4, 10, 0, 12, 0, '2025-03-17', '2025-07-05', 7),
(11, NULL, NULL, 5, 7, 0, 10, 0, '2025-03-17', '2025-07-05', 7),
(12, NULL, NULL, 3, 15, 0, 17, 0, '2025-03-17', '2025-07-05', 8),
(13, NULL, NULL, 2, 19, 0, 21, 0, '2025-03-17', '2025-07-05', 9),
(14, NULL, NULL, 4, 19, 0, 21, 0, '2025-03-17', '2025-07-05', 9),
(15, NULL, NULL, 1, 21, 0, 22, 0, '2025-03-17', '2025-07-05', 10),
(16, NULL, NULL, 3, 10, 0, 12, 0, '2025-03-17', '2025-07-05', 10),
(18, 'Bordes de tabla', NULL, 6, 0, 0, 2, 0, '2025-03-21', '2025-03-21', 10),
(19, 'Comprar Audifonos', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(20, 'Descargar Invincible', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(21, NULL, NULL, 6, 16, 0, 18, 0, '2025-03-17', '2025-07-05', 17),
(22, NULL, NULL, 1, 8, 0, 12, 0, '2025-03-17', '2025-07-05', 17);


ALTER TABLE `contexto`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `horario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FKhorario716731` (`contextoid`);


ALTER TABLE `contexto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;


ALTER TABLE `horario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;


ALTER TABLE `horario`
  ADD CONSTRAINT `FKhorario716731` FOREIGN KEY (`contextoid`) REFERENCES `contexto` (`id`);
COMMIT;
