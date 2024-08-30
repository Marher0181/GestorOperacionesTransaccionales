CREATE DATABASE LaboratorioNo1_Grupo1
USE LaboratorioNo1_Grupo1

CREATE TABLE TipoCuenta(
	idTipoCuenta INT PRIMARY KEY,
	nombreTipoCuenta VARCHAR(max),
	CONSTRAINT chk_nombreTipoCuenta CHECK (nombreTipoCuenta IN ('ahorro', 'monetaria'))
)
GO

insert into TipoCuenta values (1, 'Ahorro')
insert into TipoCuenta values (2, 'Monetaria')

CREATE TABLE TipoTransaccion(
	idTipoTransaccion INT PRIMARY KEY,
	nombreTipoTransaccion VARCHAR(max),
	CONSTRAINT chk_nombreTipoTransaccion CHECK (nombreTipoTransaccion IN ('depósito', 'retiro', 'transferencia'))
)
GO

insert into TipoTransaccion values (1, 'Depósito')
insert into TipoTransaccion values (2, 'Retiro')
insert into TipoTransaccion values (3, 'Transferencia')


CREATE TABLE Empleados(
	idEmpleado INT IDENTITY(1,1) PRIMARY KEY,
	nombreEmpleado VARCHAR(max),
	cargo VARCHAR(50),
	fechaContratacion DATE,
	salario BIGINT,
	telefono VARCHAR(25),
	email VARCHAR(MAX)
)
GO

CREATE TABLE Cliente(
	idCliente INT IDENTITY(1,1) PRIMARY KEY,
	numeroIdentificacion INT,
	nombreCliente VARCHAR(MAX),
	direccionCliente VARCHAR(MAX),
	email VARCHAR(MAX),
	telefono VARCHAR(MAX)
)
GO
CREATE TABLE Sucursales(
	idSucursal INT IDENTITY(1,1) PRIMARY KEY,
	nombreSucursal VARCHAR(MAX),
	direccionSucursal VARCHAR(MAX),
	idEmpleadoResponsable INT,
	CONSTRAINT fk_EmpleadoResponsable FOREIGN KEY (idEmpleadoResponsable) REFERENCES Empleados(idEmpleado)
)
GO

CREATE TABLE CuentasBancarias(
	idCuentaBancaria INT IDENTITY(1,1) PRIMARY KEY,
	numeroCuenta VARCHAR(MAX),
	saldo BIGINT,
	fechaApertura DATE DEFAULT GETDATE(),
	idCliente INT,
	idTipoCuenta INT, 
	CONSTRAINT fk_clientePropietario FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
	CONSTRAINT fk_tipoCuenta FOREIGN KEY (idTipoCuenta) REFERENCES TipoCuenta(idTipoCuenta)
)
GO

CREATE TABLE Transacciones(
	idTransaccion INT IDENTITY(1,1),
	idTipoTransaccion INT,
	fechaTransaccion DATETIME DEFAULT GETDATE(),
	monto BIGINT,
	idCuentaBancariaOrigen INT NOT NULL,
	idCuentaBancariaDestino INT,
	idSucursal INT
	CONSTRAINT fk_TipoTransaccion FOREIGN KEY (idTipoTransaccion) REFERENCES TipoTransaccion(idTipoTransaccion),
	CONSTRAINT fk_cuentaOrigen FOREIGN KEY (idCuentaBancariaOrigen) REFERENCES CuentasBancarias(idCuentaBancaria),
	CONSTRAINT fk_cuentaDestino FOREIGN KEY (idCuentaBancariaDestino) REFERENCES CuentasBancarias(idCuentaBancaria),
	CONSTRAINT fk_sucursal FOREIGN KEY (idSucursal) REFERENCES Sucursales(idSucursal)
)
GO

/*
SP PARA CREAR
*/


CREATE OR ALTER PROCEDURE [dbo].[sp_GestionarCuentasBancarias]
@Seleccion varchar(max),
@numeroCuenta varchar(max),
@saldo DECIMAL(10,2),
@idCliente INT,
@idTipoCuenta INT
AS 
BEGIN
    BEGIN TRY
        BEGIN TRANSACTION;
			IF @Seleccion = 'Insertar'
			BEGIN

				INSERT INTO CuentasBancarias(numeroCuenta, saldo, fechaApertura, idCliente,	idTipoCuenta)
				VALUES(@numeroCuenta, @saldo, GETDATE(), @idCliente, @idTipoCuenta)
			END

			IF @Seleccion = 'Eliminar'
			BEGIN 
				delete from CuentasBancarias
				Where numeroCuenta = @numeroCuenta

			END
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
		if @@TRANCOUNT>0
		begin
			rollback transaction;
			print('Realiz  un rollback de la transacci n')
		end;
		declare @ErrorMessage nvarchar(4000) =Error_Message();
		declare @ErrorSeverity int = Error_severity();
		declare @ErrorState int = Error_State();
		raiserror(@ErrorMessage,@errorseverity,@errorstate)
		print(@ErrorMessage)
		print(@errorseverity)
		print(@errorstate)
	end catch
end;
GO

CREATE OR ALTER PROCEDURE  [dbo].[sp_GestionarSucursales]
@Seleccion varchar(max),
@nombreSucursal varchar(max),
@direccionSucursal varchar(max),
@idEmpleadoResponsable INT
AS 
BEGIN
    BEGIN TRY
        BEGIN TRANSACTION;
			IF @Seleccion = 'Insertar'
			BEGIN

				INSERT INTO Sucursales(nombreSucursal, direccionSucursal, idEmpleadoResponsable)
				VALUES(@nombreSucursal, @direccionSucursal, @idEmpleadoResponsable)
			END
			select * from Sucursales
			IF @Seleccion = 'Eliminar'
			BEGIN 
				delete from Sucursales Where nombreSucursal = @nombreSucursal

			END
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
		if @@TRANCOUNT>0
		begin
			rollback transaction;
			print('Realiz  un rollback de la transacci n')
		end;
		declare @ErrorMessage nvarchar(4000) =Error_Message();
		declare @ErrorSeverity int = Error_severity();
		declare @ErrorState int = Error_State();
		raiserror(@ErrorMessage,@errorseverity,@errorstate)
		print(@ErrorMessage)
		print(@errorseverity)
		print(@errorstate)
	end catch
end;
GO


CREATE OR ALTER PROCEDURE  [dbo].[sp_GestionarCliente]
@Seleccion varchar(max),
@numeroIdentificacion INT,
@nombreCliente VARCHAR(MAX),
@direccionCliente VARCHAR(MAX),
@email VARCHAR(MAX),
@telefono VARCHAR(MAX)
AS 
BEGIN
    BEGIN TRY
        BEGIN TRANSACTION;
			IF @Seleccion = 'Insertar'
			BEGIN

				INSERT INTO Cliente(numeroIdentificacion, nombreCliente, direccionCliente, email, telefono)
				VALUES(@numeroIdentificacion, @nombreCliente, @direccionCliente, @email,@telefono)
			END

			IF @Seleccion = 'Eliminar'
			BEGIN 
				delete from Cliente Where numeroIdentificacion = @numeroIdentificacion

			END
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
		if @@TRANCOUNT>0
		begin
			rollback transaction;
			print('Realiz  un rollback de la transacci n')
		end;
		declare @ErrorMessage nvarchar(4000) =Error_Message();
		declare @ErrorSeverity int = Error_severity();
		declare @ErrorState int = Error_State();
		raiserror(@ErrorMessage,@errorseverity,@errorstate)
		print(@ErrorMessage)
		print(@errorseverity)
		print(@errorstate)
	end catch
end;
GO


CREATE OR ALTER PROCEDURE  [dbo].[sp_GestionarEmpleados]
	@Seleccion VARCHAR(MAX),
	@idEmpleado int,
	@nombreEmpleado VARCHAR(max),
	@cargo VARCHAR(50),
	@salario BIGINT,
	@telefono VARCHAR(25),
	@email VARCHAR(MAX)
	AS
	BEGIN
    BEGIN TRY
        BEGIN TRANSACTION;
			IF @Seleccion = 'Insertar'
			BEGIN

				INSERT INTO Empleados(nombreEmpleado, cargo, salario, telefono, email)
				VALUES(@nombreEmpleado, @cargo, @salario, @telefono,@email)
			END
			IF @Seleccion = 'Eliminar'
			BEGIN 
				delete from Empleados Where idEmpleado = @idEmpleado
			END
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
		if @@TRANCOUNT>0
		begin
			rollback transaction;
			print('Realiz  un rollback de la transacci n')
		end;
		declare @ErrorMessage nvarchar(4000) =Error_Message();
		declare @ErrorSeverity int = Error_severity();
		declare @ErrorState int = Error_State();
		raiserror(@ErrorMessage,@errorseverity,@errorstate)
		print(@ErrorMessage)
		print(@errorseverity)
		print(@errorstate)
	end catch
end;
GO


/*


DEPOSITOS, RETIROS, TRANSFERENCIAS


*/

CREATE OR ALTER PROCEDURE  [dbo].[sp_Deposito]
    @numeroCuenta varchar(max),
    @monto Decimal(10,2),
    @idSucursal INT
AS
BEGIN
    BEGIN TRY
        BEGIN TRANSACTION;

        UPDATE CuentasBancarias 
        SET saldo = saldo + @monto
        WHERE numeroCuenta = @numeroCuenta;

        DECLARE @idCuentaOrigen INT;
        SELECT @idCuentaOrigen = idCuentaBancaria
        FROM CuentasBancarias
        WHERE numeroCuenta = @numeroCuenta;
		
        IF @idCuentaOrigen IS NULL

        BEGIN
            RAISERROR('Número de cuenta no encontrado.', 16, 1);
            ROLLBACK TRANSACTION;
            RETURN;
        END

        INSERT INTO Transacciones (idTipoTransaccion, fechaTransaccion, monto, idCuentaBancariaOrigen, idSucursal)
        VALUES (1, GETDATE(), @monto, @idCuentaOrigen, @idSucursal);

        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
        BEGIN
            ROLLBACK TRANSACTION;
            PRINT('Realicé un rollback de la transacción');
        END;

        DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
        DECLARE @ErrorSeverity INT = ERROR_SEVERITY();
        DECLARE @ErrorState INT = ERROR_STATE();
        RAISERROR(@ErrorMessage, @ErrorSeverity, @ErrorState);
        PRINT(@ErrorMessage);
        PRINT(@ErrorSeverity);
        PRINT(@ErrorState);
    END CATCH
END;
GO

CREATE OR ALTER PROCEDURE  [dbo].[sp_Retiro]
    @numeroCuenta varchar(max),
    @monto decimal(10, 2),
    @idSucursal INT
AS
BEGIN
    BEGIN TRY
        BEGIN TRANSACTION;
		DECLARE @Saldo BIGINT;
		Select @Saldo = saldo 
		from CuentasBancarias 
		WHERE numeroCuenta = @numeroCuenta;
		IF @monto < @Saldo
		BEGIN
			UPDATE CuentasBancarias 
			SET saldo = saldo - @monto
			WHERE numeroCuenta = @numeroCuenta;

			DECLARE @idCuentaOrigen INT;
			SELECT @idCuentaOrigen = idCuentaBancaria
			FROM CuentasBancarias
			WHERE numeroCuenta = @numeroCuenta;
		
	        IF @idCuentaOrigen IS NULL

			BEGIN
				RAISERROR('Número de cuenta no encontrado.', 16, 1);
				ROLLBACK TRANSACTION;
				RETURN;
			END

			INSERT INTO Transacciones (idTipoTransaccion, fechaTransaccion, monto, idCuentaBancariaOrigen, idSucursal)
			VALUES (2, GETDATE(), @monto, @idCuentaOrigen, @idSucursal);

		END
		ELSE
		BEGIN
				PRINT 'MONTO SUPERA AL SALDO DISPONIBLE'
				ROLLBACK TRANSACTION;
				RETURN;
		END
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
        BEGIN
            ROLLBACK TRANSACTION;
            PRINT('Realicé un rollback de la transacción');
        END;

        DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
        DECLARE @ErrorSeverity INT = ERROR_SEVERITY();
        DECLARE @ErrorState INT = ERROR_STATE();
        RAISERROR(@ErrorMessage, @ErrorSeverity, @ErrorState);
        PRINT(@ErrorMessage);
        PRINT(@ErrorSeverity);
        PRINT(@ErrorState);
    END CATCH
END;
GO

CREATE OR ALTER PROCEDURE  [dbo].[sp_Transaccion]
    @numeroCuenta varchar(max),
    @monto decimal(10, 2),
    @idSucursal INT,
	@numeroCuentaDestino VARCHAR(MAX)
AS
BEGIN
    BEGIN TRY
        BEGIN TRANSACTION;
		DECLARE @Saldo BIGINT;
		Select @Saldo = saldo 
		from CuentasBancarias 
		WHERE numeroCuenta = @numeroCuenta;
		IF @monto < @Saldo
			BEGIN
			UPDATE CuentasBancarias 
			SET saldo = saldo + @monto
			WHERE numeroCuenta = @numeroCuenta;

			DECLARE @idCuentaOrigen INT;
			SELECT @idCuentaOrigen = idCuentaBancaria
			FROM CuentasBancarias
			WHERE numeroCuenta = @numeroCuenta;
		
			IF @idCuentaOrigen IS NULL

			BEGIN
				RAISERROR('Número de cuenta no encontrado.', 16, 1);
				ROLLBACK TRANSACTION;
				RETURN;
			END

			UPDATE CuentasBancarias 
			SET saldo = saldo + @monto
			WHERE numeroCuenta = @numeroCuentaDestino;

			DECLARE @idCuentaDes INT;
			SELECT @idCuentaDes = idCuentaBancaria
			FROM CuentasBancarias
			WHERE numeroCuenta = @numeroCuentaDestino;
		
			IF @idCuentaOrigen IS NULL

			BEGIN
				RAISERROR('Número de cuenta no encontrado.', 16, 1);
				ROLLBACK TRANSACTION;
				RETURN;
			END
			
			INSERT INTO Transacciones (idTipoTransaccion, fechaTransaccion, monto, idCuentaBancariaOrigen, idCuentaBancariaDestino, idSucursal)
			VALUES (3, GETDATE(), @monto, @idCuentaOrigen, @idCuentaDes, @idSucursal);
		END
		ELSE
		BEGIN
				PRINT 'MONTO SUPERA AL SALDO DISPONIBLE'
				ROLLBACK TRANSACTION;
				RETURN;
		END


        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
        BEGIN
            ROLLBACK TRANSACTION;
            PRINT('Realicé un rollback de la transacción');
        END;

        DECLARE @ErrorMessage NVARCHAR(4000) = ERROR_MESSAGE();
        DECLARE @ErrorSeverity INT = ERROR_SEVERITY();
        DECLARE @ErrorState INT = ERROR_STATE();
        RAISERROR(@ErrorMessage, @ErrorSeverity, @ErrorState);
        PRINT(@ErrorMessage);
        PRINT(@ErrorSeverity);
        PRINT(@ErrorState);
    END CATCH
END;
GO


/*


CONSULTAS



*/



SELECT numeroIdentificacion, nombreCliente, numeroCuenta, saldo FROM Cliente 
LEFT JOIN CuentasBancarias on Cliente.idCliente = CuentasBancarias.idCliente

SELECT DISTINCT * from TipoCuenta

SELECT * FROM Cliente Where nombreCliente LIKE 'J%'

SELECT * FROM Transacciones WHERE idSucursal IN (3);

SELECT * FROM Transacciones WHERE fechaTransaccion between '2024-07-29' and '2024-08-30' 

SELECT * FROM CuentasBancarias WHERE Saldo > (SELECT AVG(Saldo) FROM CuentasBancarias);

SELECT idTipoTransaccion, COUNT(*) AS TotalTransacciones FROM Transacciones GROUP BY idTipoTransaccion;

SELECT idTipoTransaccion, COUNT(*) AS TotalTransacciones FROM Transacciones GROUP BY idTipoTransaccion HAVING COUNT(*) > 3;

SELECT COUNT(*) as CuentasActivas FROM CuentasBancarias

SELECT SUM(Saldo) AS TotalDepositos FROM CuentasBancarias WHERE idTipoCuenta = 2;

SELECT MAX(Saldo) AS MayorSaldo, MIN(Saldo) AS MenorSaldo FROM CuentasBancarias;

