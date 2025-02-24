// array con 8 nombre de personas
const personas = ["Juan", "María", "Pedro", "Ana", "Luis", "Laura", "Carlos", "Sofía"];

// recorrer el array y mostrar cada nombre en la consola
for (let i = 0; i < personas.length; i++) {
  console.log(personas[i]);
}

// recorre la lista y muestra cada nombre en la consola, preguntando por su edad
for (let i = 0; i < personas.length; i++) {
  const edad = prompt(`¿Cuántos años tiene ${personas[i]}?`);
  console.log(`${personas[i]} tiene ${edad} años.`);
}



// Alternativa
/* // array con 8 nombres de personas y su edad
const personas = [
  { nombre: "Pedro", edad: 20 },
  { nombre: "Juan", edad: 25 },
  { nombre: "Maria", edad: 30 },
  { nombre: "Luis", edad: 35 },
  { nombre: "Ana", edad: 40 },
  { nombre: "Carlos", edad: 45 },
  { nombre: "Laura", edad: 50 },
  { nombre: "Javier", edad: 55 },
];

// recorre la lista e imprima un saludo a cada persona de la siguiente manera "Hola persona, ¿Como estas?"
for (let i = 0; i < personas.length; i++) {
  const persona = personas[i];
  console.log(`Hola ${persona.nombre}, ¿Como estas?`);
}

// recorre el array y imprime el nombre y la edad de cada persona
for (let i = 0; i < personas.length; i++) {
  const persona = personas[i];
  console.log(`Nombre: ${persona.nombre}, Edad: ${persona.edad}`);
} */