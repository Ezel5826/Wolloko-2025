object colectivo {
    const max_pasajeros = 100 
    const max_nafta = 200
    var sense = 1 
    var nafta_actual = null
    var property gente_sobrante = false 
    var property pasajeros_subidos = null 
    var property cant_gente_sobrante = null
    var property cant_gente_a_subir = null

    method avanzar() {   

    }
    

    method bajar_pasajeros() {
      
    }  

    method volver() {
      
    }

    method volver_urgencia() {
    
    }
    method recargar_nafta() {nafta_actual = max_nafta}

    method sobra_gente() =  (ruta.cant_gente_in_parada() + pasajeros_subidos) > max_pasajeros

    method nafta_insuficiente() = self.gasto_nafta_por_ruta() >= max_nafta

    method gasto_nafta(pasajeros) = 1 + 0.1 * pasajeros

    method gasto_nafta_paradas_restantes() = self.gasto_nafta(pasajeros_subidos) * ruta.paradas_restantes()

    method gasto_nafta_por_ruta() = self.gasto_nafta(ruta.gente_total()) * ruta.cant_paradas()

    method cant_vueltas_a_dar() = (ruta.gente_total() / max_pasajeros).round()

    // method sobra_gente(ruta) =  (ruta.cant_gente_in_parada() + pasajeros_subidos) > max_pasajeros

    // method nafta_insuficiente(gente_total) = self.gasto_nafta_por_ruta(gente_total) >= max_nafta

    // method gasto_nafta(pasajeros) = 1 + 0.1 * pasajeros

    // method gasto_nafta_paradas_restantes(paradas_restantes) = self.gasto_nafta(pasajeros_subidos) * paradas_restantes

    // method gasto_nafta_por_ruta(gente_total) = self.gasto_nafta(gente_total) * ruta.cant_paradas()

    // method cant_vueltas_a_dar(gente_total) = ( gente_total / max_pasajeros).round()
}

class Ruta {
    var property parada_actual = 0 
    var property parada_sig = parada_actual + 1
    const property paradas = []
    var property cant_total_gente = 0
    var property cant_total_sobrante = 0 
    var x = 0

    method add(cant_paradas) {cant_paradas.times({x => paradas.add(new Paradas(cant_minima=3, cant_maxima=10,gente_sobrante=0))})} //anda
    
    method gente_total() {paradas.forEach({parada => x += parada.cant_gente()}) if (cant_total_gente != x) {cant_total_gente = x} x = 0 return cant_total_gente} //anda 
    
    method cant_paradas() = paradas.size() //anda

    method cant_gente_in_parada() = paradas.get(parada_actual).cant_gente() //anda

    method paradas_restantes() = self.cant_paradas() - parada_actual //anda

}

class Paradas {
    var property cant_minima 
    var property cant_maxima
    var property cant_gente = cant_minima.randomUpTo(cant_maxima).round()
    var property gente_sobrante 
    method restar_pasajeros(pasajeros_a_restar) {
    if (cant_gente - pasajeros_a_restar >= 1){cant_gente -= pasajeros_a_restar}
    }

}

const ruta = new Ruta()
