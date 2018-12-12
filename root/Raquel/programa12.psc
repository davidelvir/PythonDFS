Proceso programa12
	
	Definir salario_semanal, precio Como Real;
	Definir hrs Como Entero;
	
	Escribir "Ingrese las horas trabajadas por el empleado";
	Leer hrs;
	Escribir "Ingrese el precio por hora trabajada";
	Leer precio;
	
	Si hrs>40 Entonces
		salario_semanal <- (40*precio) + ((hrs-40)*1.5*precio);
	Sino
		salario_semanal <- hrs*precio;
	FinSi
	
	Escribir "El salario semanal es de: ", salario_semanal, "Lps.";
	
FinProceso
