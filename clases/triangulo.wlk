
class Poligono {
    const property a = 3
    const property b = 5
    const property c = 6

    method es_equilatero() = a==b and b==c 
    
    method es_isosceles() = a==b or a==c and a!=b or a!=c 

    method es_escaleno() = a!=b and b!=c 
}