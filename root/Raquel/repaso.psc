Proceso repaso
	Definir respuesta, tipop, dias, bueno, estreno, finde Como Entero;
	Definir pelicula como caracter;
	Definir costo, rebaja, total, descuento, incremento como real;
	
	Escribir "Desea Ingresar al programa? 1.SI, 2.NO";
	Leer respuesta;
	Mientras respuesta=1 Hacer
		Escribir "------------------------------";
		Escribir "    ALQUUILER DE PELICULAS     ";
		Escribir " 1. DRAMA";
		Escribir " 2. TERROR";
		Escribir " 3. ACCION";
		Escribir "Que tipo de pelicula desea alquilar?";
		Leer tipop;
		Escribir "Cuantos dias desea alquilarla?";
		Leer dias;
		Escribir "Ha sido cliente por mas de dos años? 1.SI, 2.NO";
		Leer bueno;
		
		Segun tipop Hacer
			1://DRAMA
				pelicula<- "DRAMA";
				costo<- 8*dias;
				Si bueno =1 Entonces
					rebaja <- (dias-1)*0.50;
				Sino
					rebaja<- 0;
				FinSi
				Escribir "La pelicula que lleva es estreno? 1.SI, 2.NO";
				Leer estreno;
				Si estreno=1 Entonces
					incremento <- dias*1.50;
				Sino
					incremento<- 0;
				FinSi
				descuento <- 0;
				total <- costo-rebaja+incremento-descuento;
			
			2://TERROR
				pelicula<- "TERROR";
				costo<- 10*dias;
				Si bueno =1 Entonces
					rebaja <- (dias-1)*0.50;
				Sino
					rebaja<- 0;
				FinSi
				incremento<- 0;
				descuento <- 0;
				total <- costo-rebaja+incremento-descuento;
			3://ACCION
				pelicula<- "ACCION";
				costo<- 9*dias;
				Si bueno =1 Entonces
					rebaja <- (dias-1)*0.50;
				Sino
					rebaja<- 0;
				FinSi
				Escribir "La pelicula que lleva es estreno? 1.SI, 2.NO";
				Leer estreno;
				Si estreno=1 Entonces
					incremento <- dias*1.50;
				Sino
					incremento<- 0;
				FinSi
				Escribir "La rento durante un fin de semana?(VIERNES, SABADO, DOMINGO) 1.SI, 2.NO";
				LEER finde;
				Si finde =1 Entonces
					descuento<- costo*0.10;
				Sino
					descuento<- 0;
				FinSi
				total <- costo-rebaja+incremento-descuento;
			De Otro Modo:
			
				costo<- 0;
				rebaja<- 0;
				incremento<- 0;
				descuento<- 0;
				total<- 0;
		FinSegun
		
		
		Escribir "Presione enter para continuar...";
		Esperar Tecla;
		Limpiar Pantalla;
		
		Escribir "---------------------------------------------";
		Escribir "      ALQUILER DE PELICULAS        ";
		Escribir "---------------------------------------------";
		Escribir "Usted selecciono: ", pelicula;
		Escribir "Usted alquilo las peliculas por: ", dias, " dias";
		Escribir "---------------------------------------------";
		
		Escribir "EL costo original es de: LPS.", COSTO;
		si bueno =1 entonces
			Escribir "***USTED ES CLIENTE FRECUENTE!***";
			Escribir "****Obtiene una rebaja de: LPS.", REBAJA, "****";
		FinSi
		
		si incremento>0 Entonces
				Escribir "***Su pelicula es estreno.***";
				Escribir "***Se le cobra un incremento de: LPS.", incremento, "***";
			FinSi
			
		
		si descuento >0 entonces
			Escribir "Por ser fin de semana, tiene un descuento de: LPS.", descuento;	
			FinSi
		Escribir "----------------------------------------------";
		Escribir "Su total es de: LPS. ", total;
		Escribir "----------------------------------------------";
		
		
		
		
		
		
		
		
		
		
		
		Escribir "Presione enter para continuar...";
		Esperar Tecla;
		Limpiar Pantalla;
		Escribir "Desea Ingresar al programa? 1.SI, 2.NO";
		Leer respuesta;
	FinMientras
	
FinProceso
