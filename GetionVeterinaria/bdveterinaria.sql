-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-10-2023 a las 04:14:35
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bdveterinaria`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
CREATE DATABASE `bdveterinaria`  /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE bdveterinaria;
CREATE TABLE `clientes` (
    `dni` int(255) NOT NULL,
    `apellido` text NOT NULL,
    `nombre` text NOT NULL,
    `Direccion` varchar(200) NOT NULL,
    `telefono` varchar(255) NOT NULL,
    `email` varchar(100) NOT NULL,
    `estado` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcado de datos para la tabla `clientes`
INSERT INTO `clientes` (`dni`, `apellido`, `nombre`, `Direccion`, `telefono`, `email`, `estado`) VALUES
(12873501, 'SMANIA', 'Aldo Daniel', 'Olga Orozco', 2147483647, 'santiagosmania@hotmail.com', 'habilitado'),
(43811734, 'SMANIA', 'Moreno', 'Bv Ocampo 327', 2147483647, 'santiagosmania@hotmail.com', 'habilitado'),
(89488196, '', '', '', 0, '', '');
-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `especies`
--

CREATE TABLE `especies` (
  `idespecie` int(255) NOT NULL,
  `especie` varchar(100) NOT NULL,
  `idespecie` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `especies`
--


INSERT INTO `especies` (`idespecie`, `especie`) VALUES
(1, 'felino'),
(2, 'equino'),
(3, 'caninos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `examenclinico`
--

CREATE TABLE `examenclinico` (
  `idexamenc` int(255) NOT NULL,
  `ganglios` varchar(100) NOT NULL,
  `mucosas` varchar(100) NOT NULL,
  `temperatura` varchar(100) NOT NULL,
  `cardiaca` varchar(100) NOT NULL,
  `pulso` varchar(100) NOT NULL,
  `respiratoria` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial`
--

CREATE TABLE `historial` (
  `idhistorial` int(255) NOT NULL,
  `idpaciente` int(255) NOT NULL,
  `fecha` date NOT NULL,
  `peso` decimal(65,0) NOT NULL,
  `fechadesp` date NOT NULL,
  `productodesp` varchar(100) NOT NULL,
  `idvacuna` int(255) NOT NULL,
  `lotev` mediumtext NOT NULL,
  `fechacelo` date NOT NULL,
  `fechapart` date NOT NULL,
  `estirilizado` text NOT NULL,
  `consulta` mediumtext NOT NULL,
  `hallazgo` mediumtext NOT NULL,
  `idexamenc` int(255) NOT NULL,
  `idpeso` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
--

CREATE TABLE `pacientes` (
  `idpaciente` int(255) NOT NULL,
  `dni` int(255) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `idraza` int(255) NOT NULL,
  `sexo` text NOT NULL,
  `estado` varchar(100) NOT NULL,
  `seniaspart` varchar(255) NOT NULL,
  `chip` int(100) DEFAULT NULL,
  `idespecie` int(255) NOT NULL,
  `fechana` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pacientes`
--

INSERT INTO `pacientes` (`idpaciente`, `dni`, `nombre`, `idraza`, `sexo`, `estado`, `seniaspart`, `chip`, `idespecie`, `fechana`) VALUES
(1, 89488196, 'felix', 1, 'M', 'habilitado', 'mancha', 0, 1, '2000-10-20'),
(2, 43811734, 'Romelin', 3, 'M', 'habilitado', 'mancha', 250202, 2, '2004-06-27');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `peso`
--

CREATE TABLE `peso` (
  `idpeso` int(255) NOT NULL,
  `peso` decimal(65,0) NOT NULL,
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `razas`
--

CREATE TABLE `razas` (
  `idraza` int(255) NOT NULL,
  `raza` varchar(100) NOT NULL
   
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `razas`
--
INSERT INTO `razas` (`idraza`, `raza`,`idespecie`) VALUES
(1, 'siames', 1),
(2, 'Bulldog Ingles', 3),
(3, 'Árabe', 2);



-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sesion`
--

CREATE TABLE `sesion` (
  `id` int(255) NOT NULL,
  `DNI` int(100) NOT NULL,
  `contrasena` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `sesion`
--

INSERT INTO `sesion` (`id`, `DNI`, `contrasena`) VALUES
(1, 43811734, 'pepito123');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `turnos`
--

CREATE TABLE `turnos` (
  `dni` int(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `celular` int(100) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time(6) NOT NULL,
  `tipo` text NOT NULL,
  `idturno` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `turnos`
--

INSERT INTO `turnos` (`dni`, `email`, `celular`, `fecha`, `hora`, `tipo`, `idturno`) VALUES
(43811734, 'santiagosmania@hotmail.com', 2147483647, '2023-10-20', '10:00:00.000000', '', 2),
(12873501, 'santiago.smania@gmail.com', 2147483647, '2023-10-19', '11:00:00.000000', '', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vacunas`
--

CREATE TABLE `vacunas` (
  `idvacuna` int(255) NOT NULL,
  `laboratorio` varchar(100) NOT NULL,
  `vacuna` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`dni`);

--
-- Indices de la tabla `especies`
--
ALTER TABLE `especies`
  ADD PRIMARY KEY (`idespecie`),
  ADD KEY `idraza` (`idraza`);

--
-- Indices de la tabla `examenclinico`
--
ALTER TABLE `examenclinico`
  ADD PRIMARY KEY (`idexamenc`);

--
-- Indices de la tabla `historial`
--
ALTER TABLE `historial`
  ADD PRIMARY KEY (`idhistorial`),
  ADD KEY `idpaciente` (`idpaciente`),
  ADD KEY `idvacuna` (`idvacuna`),
  ADD KEY `idexamenc` (`idexamenc`),
  ADD KEY `idpeso` (`idpeso`);

--
-- Indices de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`idpaciente`),
  ADD KEY `dni` (`dni`),
  ADD KEY `idespecie` (`idespecie`),
  ADD KEY `idraza` (`idraza`);

--
-- Indices de la tabla `peso`
--
ALTER TABLE `peso`
  ADD PRIMARY KEY (`idpeso`);

--
-- Indices de la tabla `razas`
--
ALTER TABLE `razas`
  ADD PRIMARY KEY (`idraza`);

--
-- Indices de la tabla `sesion`
--
ALTER TABLE `sesion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `turnos`
--
ALTER TABLE `turnos`
  ADD PRIMARY KEY (`idturno`),
  ADD KEY `dni` (`dni`);

--
-- Indices de la tabla `vacunas`
--
ALTER TABLE `vacunas`
  ADD PRIMARY KEY (`idvacuna`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `especies`
--
ALTER TABLE `especies`
  MODIFY `idespecie` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `examenclinico`
--
ALTER TABLE `examenclinico`
  MODIFY `idexamenc` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `historial`
--
ALTER TABLE `historial`
  MODIFY `idhistorial` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  MODIFY `idpaciente` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `peso`
--
ALTER TABLE `peso`
  MODIFY `idpeso` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `razas`
--
ALTER TABLE `razas`
  MODIFY `idraza` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `sesion`
--
ALTER TABLE `sesion`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `turnos`
--
ALTER TABLE `turnos`
  MODIFY `idturno` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `vacunas`
--
ALTER TABLE `vacunas`
  MODIFY `idvacuna` int(255) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `especies`
--
ALTER TABLE `especies`
  ADD CONSTRAINT `especies_ibfk_1` FOREIGN KEY (`idraza`) REFERENCES `razas` (`idraza`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `historial`
--
ALTER TABLE `historial`
  ADD CONSTRAINT `historial_ibfk_1` FOREIGN KEY (`idpeso`) REFERENCES `peso` (`idpeso`) ON UPDATE CASCADE,
  ADD CONSTRAINT `historial_ibfk_2` FOREIGN KEY (`idvacuna`) REFERENCES `vacunas` (`idvacuna`) ON UPDATE CASCADE,
  ADD CONSTRAINT `historial_ibfk_3` FOREIGN KEY (`idexamenc`) REFERENCES `examenclinico` (`idexamenc`) ON UPDATE CASCADE,
  ADD CONSTRAINT `historial_ibfk_4` FOREIGN KEY (`idpaciente`) REFERENCES `pacientes` (`idpaciente`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD CONSTRAINT `pacientes_ibfk_1` FOREIGN KEY (`idespecie`) REFERENCES `especies` (`idespecie`) ON UPDATE CASCADE,
  ADD CONSTRAINT `pacientes_ibfk_3` FOREIGN KEY (`dni`) REFERENCES `clientes` (`dni`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `turnos`
--
ALTER TABLE `turnos`
  ADD CONSTRAINT `turnos_ibfk_1` FOREIGN KEY (`dni`) REFERENCES `clientes` (`dni`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
