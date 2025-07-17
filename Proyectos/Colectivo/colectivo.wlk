import wollok.vm.*

object colectivo {
    const property maxPasajeros = 10
    const property maxNafta = 100
    var property pasajerosSubidos = 0 
    var property genteSobrante = false
    var property naftaActual = maxNafta
    var genteIterable = 0 
    var naftaRuta = 0
    var naftaParadasR = 0
    var iterador = 0
    var sense = 1 
    var vueltas = 0

    method sistema() {
      console.println(["la cantidad de pasajeros subidos es: ",pasajerosSubidos])
      console.println(["\n la cantidad de nafta restante es:", naftaActual , " y su consumo por avanzar fue de:", maxNafta-naftaActual])
      console.println(["actualmente se encuentra en la parada:", ruta.paradaActual(), " la cual posee", ruta.obtenerGente(ruta.paradaActual()), "personas"])
      console.println(["la cantidad de gente que sobró en la parada tras la subida fue de:", ruta.obtenerGente(ruta.paradaActual())])
      console.println(["se encuentra en la vuelta Nmero: ", vueltas, " y posee un sentido", sense])
      console.println(["la ruta en la cual está posicionado se encontró modificada a:", ruta.gentePorParadas()])
      console.println(["la cantidad de personas restantes en su recorrido es de: ",ruta.genteTotalInRuta()])
      console.println(["su recorrido se encuentra a ",ruta.paradasRestantes()," de terminar, ¿desea continuar?"])
    }
    method avanzar() {  
        if (!self.llegaConGastoMinimoNafta() && ruta.paradaActual()==0) return false
        if (self.recorridoTerminado()) {self.bajarPasajeros() return false}
        naftaActual -= self.gastoNafta(pasajerosSubidos)
        if (ruta.paradaActual() + sense >= 0 && ruta.paradaActual() + sense <= ruta.cantParadas()) {ruta.paradaActual(ruta.paradaActual() + sense)}
        if (ruta.obtenerGente(ruta.paradaActual()) != 0) {self.subirGente(ruta.obtenerGente(ruta.paradaActual()))}
        self.VolverNoSobranPasajeros()
        self.volverCapacidadLlena()
        self.bajarPasajeros()
        self.sistema()
        return true
    }

    method VolverNoSobranPasajeros() {
        if(ruta.genteTotalInRuta()==0 && vueltas!=0){
            sense*=-1
            genteSobrante=false
        }      
    }
    method volverCapacidadLlena() {
        //añadir logica que te permita ver is te conviene ams ir de un lado que del otro, eso en tema de nafta. por ejemplo etas en la 4 y son 9, quiza por la nafta te convenga ir mas al inicio que a la terminal.
        
        if((pasajerosSubidos==maxPasajeros && vueltas!=0)&& sense!=1) sense*=-1

    }

    method bajarPasajeros() {
        if (self.recorridoTerminado() || (ruta.paradaActual() == 0 && vueltas != 0) || self.llegaTerminal()) {
            ruta.parada(ruta.paradaActual()).sumarPasajeros(pasajerosSubidos)
            pasajerosSubidos = 0
            
            if (!self.recorridoTerminado() && ruta.paradaActual()==ruta.cantParadas()) {
                sense*=-1
                vueltas += 1
            }
            
            self.recargarNafta(ruta.recargarNafta())
        }
    }
    method senseVuletas() = [sense,vueltas] 

    method subirGente(cantidadPasajeros) {

        if (pasajerosSubidos <= 0)  pasajerosSubidos *= 0
        if (self.llegaConGastoMinimoNafta()){
        if ((self.gastoNaftaParadasRestantes(pasajerosSubidos + cantidadPasajeros.floor()) <= naftaActual) && (pasajerosSubidos + cantidadPasajeros.floor() <= maxPasajeros) && (ruta.paradaActual() >= 0 && ruta.paradaActual() <= ruta.cantParadas()) && ( cantidadPasajeros >= 0)) {
            
            pasajerosSubidos += cantidadPasajeros.floor()

            ruta.parada(ruta.paradaActual()).restarPasajeros(cantidadPasajeros)
            
            if (ruta.obtenerGente(ruta.paradaActual()) != 0) genteSobrante = true
    
        } else if(cantidadPasajeros >= 0) {
             self.subirGente(cantidadPasajeros - 1)
        }}
    }

    method recargarNafta(naftaRecargar) {
        if (naftaRecargar <= 0) return naftaActual
        if (naftaActual + naftaRecargar < maxNafta) {
            naftaActual += naftaRecargar
        } else {
            naftaActual = maxNafta
        }
        return naftaActual
    }

    method gastoNaftaPorRuta() {
        naftaRuta = 0
        if (ruta.cantParadas() <= 1) return naftaRuta
        ruta.paradas().forEach({
            x => if (x.cantGente() >= 0) {
                genteIterable += x.cantGente() 
            } 
            naftaRuta += self.gastoNafta(genteIterable)
        })
        
        naftaRuta -= self.gastoNafta(genteIterable)
        
        genteIterable = 0 
        return naftaRuta
    }

    method gastoNaftaParadasRestantes(subir) {
        if (subir < 0 || ruta.paradaActual() < 0 || ruta.paradaActual() >= 5) return 0
        
        naftaParadasR = 0  
        genteIterable = subir 
        ruta.paradas().forEach({x => 
            if ((ruta.cantParadas() - iterador == ruta.paradasRestantes() - 1) && ruta.paradaActual() >= 0) {
                naftaParadasR += self.gastoNafta(genteIterable)
                
                if (x.cantGente() >= 0) genteIterable += x.cantGente()
            } else {
                iterador += 1
            }
        }) 

        genteIterable = 0 
        iterador = 0 
        return naftaParadasR
    }


    method gastoNafta(pasajeros) = if (pasajeros >= 0) {1 + 0.1 * pasajeros.floor()} else {1}

    method recorridoTerminado() = ruta.paradaActual() == ruta.cantParadas() && !genteSobrante

    method llegaTerminal() = ruta.paradaActual() == ruta.cantParadas()

    method llegaConGastoMinimoNafta() = self.gastoNafta(1) * ruta.cantParadas()-1 <= naftaActual
}
class Ruta {
    var property paradaActual = 0 
    const property paradas = []
    var property cantTotalGente = 0
    var property genteParadas = []
    var property recargarNafta = 50

    method cantParadas() = paradas.size() - 1

    method parada(paradaUbicada) = paradas.get(paradaUbicada) 

    method obtenerGente(paradaUbicada) = self.parada(paradaUbicada).cantGente()

    method paradasRestantes() = self.cantParadas() - paradaActual

    method addParadas(cantParadas) {
        cantParadas.times({
            x => paradas.add(new Paradas(cantMinima = 10, cantMaxima = 50))
        })
        self.setTerminals()
        return self.gentePorParadas()
    }

    method paradaPruebaAdd(paradaAniadir) {
        paradaAniadir.forEach({
            x => paradas.add(new Paradas(cantGente = x))
            })
            self.setTerminals()
            return self.gentePorParadas()
    } 

    method gentePorParadas() {
        genteParadas = [] 
        paradas.forEach({parada => genteParadas.add(parada.cantGente())}) 
        return genteParadas
    }
    
    method setTerminals() {
        if (self.cantParadas() != 0) {
            self.parada(0).cantGente(0)
            self.parada(self.cantParadas()).cantGente(0)
        }
    }

    method genteTotalInRuta() {
        cantTotalGente = 0 
        paradas.forEach({parada => cantTotalGente += parada.cantGente()})
        cantTotalGente -= self.obtenerGente(paradas.size() - 1)
        return cantTotalGente
    }
}

class Paradas {
    var property cantMinima = 0
    var property cantMaxima = 0
    var property cantGente = cantMinima.randomUpTo(cantMaxima).round()

    method restarPasajeros(pasajerosARestar) {
        if (cantGente - pasajerosARestar >= 0) {cantGente -= pasajerosARestar}
    }

    method sumarPasajeros(pasajerosASumar) {cantGente += pasajerosASumar}
}

const ruta = new Ruta()