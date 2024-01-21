# Projecte-1--Zelda

Para poder jugar solo necesitas tener descargado los archivos de dentro de la carpeta M3, el resto 
es contenido de otras asignaturas. Pero puedes revisarlo si sientes curiosidad :)


		(obviamente para que funcione necesitas un editor de codigo con extension de python)

- nota: ajusta la consola de tu editor de codigo con "emular terminal en output console" para ver bien el juego y funcione el clear. 

+ EXPLICACIÓN DEL JUEGO:

El objetivo del juego es rescatar a Zelda de las manos del malvado Ganon,
para esto, Link (o nosotros mismos) tendremos que emprender una aventura, explorando
y combatiendo para llegar a nuestro objetivo, el Castillo. 
Pero antes de todo, tienes que saber como funciona este mundo.

+ PRIMEROS PASOS:

Cuando entras al mundo de Zelda por primera vez, podras ver un menú principal
con multiples opciones:


	- New Game: Empieza tu aventura!!!
	- Help: Abre un menú de ayuda si no sabes como seguir.
	- About: Información extra acerca de la creación de este mundo. 
	- Exit: Sales de este mundo y vuelves al tuyo.
	- Continue: Si ya habias empezado una aventura, puedes seguir tu camino.


+ NEW GAME:

Lo primero de todo es presentarse no? Prueba a decirle tu nombre de aventurero 
a ver que pasa. O escribe Help si no sabes que decir.

+ LEGEND Y PLOT:
Estas dos secciones te pondran en contexto de la situación actual en el reino de
Hyrule


+ GAME: 

Como se puede apreciar, este mundo es visualmente simple. Pero ojo, este no deja de ser peligroso!!!

- PANTALLA:

El gran rectangulo es el mapa de la zona donde te encuentras. Y el pequeño rectangulo de la derecha es tu inventario.

-MAPA:En total hay 4 regiones del mapa y una central, el castillo. (img mapa grande)

 
 	 El conocimiento es saber,  asi que a continuación tienes un registro de los simbolos con los que te puedes encontrar en
	 tu aventura y su significado: siempre puedes ver el mapa introduciendo: Show map

X, el personatge (Link)
O son piedras
C son cocinas
T,TX són arbres

~ és aigua
F són un 'Fox
M, un cofre tancat
W, un cofre obert
SX,SX? són santuaris (? si no lo conoces)
EX enemigo (X es la vida)

- INVENTARIO: Esta zona de la pantalla te muestra todos los objetos, alimentos e información de tu partida actual
	tenemos tres invemtarios diferents a los cuales puedes cambiar escribiendo: 
	- Show inventory main (muestra información general)
	- Show inventory weapons (información detallada armas)
	- Show inventory Food (informacion detallada comida)

si necesitas ayuda para entenderlo, escribe show inventory help.

- ACCIONES: Una vez conocido el mundo que nos rodea, toca aprender como interactuar y desplazarnos por este mundo.
	- ENTORNO:En todo momento te saldrán las acciones disponibles que peudes realizar en ese momento.

	- GO: para desplazarte por el mapa tienes tres opciones:
		-go left/right/up/down 'numero': te desplazas el numero de casillas indicado, si nada te corta el paso claro.
		-go by 'objetivo': te permite ir al lado de un simbolo, o lo mas cercano a este que puedas.
		-go to 'region': pasa a alguna de las otras localizaciones del mapa, pero ten en cuenta que solo puedes acceder a las
				contiguas.  
	- EAT: para comer y recuperar salud, solo tienes que introducir eat 'alimento'.
	- EQUIP/UNEQUIP: para equiparte un arma, introduce: equip the 'nombre arma', y para desequipar: unequip the 'nombre arma'
		ten en cuenta que las armas tienen un uso limitado y estas se rompen.
		als armas de madera tienen 5 usos, y las normales 9.
	- COOK: A lado de una olla (C) te permite cocinar alimentos más nutritivos, para para hacerlo pon: cook 'alimento'
	- FISH: Al lado de agua puedes intentar atrapar algun pez escurridizo
	- OPEN: cuando estes cerca de un cofre o un santuario,introduce open 'objetivo'.
	- ATTACK: Siempre que estes al lado de un objeto que pueda ser atacado aparecera esta opcion, realizala escribiendo: attack. 

	
			

- TIPS DEL JUEGO:

	- CONSEGUIR COMIDA: la comida es un recurso esencial, prueba a pescar, matar a un animal o atacar a un arbol...	 
	- BLOOD MOON: cada 25 acciones aparecera la bloodmoon, un fenomeno natural que revive a tus enemigops vencidos!!!
	- RESET DE COFRES: Si has abierto todos los cofres y te quedas sin armas no te preocupes, estos volverán a cerrarse por arte de magia.
	- SANTUARIO ABIERTO: Cada vez que abras un santurario, te embriagas de energia divina y tu vida aumenta en 1. 
			     Quizas esta sea la clave para vencer al tirano Ganon...

+ FINALES: Por desgracia solo hay dos desenlaces posibles para esta aventura, salvar a Zelda o morir en el intento.

Pero tranquilo/a, si mueres puedes aprender de tus errores y reaparecer en el ultimo punto de guardado que tengas.

