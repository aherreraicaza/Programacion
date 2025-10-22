1. Cadenas de texto(str)
• .upper() → Convierte todo a MAYÚSCULAS
• .lower() → Convierte todo a minúsculas
• .capitalize() → Primera letra en mayúscula
• .title() → Primera letra de cada palabra en mayúscula
• .strip() → Elimina espacios en los extremos
• .replace('a', 'b') → Sustituye un texto por otro
• .find('x') → Devuelve la posición donde aparece algo(o - 1)
• .split(',') → Divide el texto en partes(lista)
• .join(lista) → Une una lista en un string con un separador
• .startswith('x') → Comprueba si empieza con 'x'
• .endswith('y') → Comprueba si termina con 'y'
• .isdigit() → True si son solo números
• .isalpha() → True si son solo letras
• .isalnum() → True si son letras y números


2. Listas(list)
• .append(x) → Agrega un elemento al final
• .insert(i, x) → Inserta en una posición
• .remove(x) → Elimina la primera aparición de un valor
• .pop(i) → Elimina y devuelve el elemento
• .sort() → Ordena la lista en el mismo lugar(modifica la original) se puede combinar con reverse para invertir el orden
• .reverse() → Invierte el orden
• .index(x) → Devuelve posición de un valor
• .count(x) → Cuenta cuántas veces aparece
• .copy() → Copia la lista
• .clear() → Vacía la lista
. sorted(listanum) devuelve una lista nueva ordenada sin modificar la original

3. Tuplas(tuple)
• .count(x) → Cuenta cuántas veces aparece un valor
• .index(x) → Devuelve la posición de un valor


4. Diccionarios(dict)
• .get(clave, defecto) → Obtiene el valor de forma segura
• .keys() → Devuelve todas las claves
• .values() → Devuelve todos los valores
• .items() → Devuelve lista de pares(clave, valor)
• .update({}) → Actualiza o agrega pares
• .pop(clave) → Elimina y devuelve el valor de una clave
• .clear() → Vacía el diccionario


5. Conjuntos(set)
• .add(x) → Agrega un elemento
.remove(x) → Elimina un elemento(error si no existe)
• .discard(x) → Elimina un elemento(sin error)
• .pop() → Elimina un elemento aleatorio
• .union(otro) → Une conjuntos
• .intersection(otro) → Devuelve los comunes
• .difference(otro) → Elementos que están en uno pero no en otro
• .symmetric_difference(otro) → Elementos no compartidos


6. Archivos(file)
• .read() → Lee todo el contenido
• .readline() → Lee una línea
• .readlines() → Lista con todas las líneas
• .write('texto') → Escribe en el archivo
• .writelines(lista) → Escribe varias líneas
• .close() → Cierra el archivo


7. Números(int, float)
• abs(x) → Valor absoluto
• round(x, n) → Redondea
• pow(x, y) → Potencia
• divmod(a, b) → Devuelve(cociente, resto)


8. Funciones y Clases
• Funciones definidas con def no tienen métodos internos, pero sí atributos.
• Clases pueden definir métodos propios.
• Métodos especiales(dunder methods): __init__, __str__, __len__, __getitem__, __setitem__,