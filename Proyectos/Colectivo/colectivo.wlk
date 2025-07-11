import wollok.vm.*
object colectivo {
    const max_pasajeros = 100 
    var property pasajeros_subidos = 0 
    var property cant_gente_sobrante = 0
    var genteIterable = 0 
    const max_nafta = 50
    var nafta_actual = 100
    var sense = 1 
    var nafta_ruta = 0
    var nafta_paradas_r = 0
    var iterador = 0
    var vueltas = 0
    
    method avanzar() {   
        if (ruta.parada_actual() + sense <=ruta.paradas().size()-1 && ruta.parada_actual() + sense >= 0){ruta.parada_actual(ruta.parada_actual() + sense)}
        self.subir_gente(ruta.paradas().get(ruta.parada_actual()).cant_gente())
        self.bajar_pasajeros()   
        
    }
    method bajar_pasajeros() {//anda
      if (ruta.parada_actual()==ruta.paradas().size()-1 || (ruta.parada_actual()==0 && vueltas!= 0) ){
        ruta.paradas().get(ruta.parada_actual()).sumar_pasajeros(pasajeros_subidos)
        pasajeros_subidos = 0
        if (cant_gente_sobrante != 0){sense *=-1  vueltas += 1}
        // self.recargar_nafta()
      }
    }  

    method subir_gente(cantidad_pasajeros) {//anda
        if (((self.gasto_nafta_paradas_restantes(pasajeros_subidos+cantidad_pasajeros) <= nafta_actual ) && (pasajeros_subidos + cantidad_pasajeros <= max_pasajeros) && (ruta.parada_actual() != 0 || ruta.parada_actual()!=ruta.paradas().size()-1))){
            nafta_actual -= self.gasto_nafta(pasajeros_subidos)
            pasajeros_subidos += cantidad_pasajeros
            ruta.paradas().get(ruta.parada_actual()).restar_pasajeros(cantidad_pasajeros)
            cant_gente_sobrante += ruta.paradas().get(ruta.parada_actual()).cant_gente()
        }else{
            self.subir_gente(cantidad_pasajeros-1)
        }
    }

    method recargar_nafta() {if (nafta_actual + ruta.recargar_nafta() < max_nafta) {nafta_actual += ruta.recargar_nafta()}else{ nafta_actual = max_nafta}}
//me va a quedar para revisar esta que me daba mal los calculos, fuera de eso yo ya arreglé la de la nfata por apradas (la mas importante) asi que otro dia tengoq ue fijarme sobre porque falla.
    method gasto_nafta_por_ruta() {nafta_ruta = 0 ruta.paradas().forEach({x => genteIterable += x.cant_gente() nafta_ruta += self.gasto_nafta(genteIterable)})genteIterable = 0 return nafta_ruta} //anda

    method gasto_nafta_paradas_restantes(subir) {
        nafta_paradas_r = 0  
        ruta.paradas().forEach({x => 
        if (ruta.paradas().size()-1 - iterador  == ruta.paradas_restantes()-1){

            genteIterable = subir 
            genteIterable += x.cant_gente()
            nafta_paradas_r += self.gasto_nafta(genteIterable)
            
            } else {
                iterador+=1
                }
            }) 

            genteIterable = 0 
            iterador = 0 
            return nafta_paradas_r
        }//anda
    
    method sobra_gente() = (ruta.cant_gente_in_parada() + pasajeros_subidos) > max_pasajeros //anda

    method gasto_nafta(pasajeros) = 1 + 0.1 * pasajeros //anda

    method cant_vueltas_a_dar() = (ruta.gente_total() / max_pasajeros).round() //anda

    method nafta_insuficiente() = self.gasto_nafta_por_ruta() >= max_nafta //anda




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
    var property recargar_nafta = 50
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
