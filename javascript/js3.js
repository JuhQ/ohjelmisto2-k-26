function greet() {
  console.log("moi")
  return
}

greet()

const greet2 = function() {
  console.log("moi2")
}

greet2()

const greet3 = () => {
  console.log("moi3")
}

greet3()


greet()

const param = (muuttuja) => {
  console.log("muuttuja", muuttuja)
}

param()
param("birds are real")
param("juha")


const paramN = (muuttuja, toinen) => {
  console.log("muuttuja", muuttuja)
  console.log("toinen", toinen)
}

paramN(1,2, 3, 4, 5)

paramN()


const paramN2 = (nimi, opiskelijanumero, kurssit, b, c, d) => {
  //console.log("muuttuja", muuttuja)
  //console.log("toinen", toinen)
  //console.log("a", a)
  console.log("b", b)
  console.log("c", c)
}

paramN2(1,2,3)

const plussaArvot_1 = function(a, b) {
  return a + b;
}

function plussaaArvot(a,b) {
  return a + b;
}

const plussaaArvot2 = (a, b) => {
  return a + b;
}

const plussaaArvot3 = (a,b) => a + b