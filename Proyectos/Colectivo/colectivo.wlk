import wollok.vm.*

object colectivo {
    var sense = 1 
    const property max_pasajeros = 10
    const property max_nafta = 100
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
        if (!self.llegaConGastoMinimoNafta() && ruta.parada_actual()==0) return "la capacidad de su tanque no es suficiente para recorrer las paradas."
        if (self.recorridoTerminado()) {self.bajar_pasajeros() return "ya ha terminado su recorrido"}
        nafta_actual -= self.gasto_nafta(pasajeros_subidos)
        if (ruta.parada_actual() + sense >= 0 && ruta.parada_actual() + sense <= ruta.cantParadas()) {ruta.parada_actual(ruta.parada_actual() + sense)}
        if (ruta.obtenerGente(ruta.parada_actual()) != 0) {self.subir_gente(ruta.obtenerGente(ruta.parada_actual()))}
        self.VolverNoSobranPasajeros()
        self.volverCapacidadLlena()
        self.bajar_pasajeros()
        return ["Pasajeros Subidos:", pasajeros_subidos, "nafta actual:" , nafta_actual, "sentido:", sense, "vueltas:" , vueltas, "parada actual:", ruta.parada_actual()]
    }

    method VolverNoSobranPasajeros() {
        if(ruta.genteTotalInRuta()==0 && vueltas!=0){
            sense*=-1
            genteSobrante=false
        }      
    }
    method volverCapacidadLlena() {
        //añadir logica que te permita ver is te conviene ams ir de un lado que del otro, eso en tema de nafta. por ejemplo etas en la 4 y son 9, quiza por la nafta te convenga ir mas al inicio que a la terminal.
        
        if((pasajeros_subidos==max_pasajeros && vueltas!=0)&& sense!=1) sense*=-1

    }
    method pruebas(float){
        float.floor()
        return float

    }
    method bajar_pasajeros() {
        if (self.recorridoTerminado() || (ruta.parada_actual() == 0 && vueltas != 0) || self.llegaTerminal()) {
            ruta.parada(ruta.parada_actual()).sumar_pasajeros(pasajeros_subidos)
            pasajeros_subidos = 0
            
            if (!self.recorridoTerminado() && ruta.parada_actual()==ruta.cantParadas()) {
                sense*=-1
                vueltas += 1               
            }
            
            self.recargar_nafta(ruta.recargarNafta())
        }
    }

    method subir_gente(cantidad_pasajeros) {

        if (pasajeros_subidos <= 0)  pasajeros_subidos *= 0
        if (self.llegaConGastoMinimoNafta()){
        if ((self.gasto_nafta_paradas_restantes(pasajeros_subidos + cantidad_pasajeros.floor()) <= nafta_actual) && (pasajeros_subidos + cantidad_pasajeros.floor() <= max_pasajeros) && (ruta.parada_actual() >= 0 && ruta.parada_actual() <= ruta.cantParadas()) && ( cantidad_pasajeros >= 0)) {
            
            pasajeros_subidos += cantidad_pasajeros.floor()

            ruta.parada(ruta.parada_actual()).restar_pasajeros(cantidad_pasajeros)
            
            if (ruta.obtenerGente(ruta.parada_actual()) != 0) genteSobrante = true
    
        } else if(cantidad_pasajeros >= 0) {
             self.subir_gente(cantidad_pasajeros - 1)
        }}
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

    method gasto_nafta_por_ruta() {
        nafta_ruta = 0
        if (ruta.cantParadas() <= 1) return nafta_ruta
        ruta.paradas().forEach({
            x => if (x.cant_gente() >= 0) {
                genteIterable += x.cant_gente() 
            } 
            nafta_ruta += self.gasto_nafta(genteIterable)
        })
        
        nafta_ruta -= self.gasto_nafta(genteIterable)
        
        genteIterable = 0 
        return nafta_ruta
    }

    method gasto_nafta_paradas_restantes(subir) {
        if (subir < 0 || ruta.parada_actual() < 0 || ruta.parada_actual() >= 5) return 0
        
        nafta_paradas_r = 0  
        genteIterable = subir 
        ruta.paradas().forEach({x => 
            if ((ruta.cantParadas() - iterador == ruta.paradas_restantes() - 1) && ruta.parada_actual() >= 0) {
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

    method gasto_nafta(pasajeros) = if (pasajeros >= 0) {1 + 0.1 * pasajeros.floor()} else {1}

    method recorridoTerminado() = ruta.parada_actual() == ruta.cantParadas() && !genteSobrante

    method llegaTerminal() = ruta.parada_actual() == ruta.cantParadas()

    method llegaConGastoMinimoNafta() = self.gasto_nafta(1) * ruta.cantParadas()-1 <= nafta_actual
}
class Ruta {
    var property parada_actual = 0 
    const property paradas = []
    var property cant_total_gente = 0
    var property gente_paradas = []
    var property recargarNafta = 50

    method cantParadas() = paradas.size() - 1

    method parada(paradaUbicada) = paradas.get(paradaUbicada) 

    method obtenerGente(paradaUbicada) = self.parada(paradaUbicada).cant_gente()

    method paradas_restantes() = self.cantParadas() - parada_actual

    method addParadas(cant_paradas) {
        cant_paradas.times({
            x => paradas.add(new Paradas(cant_minima = 10, cant_maxima = 50))
        })
        self.set_terminals()
        return self.gente_por_paradas()
    }

    method paradaPruebaAdd(paradaAñadir) {
        paradaAñadir.forEach({
            x => paradas.add(new Paradas(cant_gente = x))
            })
            self.set_terminals()
            return self.gente_por_paradas()
    } 

    method gente_por_paradas() {
        gente_paradas = [] 
        paradas.forEach({parada => gente_paradas.add(parada.cant_gente())})
        return gente_paradas
    }
    
    method set_terminals() {
        if (self.cantParadas() != 0) {
            self.parada(0).cant_gente(0)
            self.parada(self.cantParadas()).cant_gente(0)
        }
    }

    method genteTotalInRuta() {
        cant_total_gente = 0 
        paradas.forEach({parada => cant_total_gente += parada.cant_gente()})
        cant_total_gente -= self.obtenerGente(paradas.size() - 1)
        return cant_total_gente
    }
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

const ruta = new Ruta()
// const colectivo = new Colectivo()
// const hola = colectivo.avanzar()
