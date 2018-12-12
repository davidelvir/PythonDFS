Proceso programa23
	
	Definir sueldo Como Real;
	Definir turno, horas Como Entero;
	
	Escribir "";
	Escribir "*********";
	Escribir "BIENVENIDO";
	ESCRIBIR "**********";
	ESCRIBIR "";
	Escribir "Mañana.....(0)";
	Escribir "Tarde......(1)";
	Escribir "Ingrese el turno en el que trabaja el empleado.";
	Leer turno;
	Escribir "Ingrese el numero de horas semanales trabajadas por el empleado.";
	Leer horas;
	Limpiar Pantalla;
	
	Si turno = 0 y horas <= 40 Entonces
		sueldo <- horas * 60;
	Sino
		Si turno = 0 y horas > 40 Entonces
			sueldo <- (40*60) + ((horas-40)*2*60);
		Sino
			Si turno = 1 y horas <= 40 Entonces
				sueldo <- horas *80;
			Sino
				Si turno =1 y horas >40 Entonces
					sueldo <- (40*80) + ((horas-40)*3*80);
				Sino
					sueldo <- 0;
				FinSi
			FinSi
		FinSi
	FinSi

	
		
	Escribir "";
	Escribir "********************************";
	Escribir "";
	Escribir "El sueldo total es de: ", sueldo, "Lps.";
	escribir "";
	Escribir "********************************";
	Escribir "";
	Escribir "Gracias";
FinProceso

