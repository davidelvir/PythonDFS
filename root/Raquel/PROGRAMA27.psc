Proceso programa27
	
	Definir respuesta Como Entero;
	Definir nombre, direccion Como Caracter;
	Definir inicial, final, cobro, consumo Como Real;
	
	Escribir "Desea ingresar al programa? SI (1), NO (2)";
	Leer respuesta;
	Mientras respuesta=1 Hacer
		Escribir "Ingrese el nombre del cliente.";
		Leer nombre;
		Escribir "Ingrese la direccion del cliente.";
		Leer direccion;
		Escribir "Ingrese el registro inicial.";
		Leer inicial;
		Escribir "Ingrese el registro final.";
		Leer final;
		
		consumo<- inicial+final;
		
		Si consumo <= 140 Entonces
			cobro <- consumo *3.20;
		Sino
			Si consumo > 140 y consumo<= 310 Entonces
				cobro <- (140*3.20) + ((consumo-140)*0.15);
			Sino
				Si consumo>310 Entonces
					cobro <- (140*3.20)+(170*0.15)+((consumo-310)*0.10);
				Sino
					cobro<- 0;
				FinSi
			FinSi
		FinSi
		
		Limpiar Pantalla;
		Escribir "";
		Escribir "******************";
		Escribir nombre;
		Escribir direccion;
		Escribir "Usted consumio: ",consumo, "KVH";
		Escribir "Su total a pagar es de: ", cobro, "LPS.";
		Escribir "*******************";
		Escribir "";
		Escribir "Desea ingresar al programa? SI (1), NO (2)";
		Leer respuesta;
	FinMientras
	
FinProceso
