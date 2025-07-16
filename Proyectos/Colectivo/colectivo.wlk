import wollok.vm.*

object colectivo {
    var sense = 1 
    const max_pasajeros = 30
    const property max_nafta = 300
    var property pasajeros_subidos = 0 
    var property genteSobrante = false
    var property nafta_actual = max_nafta
    var genteIterable = 0 
    var nafta_ruta = 0
    var nafta_paradas_r = 0
    var iterador = 0
    var vueltas = 0

    //me queda por hacer el metodo de sistema o como sea uqe lo llame
    //pero que sirva para ver todos los datos importantes en tiempo real,
    //es como si retornace todos los datos asi el usuario puede leerlos y
    //poder por ejemplo "en la siguiente parada no podria subirse nadie" etc

    method avanzar() {  
        if (!self.llegaConGastoMinimoNafta() && ruta.paradaActual()==0) return "la capacidad de su tanque no es suficiente para recorrer las paradas."
        if (self.recorridoTerminado()) {self.bajar_pasajeros() return "ya ha terminado su recorrido"}
        nafta_actual -= self.gasto_nafta(pasajeros_subidos)
        if (ruta.parada_actual() + sense >= 0 && ruta.parada_actual() + sense <= ruta.cantParadas()) {ruta.parada_actual(ruta.parada_actual() + sense)}
        if (self.obtenerGente() != 0) {self.subir_gente(self.obtenerGente())}
        self.VolverNoSobranPasajeros()
        self.volverCapacidadLlena()
        self.bajar_pasajeros()
        return ["Pasajeros Subidos:", pasajeros_subidos, "nafta actual:" , nafta_actual, "sentido:", sense, "vueltas:" , vueltas, "parada actual:", ruta.parada_actual()]
    }

    method VolverNoSobranPasajeros() {
        if(ruta.genteTotal()==0 && vueltas!=0){
            sense*=-1
            genteSobrante=false
        }      
    }
    method volverCapacidadLlena() {
        
        if((pasajeros_subidos==max_pasajeros && vueltas!=0)&& sense!=1) sense*=-1
        
    }
    method bajar_pasajeros() {
        if (self.recorridoTerminado() || (ruta.parada_actual() == 0 && vueltas != 0) || self.llegaTerminal()) {
            ruta.paradaActual().sumar_pasajeros(pasajeros_subidos)
            pasajeros_subidos = 0
            
            if (!self.recorridoTerminado() && ruta.parada_actual()==ruta.cantParadas()) {
                sense*=-1
                vueltas += 1               
            }
            
            self.recargar_nafta(ruta.recargarNafta())
        }
    }

    method subir_gente(cantidad_pasajeros) {
        if (self.gasto_nafta_paradas_restantes(pasajeros_subidos + cantidad_pasajeros, ruta.paradas(), ruta.parada_actual()) <= nafta_actual && (pasajeros_subidos + cantidad_pasajeros <= max_pasajeros) && (ruta.parada_actual() != 0 || ruta.parada_actual() != ruta.cantParadas())) {
            
            pasajeros_subidos += cantidad_pasajeros
            
            ruta.paradaActual().restar_pasajeros(cantidad_pasajeros)
            if (self.obtenerGente() != 0) {
                genteSobrante = true
            }

        } else {
            self.subir_gente(cantidad_pasajeros - 1)
        }
    }

    method recargar_nafta(naftaRecargar) {
        if (naftaRecargar <= 0) return nafta_actual
        if (nafta_actual + naftaRecargar < max_nafta) {
            nafta_actual += naftaRecargar
        } else {
            nafta_actual = max_nafta
        }
        return nafta_actual
    }

    method gasto_nafta_por_ruta(paradas) {
        nafta_ruta = 0
        paradas.forEach({
            x => if (x.cant_gente() >= 0) { 
                genteIterable += x.cant_gente() //esto es solo de pruebas, en desarrollo
            } 
            nafta_ruta += self.gasto_nafta(genteIterable)
        })
        
        if (paradas.size() != 0) nafta_ruta -= self.gasto_nafta(genteIterable)
        
        genteIterable = 0 
        return nafta_ruta
    }

    method gasto_nafta_paradas_restantes(subir, paradas, paradaActual) {
        if (subir < 0 || paradaActual < 0 || paradaActual >= 5) return 0
        
        nafta_paradas_r = 0  
        genteIterable = subir 
        paradas.forEach({x => 
            if ((ruta.cantParadas() - iterador == (ruta.cantParadas() - paradaActual) - 1) && paradaActual >= 0) {
                nafta_paradas_r += self.gasto_nafta(genteIterable)
                
                if (x.cant_gente() >= 0) genteIterable += x.cant_gente()
            } else {
                iterador += 1
            }
        }) 

        genteIterable = 0 
        iterador = 0 
        return nafta_paradas_r
    }

    method gasto_nafta(pasajeros) = 
        if (pasajeros >= 0) {1 + 0.1 * pasajeros.truncate(0)} else {1}

    method obtenerGente() = ruta.paradaActual().cant_gente()

    method recorridoTerminado() = ruta.parada_actual() == ruta.cantParadas() && !genteSobrante

    method llegaTerminal() = ruta.parada_actual() == ruta.cantParadas()

    method llegaConGastoMinimoNafta() = self.gasto_nafta(1) * ruta.cantParadas() <= nafta_actual
}
class Ruta {
    var property parada_actual = 0 
    const property paradas = []
    var property cant_total_gente = 0
    var property gente_paradas = []
    var property recargarNafta = 50
    var property paradasPrueba 
    method addParadas(cant_paradas) {
        cant_paradas.times({
            x => paradas.add(new Paradas(cant_minima = 10, cant_maxima = 50))
        })
        self.set_terminals(paradas)
        return self.gente_por_paradas()
    }

    method set_terminals(parada) {
        if (parada.size() != 0) {
            parada.get(0).cant_gente(0)
            parada.get(parada.size() - 1).cant_gente(0)
        }
    }

    method genteTotal() {
        cant_total_gente = 0 
        paradas.forEach({parada => cant_total_gente += parada.cant_gente()})
        cant_total_gente -= self.cant_gente_en_parada(paradas.size() - 1)
        return cant_total_gente
    }

    method cantParadas() = paradas.size() - 1

    method paradaActual() = ruta.paradas().get(ruta.parada_actual()) 

    method gente_por_paradas() {
        gente_paradas = [] 
        paradas.forEach({parada => gente_paradas.add(parada.cant_gente())})
        return gente_paradas
    }

    method cant_gente_en_parada(parada) = paradas.get(parada).cant_gente()

    method paradas_restantes() = self.cantParadas() - parada_actual
}
class Paradas {
    var property cant_minima = 0
    var property cant_maxima = 0
    var property cant_gente = cant_minima.randomUpTo(cant_maxima).round()

    method restar_pasajeros(pasajeros_a_restar) {
        if (cant_gente - pasajeros_a_restar >= 0) {cant_gente -= pasajeros_a_restar}
    }

    method sumar_pasajeros(pasajeros_a_sumar) {cant_gente += pasajeros_a_sumar}
}

const ruta = new Ruta(paradasPrueba=[])
// const colectivo = new Colectivo()
// const hola = colectivo.avanzar()
