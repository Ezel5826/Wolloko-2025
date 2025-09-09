//me quedó pendiente la clase de gallina, lograr hacer el metodo de enfermarse, 
//que se pueda enfermar en diferentes aspectos, que te permita ver stats y hacer una especie de matadero tambien que 
//se enfermen cuando estan con otras diferencias por tipos de animales y añadir una zona de cuarentena. tenes mas posibilidad de que se cure con 
//las demas,pero a diferencia de la cuarentena, tambien tenes chanse de que se contagien otras, asimismo, en la cuarentena no se contagian con otras
//pero tiene menos chanse de curado. todo esto apartir de los 3 dias.
//tambien agregar un objeto posicion que me permita saber la posicion actual y en base a eso tengo que saber donde está y definir un radio para enfermar
//estoy haciendo la asignaicon de las enfermedades para ver si afecta o no al animal.
class Kikiriki inherits Animals(posicion=0,ubicacion="corral",peso=30, vacunado = false, muerto = false, hambriento = true, bebido = false, enfermo = false, diasHabiles = 10){
    const comidaTolerada = ["zanahoria","calabaza"]
    override method comer(cantidad,comida) {
        peso+=cantidad    
    }

}

class Oink inherits Animals(posicion=0,ubicacion="chiquero", peso=30, vacunado = false, muerto = false, hambriento = true, bebido = false, enfermo = false, diasHabiles = 20){
    var property pesoMinimo = 200
    var property vecesRestantes = 3
    const comidaTolerada = ["zanahoria","calabaza"]
    method vacunarse() {
        vacunado=true      
    }

    override method comer(cantidad,comida) {
        if (!bebido) {console.println("el cerdo debe ser abrevado para que pueda comer")}
        else if (peso<=pesoMinimo) {hambriento = false}
        else {mataderojeje = true}
        peso += cantidad/2
        if(vecesRestantes == 0) {bebido = false}
        else {vecesRestantes -= 1}
        if (comidaTolerada.count({comidaV => comidaV==comida.type()}) != 1){
            self.EnfermarPorComer(comida.type())
        }
    }
    override method abrevar() {
        bebido=true
    }

}
class Muuu inherits Animals(posicion=0,ubicacion="pastal", peso=50, vacunado = false, muerto = false, hambriento = true, bebido = false, enfermo = false, diasHabiles = 30){
    var property ciclos = 1
    var property pesoMinimo = 400
    var property comidaTolerada = ["heno","pasto"]
    method vacunarse() {
      if (ciclos!=0){ciclos-=1 vacunado=true}
    }
    method caminar(cantidadRecorrida) {
        if (peso - cantidadRecorrida/5 > 0)
        peso -= cantidadRecorrida/5        
    }
    override method comer(cantidad,comida) {
        if (!bebido) {console.println("la vaca debe ser abrevada para que pueda comer")}
        else if (peso<=pesoMinimo) {hambriento = false}
        else if(diasVivo>=60 && peso>=pesoMinimo){mataderojeje = true}
        peso += cantidad/2
        bebido=false
        if (comidaTolerada.count({comidaV => comidaV==comida.type()}) != 1){
            self.EnfermarPorComer(comida.type())
        }
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

    const numeroComidaEnfermo = 1

    method comer(cantidad,comida) {}
    method abrevar() {}
    method morir() {
        if (diasHabiles < diasEnfermo && enfermo){muerto=true enfermo=false console.println("su animal ha muerto")}
        if (enfermo){console.println(["su animal esta enfermo, le quedan", diasHabiles-diasEnfermo,"de vida"])}
    }
    method enfermarse() {
        if(!enfermo){enfermo=true}
         
    }
    method EnfermarPorComer(comida) {//comida= comida.tipe
            const num = 0.roundUpTo(10).floor()
            if (num==numeroComidaEnfermo){
                self.enfermarse()
            }
    }

    // method kind (instacia) {
    // const enfermedad = enfermedades.elegirEnfermedad()
    // //a ver si funciona esta
    //     if (instacia.kindName() == new Muuu().kindName()) {

    //     }else if (instacia.kindName() == new Kikiriki().kindName()){

    //     }else if (instacia.kindName() == new Oink().kindName()){

    //     }else{

    //     }}

    // method curarse(){
    //     const num = 0.roundUpTo(10).floor()
    //     if (!enfermo){return true}
        
    //     if (ubicacion != "Cuarentena" && num <= 4 ){
    //         enfermo=false
    //         return true
    //     }
    //     return false
  
    // }
}

class Granja {
    const property animales = [] 
    var property days =  0 
    const property comidasPosibles = ["maiz","insectos","pasto","heno","zanahoria","calabaza"]
    const property comida = [] 

    method CrearAnimales(cantidad,clase) {
    if (clase == "a Oink"){ const corral = [] cantidad.times({i => animales.add(new Oink())})}
    else if (clase == "a Muuu") cantidad.times({i => animales.add(new Muuu())})
    else if (clase =="a Kikiriki") cantidad.times({i => animales.add(new Kikiriki())})
    else {
        console.println("el animal que quieres agregar a la granja no se encuentra en nuestro terreno")
        return
    }}

    method CrearComida(cantidad,cantidadAlimentar,tipo) {
        if (comidasPosibles.contains(tipo)) {cantidad.times({i => comida.add(new Comida(type=tipo, valorEnergetico=cantidadAlimentar))})}
        else{
            console.println("has elegido un nombre de comida no disponible, ingrese de vuelta")
            return
        }
    }

    method Procrear(instance) {
        self.CrearAnimales(1, instance)      
    }

}
class  Comida {
    const property type  
    const property valorEnergetico 
}
object matadero {}

class Enfermedades{}

const enfermedades = new Enfermedades()

const granja = new Granja()