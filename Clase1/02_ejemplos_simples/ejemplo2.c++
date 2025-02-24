//  funcion para calcular el promedio de notas
#include <iostream>
using namespace std;
int main()
{
    int n, i;
    float nota, suma = 0, promedio;
    cout << "Ingrese el numero de notas: ";
    cin >> n;
    for (i = 1; i <= n; i++)
    {
        cout << "Ingrese la nota " << i << ": ";
        cin >> nota;
        suma += nota;
    }
    promedio = suma / n;
    cout << "El promedio de las notas es: " << promedio << endl;
    return 0;
}