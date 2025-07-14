import wollok.vm.*
object colectivo {
    const max_pasajeros = 100 
    var property pasajeros_subidos = 0 
    var property cant_gente_sobrante = 0
    var genteIterable = 0 
    const max_nafta = 50
    var property nafta_actual = max_nafta
    var sense = 1 
    var nafta_ruta = 0
    var nafta_paradas_r = 0
    var iterador = 0
    var vueltas = 0
    
    //me queda por hacer el metodo de sistema o como sea uqe lo llame pero que sirva para ver todos los datos importantes en tiempo real, es como si retornace todos los datos asi el usuario puede leerlos y poder por ejemplo "en la siguiente parada no podria subirse nadie" etc


    method avanzar() {   
        self.subir_gente(self.obtenerGente())
        self.bajar_pasajeros()
        if (ruta.parada_actual() + sense >= 0 && ruta.parada_actual() + sense <= ruta.paradas().size()-1){ruta.parada_actual(ruta.parada_actual() + sense)}
        nafta_actual -= self.gasto_nafta(pasajeros_subidos)
    }

    method bajar_pasajeros() {//anda
      if (ruta.parada_actual() == ruta.paradas().size()-1 || (ruta.parada_actual() == 0 && vueltas != 0) ){
        ruta.paradas().get(ruta.parada_actual()).sumar_pasajeros(pasajeros_subidos)
        pasajeros_subidos = 0
        if (cant_gente_sobrante != 0){sense *=-1  vueltas += 1}
        self.recargar_nafta(ruta.recargarNafta())
      }
    }  

    method subir_gente(cantidad_pasajeros) {//anda
        if (((self.gasto_nafta_paradas_restantes(pasajeros_subidos+cantidad_pasajeros,ruta.paradas()) <= nafta_actual ) && (pasajeros_subidos + cantidad_pasajeros <= max_pasajeros) && (ruta.parada_actual() != 0 || ruta.parada_actual()!=ruta.paradas().size()-1))){
            pasajeros_subidos += cantidad_pasajeros
            ruta.paradas().get(ruta.parada_actual()).restar_pasajeros(cantidad_pasajeros)
            cant_gente_sobrante += self.obtenerGente()
        } else{
            self.subir_gente(cantidad_pasajeros-1)
        }
    }

    method recargar_nafta(naftaRecargar) {if(naftaRecargar <= 0) return nafta_actual if (nafta_actual + naftaRecargar < max_nafta ) {nafta_actual += naftaRecargar} else { nafta_actual = max_nafta} return nafta_actual}
//me va a quedar para revisar esta que me daba mal los calculos, fuera de eso yo ya arreglé la de la nfata por apradas (la mas importante) asi que otro dia tengoq ue fijarme sobre porque falla.
    method gasto_nafta_por_ruta(paradas) {
        nafta_ruta = 0
        paradas.forEach({
        x => if (x >= 0){ 
        genteIterable += x //.cant_gente() esto es solo de pruebas, en desarollo
        } 
        nafta_ruta += self.gasto_nafta(genteIterable)
        })
        if (paradas.size() != 0) nafta_ruta -= self.gasto_nafta(genteIterable)
        genteIterable = 0 
        return nafta_ruta} //anda

    method gasto_nafta_paradas_restantes(subir, paradas, paradaActual) {
        if (subir < 0 || 0 > paradaActual || paradaActual >= 5) return 0
        nafta_paradas_r = 0  
        genteIterable = subir 
        paradas.forEach({x => 
        if ((paradas.size()-1 - iterador  == (paradas.size()-1 - paradaActual)-1) && paradaActual >= 0)//ruta.paradas_restantes()-1
        {
            nafta_paradas_r += self.gasto_nafta(genteIterable)
            if (x >= 0) genteIterable += x //.cant_gente()
            } else {
                iterador+=1
            }
        }) 

            genteIterable = 0 
            iterador = 0 

            return nafta_paradas_r
        }//anda
    
    method gasto_nafta(pasajeros) = if (pasajeros >= 0){1 + 0.1 * pasajeros.truncate(0)} else{ 1 } //anda

    method sobra_gente() = (ruta.cant_gente_in_parada() + pasajeros_subidos) > max_pasajeros //anda

    method cant_vueltas_a_dar(genteTotal) = (genteTotal / max_pasajeros).round() //anda

    method obtenerGente() = ruta.paradas().get(ruta.parada_actual()).cant_gente() 


    // method sobra_gente(ruta) =  (ruta.cant_gente_in_parada() + pasajeros_subidos) > max_pasajeros

    // method nafta_insuficiente(gente_total) = self.gasto_nafta_por_ruta(gente_total) >= max_nafta

    // method gasto_nafta(pasajeros) = 1 + 0.1 * pasajeros

    // method gasto_nafta_paradas_restantes(paradas_restantes) = self.gasto_nafta(pasajeros_subidos) * paradas_restantes

    // method gasto_nafta_por_ruta(gente_total) = self.gasto_nafta(gente_total) * ruta.cant_paradas()

    // method cant_vueltas_a_dar(gente_total) = ( gente_total / max_pasajeros).round()
}

class Ruta {
    var property parada_actual = 0 
    const property paradas = []
    var property cant_total_gente = 0
    var property gente_paradas = []
    var property recargarNafta = 50
    var suma_gente_parada = 0
    

    method add(cant_paradas) {cant_paradas.times({x => paradas.add(new Paradas(cant_minima=10, cant_maxima=50))}) self.set_terminals()} //anda
    
    method set_terminals() {paradas.get(0).cant_gente(0) paradas.get(paradas.size()-1).cant_gente(0)}//anda
    
    method gente_total() {paradas.forEach({parada => suma_gente_parada += parada.cant_gente()}) if (cant_total_gente != suma_gente_parada) {cant_total_gente = suma_gente_parada} suma_gente_parada = 0 return cant_total_gente} //anda 
    
    method cant_paradas() = paradas.size()-1 //anda
    
    method gente_por_paradas(){gente_paradas=[] paradas.forEach({parada => gente_paradas.add(parada.cant_gente())}) return gente_paradas}//anda

    method cant_gente_in_parada() = paradas.get(parada_actual).cant_gente() //anda

    method paradas_restantes() = self.cant_paradas() - parada_actual //anda

}

class Paradas {
    var property cant_minima 
    var property cant_maxima
    var property cant_gente = cant_minima.randomUpTo(cant_maxima).round()
    method restar_pasajeros(pasajeros_a_restar) {if(cant_gente - pasajeros_a_restar >= 0){cant_gente -= pasajeros_a_restar}}
    method sumar_pasajeros(pasajeros_a_sumar) {cant_gente += pasajeros_a_sumar}

}

const ruta = new Ruta()
