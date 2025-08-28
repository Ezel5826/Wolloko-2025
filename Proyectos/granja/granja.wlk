//me quedó pendiente la clase de gallina, lograr hacer el metodo de enfermarse, 
//que se pueda enfermar en diferentes aspectos, que te permita ver stats y hacer una especie de matadero tambien que 
//se enfermen cuando estan con otras diferencias por tipos de animales y añadir una zona de cuarentena. tenes mas posibilidad de que se cure con 
//las demas,pero a diferencia de la cuarentena, tambien tenes chanse de que se contagien otras, asimismo, en la cuarentena no se contagian con otras
//pero tiene menos chanse de curado. todo esto apartir de los 3 dias.
//tambien agregar un objeto posicion que me permita saber la posicion actual y en base a eso tengo que saber donde está y definir un radio para enfermar


class Kikiriki inherits Animals(peso=30, vacunado = false, muerto = false, hambriento = true, bebido = false, enfermo = false,mataderojeje = false, diasHabiles = 10){

}

class Oink inherits Animals(peso=30, vacunado = false, muerto = false, hambriento = true, bebido = false, enfermo = false,mataderojeje = false,diasHabiles = 20){
    var property pesoMinimo = 200
    var property vecesRestantes = 3
    method vacunarse() {
        vacunado=true      
    }

    override method comer(cantidad) {
        if (!bebido) {console.println("el cerdo debe ser abrevado para que pueda comer")}
        else if (peso<=pesoMinimo) {hambriento = false}
        else {mataderojeje = true}
        peso += cantidad/2
        if(vecesRestantes == 0) {bebido = false}
        else {vecesRestantes -= 1}
    }
    override method abrevar() {
        bebido=true
    }

}
class Muuu inherits Animals(peso=50, vacunado = false, muerto = false, hambriento = true, bebido = false, enfermo = false,mataderojeje = false, diasHabiles = 30){
    var property ciclos = 1
    var property pesoMinimo = 400

    method vacunarse() {
      if (ciclos!=0){ciclos-=1 vacunado=true}
    }
    method caminar(cantidadRecorrida) {
        if (peso - cantidadRecorrida/5 > 0)
        peso -= cantidadRecorrida/5
        
    }

    override method comer(cantidad) {
        if (!bebido) {console.println("la vaca debe ser abrevada para que pueda comer")}
        else if (peso<=pesoMinimo) {hambriento = false}
        peso += cantidad/2
        bebido=false
    }
    override method abrevar() {
      bebido=true
    
    }

}
class Animals {
    var property peso 
    var property vacunado 
    var property muerto 
    var property hambriento 
    var property bebido 
    var property enfermo 
    var property diasEnfermo = 0
    var property mataderojeje = false
    var property diasHabiles 
    var property diasVivo = 0 
    var property ubicacion  
    var property posicion 
    method comer(cantidadComida) {}
    method abrevar() {}
    method morir() {
        if (diasHabiles < diasEnfermo && enfermo){muerto=true enfermo=false console.println("su animal ha muerto")}
        if (enfermo){console.println(["su animal esta enfermo, le quedan", diasHabiles-diasEnfermo,"de vida"])}
    }
    method enfermarse() {
        if(!enfermo){enfermo=true}
    }
    method curarse(){
        const num = 0.roundUpTo(10).floor()
        if (!enfermo){return true}
        
        if (ubicacion != "Cuarentena" && num <= 4 ){
            enfermo=false
            return true
        }
        return false
  
    }
}
class Granja {
    const property animales = [] 
    method CrearAnimales(cantidad,clase) {

    if (clase=="oink") cantidad.times({i => animales.add(new Oink())})

    else if (clase== "muuu") cantidad.times({i => animales.add(new Muuu())})

    else if (clase=="kikiriki") cantidad.times({i => animales.add(new Kikiriki())})

    else {
        console.println("el animal que quieres agregar a la granja no se encuentra en nuestro terreno")
        return
    }
    }

}
object matadero {}

const granja = new Granja()