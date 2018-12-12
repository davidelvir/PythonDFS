Proceso programa11
	
	Definir nombre Como Caracter;
	Definir C1, c2, c3, c4, c5, average Como Real;
	
	Escribir "Escriba el nombre del alumno";
	Leer nombre;
	Escribir "Escriba la calificacion 1 del alumno";
	Leer c1;
	Escribir "Escriba la calificacion 2 del alumno";
	Leer c2;
	Escribir "Escriba la calificacion 3 del alumno";
	Leer c3;
	Escribir "Escriba la calificacion 4 del alumno";
	Leer c4;
	Escribir "Escriba la calificacion 5 del alumno";
	Leer c5;
	
	average<- (c1+c2+c3+c4+c5)/5;
	
	Escribir nombre;
	Escribir average, "%";
	
	Si average < 60 Entonces
		Escribir "NO APROBADO";
	Sino
		Escribir "APROBADO";
	FinSi
FinProceso
