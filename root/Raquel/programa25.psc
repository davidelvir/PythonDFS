Proceso Programa25
	
	Definir nombre como caracter;
	Definir nsueldo, sueldo Como real; 
	Definir Respuesta Como Entero;
	
	Escribir "Desea ingresar al programa? SI(1) NO(2)"; 
	Leer Respuesta; 
	Mientras respuesta=1 Hacer
		Escribir "Ingrese el nombre del empleado";
		Leer nombre; 
		Escribir "Ingrese el sueldo del empleado";
		Leer Sueldo;
		//Proceso
		Si Sueldo<1000 Entonces
			Nsueldo<- Sueldo + Sueldo*0.15; 
		SiNo
			Si Sueldo>2500 Entonces
				Nsueldo<- Sueldo + Sueldo * 0.08;
			SiNo
				Nsueldo<- Sueldo + Sueldo * 0.10; 
			FinSi
		FinSi
		
		Escribir nombre;
		Escribir "Su sueldo es de: ", nSUELDO, "LPS."; 
		Escribir "Desea ingresar al programa? 1(SI) 2(NO)"; 
		Leer Respuesta; 
	FinMientras
	
	
FinProceso
