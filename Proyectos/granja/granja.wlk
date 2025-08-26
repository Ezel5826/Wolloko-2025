//me quedó pendiente la clase de gallina, lograr hacer el metodo de enfermarse, 
//que se pueda enfermar en diferentes aspectos, que te permita ver stats y hacer una especie de matadero tambien que 
//se enfermen cuando estan con otras diferencias por tipos de animales y añadir una zona de cuarentena. tenes mas posibilidad de que se cure con 
//las demas,pero a diferencia de la cuarentena, tambien tenes chanse de que se contagien otras, asimismo, en la cuarentena no se contagian con otras
//pero tiene menos chanse de curado. todo esto apartir de los 3 dias.
class Kikiriki inherits Animals{

}

class Oink inherits Animals{
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
class Muuu inherits Animals{
    var property ciclos = 1
    var property pesoMinimo = 400

    method vacunarse() {
      if (ciclos!=0){ciclos-=1 vacunado=true}
    }
    method caminar(cantidadRecorrida) {
      peso += cantidadRecorrida/5
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
    method comer(cantidadComida) {}
    method abrevar() {}
    method morir() {
        if (diasHabiles < diasEnfermo && enfermo){muerto=true enfermo=false console.println("su animal ha muerto")}
        if (enfermo){console.println(["su animal esta enfermo, le quedan", diasHabiles-diasEnfermo,"de vida"])}
    }
    method enfermarse() {
      
    }
}
class Granja {
    const property animales = [] 
    method CrearAnimales(cantidad,clase) {

    if (clase=="oink") cantidad.times({i => animales.add(new Oink(peso=30, vacunado = false, muerto = false, hambriento = true, bebido = false, enfermo = false,mataderojeje = false,diasHabiles = 20))})

    else if (clase== "muuu") cantidad.times({i => animales.add(new Muuu(peso=50,ciclos=1, vacunado = false, muerto = false, hambriento = true, bebido = false, enfermo = false,mataderojeje = false, diasHabiles = 30))})

    else if (clase=="kikiriki") cantidad.times({i => animales.add(new Kikiriki(peso=30, vacunado = false, muerto = false, hambriento = true, bebido = false, enfermo = false,mataderojeje = false, diasHabiles = 10))})

    else {
        console.println("el animal que quieres agregar a la granja no se encuentra en nuestro terreno")
        return
    }
    }

}
object matadero {}

const granja = new Granja()